import random
from nonebot.rule import Rule, to_me
from nonebot import  on_message
from nonebot.adapters.qq import Message
from nonebot.adapters import Bot, Event

menu = ['/今日运势','/天气','/图','/点歌','/摸摸头','/群老婆','/今日老婆']
async def check_value_in_menu(event: Event) -> bool:
    value = event.get_plaintext().strip().split(" ")
    if value[0] in menu:
        return False
    else:
        return True

rule = Rule(check_value_in_menu)

check = on_message(rule=to_me() & rule ,block=True)
@check.handle()
async def check(bot: Bot, event: Event):
    await bot.send(message=Message(random.choice(text_list)),event=event)

text_list = [
    "是什么呢？猫猫没有识别到,喵~"+'\n'+"(๑＞ڡ＜)☆ 给个准信，别让我瞎猜",
    "是想让我干嘛呢？猫猫一头雾水，喵～" + '\n' + "(๑•̀ㅂ•́)و✧ 直接跟我说，别这么含蓄，喵～",
    "是啥意思呀？猫猫完全没搞懂，喵～" + '\n' + "(๑・.・๑)  别折腾我啦，说明白，喵~",
    "是特殊信号？猫猫听不懂，喵～" + '\n' + "(๑・̀︶・́)و 下个明确指令，喵~",
    "难道是新指令？猫猫一脸茫然，喵～" + '\n' + "(๑＞ڡ＜)☆ 说详细点，别这么隐晦，喵～",
]