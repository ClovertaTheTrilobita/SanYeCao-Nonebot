import os
import yaml
import random
from pathlib import Path
from nonebot import  on_message
from nonebot.rule import Rule, to_me
from nonebot.plugin import on_command, on_keyword
from nonebot.adapters.qq import Message, MessageEvent, MessageSegment

from src.ai_chat import ai_chat
from src.my_sqlite.models.chat import GroupChatRole
from src.my_sqlite.models.user import UserList
import platform
import psutil
import time

menu = ['/今日运势','/今日塔罗','/图','/点歌','/摸摸头','/群老婆','/今日老婆', "/开启ai","/关闭ai","/角色列表","/添加人设", "/更新人设", "/删除人设", "/切换人设", "/管理员注册",
        '/待办', '/test','/天气','我喜欢你', "❤", "/待办查询", "/新建待办", "/删除待办" ,"/cf","/B站搜索", "/BV搜索", "/喜报", "/悲报", "/奶龙", "/repo", "/info", "/menu"]


async def check_value_in_menu(message: MessageEvent) -> bool:
    value = message.get_plaintext().strip().split(" ")
    if hasattr(message, 'group_openid'): # 是否有属性group_openid，即是否为群聊消息
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

    if hasattr(message, 'group_openid'):
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
    "是什么呢？猫猫没有识别到,喵~"+'\n'+"(๑＞ڡ＜)☆ 给个准信，别让我瞎猜",
    "是想让我干嘛呢？猫猫一头雾水，喵～" + '\n' + "(๑•̀ㅂ•́)و✧ 直接跟我说，别这么含蓄，喵～",
    "是啥意思呀？猫猫完全没搞懂，喵～" + '\n' + "(๑・.・๑)  别折腾我啦，说明白，喵~",
    "是特殊信号？猫猫听不懂，喵～" + '\n' + "(๑・̀︶・́)و 下个明确指令，喵~",
    "难道是新指令？猫猫一脸茫然，喵～" + '\n' + "(๑＞ڡ＜)☆ 说详细点，别这么隐晦，喵～",
]


love = on_keyword({"我喜欢你", "❤"}, rule=to_me(), priority=2, block=False)
@love.handle()
async def spread_love():
    await love.finish("我也喜欢你。")

test = on_command("test", rule=to_me(), priority=10, block=True)
@test.handle()
async def bot_on_ready():
    await test.finish("\nBoost & Magnum, ready fight!!!")

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

repository = on_command("repo", rule=to_me(), priority=10, block=True)
@repository.handle()
async def github_repo():

    content = "三叶草bot仓库地址\n一起来搭个机器人吧😆"
    msg = Message([
        MessageSegment.file_image(Path("src/resources/image/github_repo/SanYeCao-Nonebot3.png")),
        MessageSegment.text(content),
    ])
    await repository.finish(msg)

platform_info = on_command("info", rule=to_me(), priority=10, block=True)
@platform_info.handle()
async def get_platform_info():
    # 获取操作系统名称
    os_name = platform.system()
    os_version = platform.version()
    processor_name = platform.processor()
    processor_architecture = platform.architecture()
    python_version = platform.python_version()
    memory = psutil.virtual_memory().total
    memory_usage = psutil.virtual_memory().percent
    cpu_usage = psutil.cpu_percent()

    content = ("\n[操作系统]: " + os_name + "\n[系统版本]: " + os_version + "\n[开机时长]: " + str(format((time.time() - psutil.boot_time()) / 3600, ".1f")) + "h" +
               "\n[服务器时间]: \n" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) +
               "\n\n[CPU架构]: " + processor_architecture[0] + ", " + processor_architecture[1] +
               "\n[CPU占用]: " + str(cpu_usage) + "%" +
               "\n\n[物理内存]: " + str(format(memory / (1024 ** 3), ".1f")) + "GB" +
               "\n[内存占用]: " + str(memory_usage) + "%"
               "\n\n[Python版本]: " + python_version +
               "\n\n[Bot源码]: 请发送 /repo \n[联系我们]: cloverta@petalmail·com")
    await platform_info.finish(content)

get_menu = on_command("menu", rule=to_me(), priority=10, block=True)
@get_menu.handle()
async def send_menu_list():
    content = "\n"
    for command in menu:
        if command in ["/开启ai","/关闭ai","/角色列表","/添加人设", "/更新人设", "/删除人设", "/切换人设", "/管理员注册", '/待办', '/test', '我喜欢你', "❤", "/menu"]:
            continue
        content += command + "\n"

    await get_menu.finish(content)