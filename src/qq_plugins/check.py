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

with open(os.getcwd() + '/src/ai_chat/config/chat_ai.yaml', 'r', encoding='utf-8') as f1:
    chat = yaml.load(f1, Loader=yaml.FullLoader).get('chat_ai')
    admin_password = chat.get('admin_password')


menu = ['/今日运势','/图','/点歌','/摸摸头','/群老婆','/今日老婆', "/开启ai","/关闭ai","/角色列表","/添加人设", "/更新人设", "/删除人设", "/切换人设", "/管理员注册",
        '/待办', '/test','/天气','我喜欢你', "❤", "/待办查询", "/新建待办", "/删除待办"  ,"/cf", "/奶龙", "/repo"]


async def check_value_in_menu(message: MessageEvent) -> bool:
    value = message.get_plaintext().strip().split(" ")
    #缓存用户id
    await UserList.insert_user(message.author.id,message.group_openid)
    if value[0] in menu:
        return False
    else:
        return True


check = on_message(rule=to_me() & Rule(check_value_in_menu) ,block=True, priority=10)
@check.handle()
async def handle_function(message: MessageEvent):

    member_openid, group_openid,content = message.author.id, message.group_openid,message.get_plaintext()
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


love = on_keyword({"我喜欢你", "❤"}, rule=to_me(), priority=2, block=True)
@love.handle()
async def spread_love():
    await love.finish("我也喜欢你。")

test = on_command("test", rule=to_me(), priority=10, block=True)
@test.handle()
async def bot_on_ready():
    await test.finish("\nBoost & Magnum, ready fight!!!")


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

    content = "👆三叶草bot仓库地址\n一起来搭个机器人吧😆"
    msg = Message([
        MessageSegment.file_image(Path("src/image/github_repo/SanYeCao-Nonebot.png")),
        MessageSegment.text(content),
    ])
    await repository.finish(msg)