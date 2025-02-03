# 引入sqlalchemy依赖
from pathlib import Path
from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.qq import Message, MessageEvent, MessageSegment
from src.image.get_image import get_image_names
from src.my_sqlite.models.fortune import QrFortune
from src.my_sqlite.models.tarot import MajorArcana

fortune_by_sqlite = on_command("今日运势", rule=to_me(), priority=10, block=True)
@fortune_by_sqlite.handle()
async def get_today_fortune(message: MessageEvent):

    local_image_path = get_image_names()
    result = await QrFortune.get_fortune(message.get_user_id())

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


tarot = on_command("今日塔罗", rule=to_me(), priority=10, block=True)
@tarot.handle()
async def tarot(message: MessageEvent):
    result = await MajorArcana.tarotChoice(message.get_user_id())

    content = ("\n" + result.ints + "\n" +
               result.name + "\n" +
               "含义：" + result.meaning)

    msg = Message([
        MessageSegment.file_image(Path(result.image)),
        MessageSegment.text(content),
    ])
    await fortune_by_sqlite.finish(msg)
