
from nonebot.rule import Rule, to_me
from nonebot.adapters.qq import Message, MessageEvent, MessageSegment
from nonebot import  on_message
from nonebot.adapters import Bot, Event

menu = ['/今日运势','/天气','/美图','/点歌','/摸摸','/今日老婆']
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
    await bot.send(message=Message("是什么呢？猫猫没有识别到,喵~"+'\n'+"(๑＞ڡ＜)☆ 请注意命令后要加空格哦~"),event=event)



