from nonebot.plugin import on_command, on_keyword
import random
from nonebot.rule import Rule, to_me
from nonebot import  on_message
from nonebot.adapters.qq import Message
from nonebot.adapters import Bot, Event
from src.ai_chat import ai_chat
import os
import yaml

menu = ['/今日运势','/天气','/图','/点歌','/摸摸头','/群老婆','/今日老婆', '/待办', '/test', '我喜欢你', "❤", "/待办查询", "/新建待办", "/删除待办", "/openai"]
async def check_value_in_menu(event: Event) -> bool:
    value = event.get_plaintext().strip().split(" ")
    if value[0] in menu:
        return False
    else:
        return True

rule = Rule(check_value_in_menu)
with open(os.getcwd() +'/src/ai_chat/config/chat_ai.yaml', 'r', encoding='utf-8') as f:
    is_ai = yaml.load(f.read(), Loader=yaml.FullLoader).get('chat_ai').get('active')

check = on_message(rule=to_me() & rule ,block=True)
@check.handle()
async def check(bot: Bot, event: Event):
    print(event.get_plaintext())
    msg = ai_chat.gpt(event.get_plaintext())
    print(msg)
    if is_ai == "True":
        await bot.send(message=msg,event=event)
    else:
        await bot.send(message=Message(random.choice(text_list)),event=event)

text_list = [
    "是什么呢？猫猫没有识别到,喵~"+'\n'+"(๑＞ڡ＜)☆ 给个准信，别让我瞎猜",
    "是想让我干嘛呢？猫猫一头雾水，喵～" + '\n' + "(๑•̀ㅂ•́)و✧ 直接跟我说，别这么含蓄，喵～",
    "是啥意思呀？猫猫完全没搞懂，喵～" + '\n' + "(๑・.・๑)  别折腾我啦，说明白，喵~",
    "是特殊信号？猫猫听不懂，喵～" + '\n' + "(๑・̀︶・́)و 下个明确指令，喵~",
    "难道是新指令？猫猫一脸茫然，喵～" + '\n' + "(๑＞ڡ＜)☆ 说详细点，别这么隐晦，喵～",
]

love = on_keyword({"我喜欢你", "❤"}, rule=to_me(), priority=10, block=True)
@love.handle()
async def spread_love():
    await love.finish("我也喜欢你。")

test = on_command("test", rule=to_me(), priority=10, block=True)
@test.handle()
async def bot_on_ready():
    await test.finish("\nBoost & Magnum, ready fight!!!")


