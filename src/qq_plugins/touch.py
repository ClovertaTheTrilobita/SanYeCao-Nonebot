from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.qq import  MessageEvent

from src.my_sqlite.touch_by_sqlite import touch_count, QrTouchLog, insert_touch_log, touch

to = on_command("摸摸头",rule=to_me(),priority=10,block=True)

@to.handle()
async def handle_touch(event: MessageEvent):

    member_openid = event.get_user_id()
    # 判断触摸次数
    if touch_count(member_openid) > 10:
        await to.finish("你已经摸了太多次了，请休息一下吧！")
    elif touch_count(member_openid) > 5:
        result = touch(1)
        # 记录触摸次数
        q = QrTouchLog()
        q.touch_status = 0
        q.reply_touch_content = result.reply_touch_content
        q.user_id = member_openid
        insert_touch_log(q)
        await to.finish(result.reply_touch_content)
    else:
        result = touch(0)
        # 记录触摸次数
        q = QrTouchLog()
        q.touch_status = 0
        q.reply_touch_content = result.reply_touch_content
        q.user_id = member_openid
        insert_touch_log(q)

        await to.finish(result.reply_touch_content)


