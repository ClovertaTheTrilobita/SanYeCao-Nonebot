import os
import yaml
import random
from nonebot import  on_message
from nonebot.rule import Rule, to_me
from nonebot.plugin import on_command, on_keyword
from nonebot.adapters.qq import Message, MessageEvent
from nonebot.adapters import Bot, Event
from src.ai_chat import ai_chat
from src.ai_chat.chat_history import relace_character_setting,character_settings
from src.my_sqlite.admin_manage_by_sqlite import *

with open(os.getcwd() + '/src/ai_chat/config/chat_ai.yaml', 'r', encoding='utf-8') as f1:
    chat = yaml.load(f1, Loader=yaml.FullLoader).get('chat_ai')
    admin_password = chat.get('admin_password')


menu = ['/今日运势','/天气','/图','/点歌','/摸摸头','/群老婆','/今日老婆', '/待办', '/test', '/切换角色',
        '我喜欢你', "❤", "/待办查询", "/新建待办", "/删除待办", "/开启ai","/关闭ai", "/cf", "/管理员确认"]
async def check_value_in_menu(event: Event) -> bool:
    value = event.get_plaintext().strip().split(" ")
    if value[0] in menu:
        return False
    else:
        return True


check = on_message(rule=to_me() & Rule(check_value_in_menu) ,block=True)
@check.handle()
async def check(bot: Bot, event: Event):
    status = select_status(event.get_session_id().split('_')[1])
    if  status.is_on:
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

replace_character = on_command("切换角色", rule=to_me(), priority=10, block=True)
@replace_character.handle()
async def function(message: MessageEvent):
    status = select_status(message.get_session_id().split('_')[1])
    if not status.is_on:
        await replace_character.finish("当前群未开启ai聊天。")
    character = message.get_plaintext().replace("/切换角色", "").strip(" ")
    if character == "":
        await replace_character.finish("请输入角色名称。")
    else:
        if character in character_settings.settings:
            relace_character_setting(character)
            await replace_character.finish("角色切换成功。")
        else:
            await replace_character.finish("角色不存在。")


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
    if passwd == admin_password:
        insert_administrator(message.get_user_id(), message.get_session_id().split('_')[1])
        await verification.finish("成功注册为管理员。")
    else:
        await verification.finish("管理员认证密码错误。")


ai_on = on_command("开启ai",aliases={'关闭ai'}, rule=to_me(), priority=10, block=True)
@ai_on.handle()
async def change_ai_availability(message: MessageEvent):

    result = check_admin_access(message.get_user_id(), message.get_session_id().split('_')[1])
    if result is None:
        await ai_on.finish("当前群无权限，请联系管理员")
    elif (not result.is_on) & (message.get_plaintext() == "/开启ai"):
        update_administrator(message.get_session_id().split('_')[1], True)
        await ai_on.finish("成功开启语言模型对话功能。一起来聊天吧~")
    elif not result.is_on :
        await ai_on.finish("当前群未开启ai聊天。")
    else:
        update_administrator(message.get_session_id().split('_')[1], False)
        await ai_on.finish("成功关闭语言模型对话功能。")
