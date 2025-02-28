from nonebot.adapters.qq import MessageEvent
from nonebot.plugin import on_command
from nonebot.rule import to_me
from src.clover_sqlite.models.to_do import ToDoList

get_todo_list = on_command("待办查询", rule=to_me(), priority=10, aliases={"代办", "daiban"})
@get_todo_list.handle()
async def show_todo_list(message: MessageEvent):
    """
    查询用户所有的待办

    :param message:
    :return:
    """
    member_openid = message.get_user_id()
    result = await ToDoList.get_todo_list(member_openid)
    if not result:
        await get_todo_list.finish("\n您还未创建待办\n快使用 /新建待办 创建一份吧")

    todo_list = "\n\n".join([f"{i + 1}. {content}" for i, content in enumerate(result)])
    await get_todo_list.finish(f"您的待办有如下哦：⭐\n\n{todo_list}")


insert_todo = on_command("新建待办", rule=to_me(), priority=10)
@insert_todo.handle()
async def insert_todo_list(message: MessageEvent):
    member_openid = message.get_user_id()
    content = message.get_plaintext().replace("/新建待办", "").strip(" ")
    success = await ToDoList.insert_todo_list(member_openid, content)
    if success:
        await insert_todo.finish("成功添加待办，今后也要加油哦(ง •_•)ง")
    else:
        await insert_todo.finish("\n请输入 /新建待办+待办内容 哦")


delete_todo = on_command("删除待办", rule=to_me(), priority=10)
@delete_todo.handle()
async def del_todo(message: MessageEvent):
    member_openid = message.get_user_id()
    del_line_str = message.get_plaintext().replace("/删除待办", "").strip(" ")
    try:
        del_line_num = int(del_line_str)
    except BaseException:
        await delete_todo.finish("请检查您的输入是否正确。\n请输入 /删除待办+数字 哦。")
    result = await ToDoList.delete_user_todo(member_openid, del_line_num)
    if result == -1:
        await delete_todo.finish("您还未创建过待办哦。")
    elif result == 0:
        await delete_todo.finish("成功删除第" + str(del_line_num) + "条待办。")
    elif result == 1:
        await delete_todo.finish("没有找到这条待办哦，请检查您的输入是否正确.")
