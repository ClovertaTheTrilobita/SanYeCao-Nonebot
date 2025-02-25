# 引入sqlalchemy依赖
from pathlib import Path
from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.qq import Message, MessageEvent, MessageSegment,exception
from src.clover_image.get_image import get_image_names
from src.clover_sqlite.models.fortune import QrFortune
from src.clover_sqlite.models.tarot import TarotExtractLog
import time

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
    try:
        await fortune_by_sqlite.finish(msg)
    except exception.ActionFailed as e:
        print("\033[32m" + str(time.strftime("%m-%d %H:%M:%S")) +
              "\033[0m [" + "\033[31;1mFAILED\033[0m" + "]" +
              "\033[31;1m nonebot.adapters.qq.exception.ActionFailed \033[0m" + str(e))
        await fortune_by_sqlite.finish("您的今日运势被外星人抢走啦，请重试。这绝对不是咱的错，绝对不是！")


tarot = on_command("今日塔罗", rule=to_me(), priority=10, block=True)
@tarot.handle()
async def get_tarot(message: MessageEvent):
    #extract_type : 1大阿尔克纳牌 2小阿尔克纳牌 3 混合牌组 4三角牌阵 5六芒星牌阵 6凯尔特十字牌阵 7恋人牌阵
    value = message.get_plaintext().strip().split(" ")
    if len(value) < 2 or len(value) > 2 or value[1] == "" or value[1] not in ["1","2","3","4","5"]:
        await tarot.finish("请输入正确的指令格式：/今日塔罗 + 数字(1-5) \n"
                           "1   大阿尔克纳牌 \n"
                           "2   小阿尔克纳牌 \n"
                           "3   混合牌组 \n"
                           "4   三角牌阵 \n"
                           "5   六芒星牌阵 "
                           )
    result = await TarotExtractLog.tarotChoice(int(value[1]),message.get_user_id())
    if result.extract_type in [1,2,3]:
        content = ("\n" + result.orientation + "\n" +
                   result.name + "\n" +
                   "含义：" + result.meaning)

        msg = Message([
            MessageSegment.file_image(Path(result.image)),
            MessageSegment.text(content),
        ])
        try:
            await tarot.finish(msg)
        except exception.ActionFailed as e:
            print("\033[32m" + str(time.strftime("%m-%d %H:%M:%S")) +
                  "\033[0m [" + "\033[31;1mFAILED\033[0m" + "]" +
                  "\033[31;1m nonebot.adapters.qq.exception.ActionFailed \033[0m" + str(e))
            await tarot.finish("您的塔罗牌被未来人抢走啦，请重试。这绝对不是咱的错，绝对不是！")
    else:
        await tarot.finish(MessageSegment.file_image(Path(result.image)))
