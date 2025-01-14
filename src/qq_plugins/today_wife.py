from pathlib import Path
from nonebot.adapters.qq import Message, MessageEvent
from nonebot.adapters.qq import  MessageSegment
from nonebot.plugin import on_command
from nonebot.rule import to_me
from src.image.get_image import  download_qq_image,qq_image_delete

today_group_wife = on_command("群老婆", rule=to_me(), priority=10, block=True)
@today_group_wife.handle()
async def handle_function(message: MessageEvent):
      member_openid = message.get_user_id()

      local_image_path = download_qq_image(member_openid)
      msg = Message([
            MessageSegment.file_image(Path(local_image_path)),
            MessageSegment.text("@" + member_openid),
        ])

      qq_image_delete()
      await today_group_wife.finish(msg)


today_wife = on_command("今日老婆", rule=to_me(), priority=10, block=True)
@today_wife.handle()
async def handle_function(message: MessageEvent):
      member_openid = message.get_user_id()

      local_image_path = download_qq_image(member_openid)
      msg = Message([
            MessageSegment.file_image(Path(local_image_path)),
        ])

      qq_image_delete()
      await today_wife.finish(msg)


