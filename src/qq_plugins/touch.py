from pathlib import Path
from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.qq import  Message,MessageEvent,MessageSegment
from src.my_sqlite.touch_by_sqlite import touch_count, QrTouchLog, insert_touch_log, touch
from src.image.get_image import  download_qq_image_by_account,qq_image_delete,rua

to = on_command("摸摸头",rule=to_me(),priority=10,block=True)

@to.handle()
async def handle_touch(event: MessageEvent):

    member_openid = event.get_user_id()
    num  = touch_count(member_openid)
    q = QrTouchLog()
    q.user_id = member_openid
    if num > 10 :
        await to.finish("你今天已经摸了太多次了，请明天再吧！")
    elif num > 5:
        result = touch(1)
        q.touch_status = 1
        q.reply_touch_content = result.reply_touch_content
    else:
        result = touch(0)
        q.touch_status = 1
        q.reply_touch_content = result.reply_touch_content

    insert_touch_log(q)
    local_gif = rua(download_qq_image_by_account(None)).add_gif()
    msg = Message([
        MessageSegment.file_image(Path(local_gif)),
        MessageSegment.text(result.reply_touch_content),
    ])
    qq_image_delete()
    await to.finish(msg)


