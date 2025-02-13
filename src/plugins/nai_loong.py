import random
from nonebot.rule import to_me
from nonebot.plugin import on_keyword
from nonebot.adapters.qq import Message


nai_loong = on_keyword({"奶龙"}, rule=to_me(), priority=1, block=True)
@nai_loong.handle()
async def not_nai_loong():
    await nai_loong.finish(message=Message(random.choice(text_list_nailoong)))

text_list_nailoong = [
    "我是？你是？😨",
    "你才是奶龙😡",
    "你是奶龙？🤔我是奶龙？😨你才是奶龙！😱",
    "今夜星光闪闪✨️我爱你的心满满🤩",
    "唐",
]