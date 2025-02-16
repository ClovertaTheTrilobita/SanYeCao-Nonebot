import os
import random
from nonebot import  on_message
from nonebot.rule import Rule, to_me
from nonebot.plugin import on_command, on_keyword
from nonebot.adapters.qq import Message, MessageEvent
from src.clover_openai import ai_chat
from src.clover_sqlite.models.chat import GroupChatRole
from src.clover_sqlite.models.user import UserList

menu = ["/重启","/今日运势","/今日塔罗","/图","/日报","/点歌","/摸摸头","/群老婆","/今日老婆", "/开启ai","/关闭ai","/角色列表","/添加人设", "/更新人设", "/删除人设", "/切换人设", "/管理员注册",
        "/待办", "/test","/天气","我喜欢你", "❤", "/待办查询", "/新建待办", "/删除待办" ,"/cf","/B站搜索", "/BV搜索", "/喜报", "/悲报", "/luxun","/鲁迅说",
        "/奶龙", "/repo", "/info", "/menu", "/轻小说","/本季新番","/新番观察"]

send_menu = ["/开启ai","/关闭ai","/角色列表","/添加人设", "/更新人设", "/删除人设", "/切换人设", "/管理员注册", "/待办", "/test", "我喜欢你", "❤", "/menu"]

async def check_value_in_menu(message: MessageEvent) -> bool:
    value = message.get_plaintext().strip().split(" ")
    if hasattr(message, "group_openid"): # 是否有属性group_openid，即是否为群聊消息
        group_id = message.group_openid
    else:
        group_id = "C2C" # 非群聊消息，存为c2c
    #缓存用户id
    await UserList.insert_user(message.author.id,group_id)
    if value[0] in menu:
        return False
    else:
        return True


check = on_message(rule=to_me() & Rule(check_value_in_menu) ,block=True, priority=10)
@check.handle()
async def handle_function(message: MessageEvent):

    if hasattr(message, "group_openid"):
        group_openid = message.group_openid
    else:
        group_openid = "C2C"

    member_openid, content = message.author.id, message.get_plaintext()
    status = await GroupChatRole.is_on(group_openid)
    if status:
        msg = await ai_chat.deepseek_chat(group_openid,content)
        await check.finish(msg)
    else:
        await check.finish(message=Message(random.choice(text_list)))

text_list = [
    "是什么呢？猫猫没有识别到,喵~"+"\n"+"(๑＞ڡ＜)☆ 给个准信，别让我瞎猜",
    "是想让我干嘛呢？猫猫一头雾水，喵～" + "\n" + "(๑•̀ㅂ•́)و✧ 直接跟我说，别这么含蓄，喵～",
    "是啥意思呀？猫猫完全没搞懂，喵～" + "\n" + "(๑・.・๑)  别折腾我啦，说明白，喵~",
    "是特殊信号？猫猫听不懂，喵～" + "\n" + "(๑・̀︶・́)و 下个明确指令，喵~",
    "难道是新指令？猫猫一脸茫然，喵～" + "\n" + "(๑＞ڡ＜)☆ 说详细点，别这么隐晦，喵～",
]

get_menu = on_command("menu", rule=to_me(), priority=10, block=True)
@get_menu.handle()
async def send_menu_list():
    content = "\n"
    for command in send_menu:
        content += command + "\n"
    await get_menu.finish(content)

restart = on_command("重启", rule=to_me(), priority=10, block=True)
@restart.handle()
async def handle_function(message: MessageEvent):

    member_openid, group_openid = message.author.id, message.group_openid
    if not await GroupChatRole.get_admin_list(group_openid, member_openid):
        await restart.finish("您没有权限使用此功能。")

    return_code = os.system("python ./update_remote_code.py")
    if return_code == 0:
        await restart.finish("重启成功,请10s后再试。")
    else:
        await restart.finish("重启失败")

love = on_keyword({"我喜欢你", "❤"}, rule=to_me(), priority=2, block=False)
@love.handle()
async def spread_love():
    await love.finish("我也喜欢你。")

test = on_command("test", rule=to_me(), priority=10, block=True)
@test.handle()
async def bot_on_ready():
    await test.finish("\nBoost & Magnum, ready fight!!!")
