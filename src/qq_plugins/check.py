import os
import yaml
import random
from nonebot import  on_message
from nonebot.rule import Rule, to_me
from nonebot.plugin import on_command, on_keyword
from nonebot.adapters.qq import Message, MessageEvent
from nonebot.adapters import Bot, Event
from src.ai_chat import ai_chat
from src.ai_chat.chat_history import init_character_setting
from src.my_sqlite.admin_manage_by_sqlite import insert_administrator, check_admin_access

"""
设置管理员鉴权密码
"""
admin_passwd = "1234"

menu = ['/今日运势','/天气','/图','/点歌','/摸摸头','/群老婆','/今日老婆', '/待办', '/test', '/初始化聊天',
        '我喜欢你', "❤", "/待办查询", "/新建待办", "/删除待办", "/activate_ai", "/cf", "/管理员确认"]
async def check_value_in_menu(event: Event) -> bool:
    value = event.get_plaintext().strip().split(" ")
    if value[0] in menu:
        return False
    else:
        return True


def change_chatai_yaml_availability_to(is_available):
    with open(os.getcwd() + '/src/ai_chat/config/chat_ai.yaml', 'r', encoding='utf-8') as f1:
        dic_temp = yaml.load(f1, Loader=yaml.FullLoader)
        dic_temp['chat_ai']['active'] = is_available
    with open(os.getcwd() + '/src/ai_chat/config/chat_ai.yaml', 'w', encoding='utf-8') as f1:
        yaml.dump(dic_temp, f1)
        print(dic_temp)
        f1.close()

def is_ai():
    with open(os.getcwd() + '/src/ai_chat/config/chat_ai.yaml', 'r', encoding='utf-8') as f:
        state = yaml.load(f.read(), Loader=yaml.FullLoader).get('chat_ai').get('active')
    return state


rule = Rule(check_value_in_menu)


check = on_message(rule=to_me() & rule ,block=True)
@check.handle()
async def check(bot: Bot, event: Event):
    if is_ai():
        msg = ai_chat.deepseek_chat(event.get_plaintext())
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

character_setting_init = on_command("初始化聊天", rule=to_me(), priority=10, block=True)
@character_setting_init.handle()
async def chat_init():
    init_character_setting()
    await character_setting_init.finish("角色初始化聊天成功。")


love = on_keyword({"我喜欢你", "❤"}, rule=to_me(), priority=10, block=True)
@love.handle()
async def spread_love():
    await love.finish("我也喜欢你。")

test = on_command("test", rule=to_me(), priority=10, block=True)
@test.handle()
async def bot_on_ready():
    await test.finish("\nBoost & Magnum, ready fight!!!")

verification = on_command("管理员确认", rule=to_me(), priority=10, block=True)
@verification.handle()
async def verify_as_administrator(message: MessageEvent):
    passwd = message.get_plaintext().replace("/管理员确认", "").strip(" ")
    if passwd == admin_passwd:
        insert_administrator(message.get_user_id())
        await verification.finish("成功注册为管理员。")
    else:
        await verification.finish("管理员鉴权失败。")

ai_is_available = on_command("activate_ai", rule=to_me(), priority=10, block=True)
@ai_is_available.handle()
async def change_ai_availability(message: MessageEvent):
    member_openid = message.get_user_id()
    result = check_admin_access(member_openid)
    if result is None:
        await ai_is_available.finish(message=Message(random.choice(text_list)))
    elif str(result).lstrip("('").rstrip("',)") == member_openid:
        if is_ai():
            change_chatai_yaml_availability_to(False)
            await ai_is_available.finish("成功关闭语言模型对话功能。")
        else:
            change_chatai_yaml_availability_to(True)
            await ai_is_available.finish("成功开启语言模型对话功能。一起来聊天吧~")

