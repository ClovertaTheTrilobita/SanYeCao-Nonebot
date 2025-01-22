# 引入sqlalchemy依赖
from pathlib import Path
from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.qq import Message, MessageEvent, MessageSegment

from src.image.get_image import get_image_names
from src.my_sqlite.models.fortune import QrFortune,QrFortuneLog

fortune_by_sqlite = on_command("今日运势", rule=to_me(), priority=10, block=True)
@fortune_by_sqlite.handle()
async def get_today_fortune(message: MessageEvent):

    local_image_path = get_image_names()
    member_openid = message.get_user_id()
    # 查询今日是否已经获取过今日运势，如果获取过则直接从日志取
    result = await QrFortuneLog.is_get_fortune_log(member_openid)
    if result is None:
        # 获取 运势说明
        result = await QrFortune.get_fortune()
        # 把抽取的今日运势插入日志
        await QrFortuneLog.insert_fortune_log(result, member_openid)

    content = ("\n" + "您的今日运势为：" + "\n" +
               result.fortune_summary + "\n" +
               result.lucky_star + "\n" +
               "签文：" + result.sign_text + "\n" +
               "————————————" + "\n" +
               "解签：" + result.un_sign_text)

    msg = Message([
        MessageSegment.file_image(Path(local_image_path)),
        MessageSegment.text(content),
    ])
    await fortune_by_sqlite.finish(msg)
