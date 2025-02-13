from pathlib import Path
from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.qq import Message, MessageEvent, MessageSegment
from src.clover_sqlite.models.touch import QrTouch, QrTouchLog
from src.clover_image.qq_image import download_qq_image_by_account, qq_image_delete
from src.clover_image.rua import rua

to = on_command("摸摸头", rule=to_me(), priority=10, block=True)
@to.handle()
async def handle_touch(message: MessageEvent):
    member_openid = message.get_user_id()
    num = await QrTouchLog.touch_count(member_openid)
    if num > 10:
        await to.finish("你今天已经摸了太多次了，请明天再吧！")
    q = QrTouch()
    q.touch_status = 1
    if num > 5:
        result = await QrTouch.touch(1)
    else:
        result = await QrTouch.touch(0)
    q.reply_touch_content = result.reply_touch_content
    await QrTouchLog.insert_touch_log(q, member_openid)
    local_gif = rua(download_qq_image_by_account(None)).add_gif()
    msg = Message([MessageSegment.file_image(Path(local_gif)),
                  MessageSegment.text(result.reply_touch_content),])
    qq_image_delete()
    await to.finish(msg)
