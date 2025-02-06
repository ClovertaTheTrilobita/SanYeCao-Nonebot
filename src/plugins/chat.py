import re
from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.qq import MessageEvent
from src.clover_sqlite.models.chat import ChatRole, GroupChatRole
from src.configs.api_config import admin_password


t1 = on_command("管理员注册", rule=to_me(), priority=10, block=True)
@t1.handle()
async def handle_function(message: MessageEvent):
    if not hasattr(message, 'group_openid'):
        await t1.finish("暂未在当前场景下开放此功能。")

    member_openid, group_openid = message.author.id, message.group_openid
    password = message.get_plaintext().replace("/管理员注册", "").strip()
    if password == admin_password:
        result = await GroupChatRole.blind_admin([member_openid], group_openid)
        await t1.finish(result)
    else:
        await t1.finish("管理员注册密码错误。")


t3 = on_command("开启ai",aliases={"关闭ai"},rule=to_me(),priority=10,block=True)
@t3.handle()
async def handle_function(message: MessageEvent):

    if not hasattr(message, 'group_openid'):
        await t3.finish("暂未在当前场景下开放此功能。")

    member_openid, group_openid, content = message.author.id, message.group_openid, message.get_plaintext()
    # 判断是否为管理员
    if not await GroupChatRole.get_admin_list(group_openid, member_openid):
        await t3.finish("您没有权限使用此功能。")
    else:
        status = await GroupChatRole.is_on(group_openid)
        if not status and content == "/开启ai":
            await GroupChatRole.ai_switch(group_openid)
            await t3.finish("成功开启语言模型对话功能。一起来聊天吧~")
        elif status and content == "/开启ai":
            await t3.finish("当前群已开启ai聊天。请勿重复开启")
        elif status and content == "/关闭ai":
            await GroupChatRole.ai_switch(group_openid)
            await t3.finish("成功关闭语言模型对话功能。")
        elif not status and content == "/关闭ai":
            await t3.finish("当前群已关闭ai聊天,请勿重复关闭。")


tt = on_command("角色列表", rule=to_me(), priority=10, block=True)
@tt.handle()
async def handle_function(message: MessageEvent):

    if not hasattr(message, 'group_openid'):
        await tt.finish("暂未在当前场景下开放此功能。")

    member_openid, group_openid = message.author.id, message.group_openid
    if not await GroupChatRole.get_admin_list(group_openid, member_openid):
        await tt.finish("您没有权限使用此功能。")
    role_setting = await ChatRole.get_role_list()
    if (role_setting is None) | (not role_setting):
        await tt.finish("角色设定库为空，请添加角色以及设定")
    else:
        await tt.finish(str(role_setting))


t2 = on_command("添加人设",aliases={"更新人设","删除人设","切换人设"},rule=to_me(),priority=10,block=True)
@t2.handle()
async def handle_function(message: MessageEvent):

    if not hasattr(message, 'group_openid'):
        await t2.finish("暂未在当前场景下开放此功能。")

    member_openid, group_openid = message.author.id, message.group_openid
    if not await GroupChatRole.get_admin_list(group_openid, member_openid):
        await t2.finish("您没有权限使用此功能。")
    value = message.get_plaintext().strip().split(" ")
    action, role_name = value[0], value[1]
    if action == "/删除人设":
        result = await ChatRole.delete_role(role_name)
        await t2.finish(result)
    if action == "/切换人设":
        result = await GroupChatRole.set_chat_role(group_openid,role_name)
        await t2.finish(result)
    if len(value[1])>10:
        await t2.finish("角色名称过长，请重新输入")
    if len(value) < 3:
        await t2.finish("请输入角色名称和设定，格式为：命令 角色名称 角色设定")
    role_setting = re.sub(r'[\n\\n\s"‘’]', '', ''.join(value[2:]))
    if action == "/添加人设":
        result = await ChatRole.insert_role_setting(role_name, role_setting)
        await t2.finish(result)
    if action == "/更新人设":
        result = await ChatRole.update_role_setting(role_name, role_setting)
        await t2.finish(result)

