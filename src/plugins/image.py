import random
from pathlib import Path
from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.qq import  MessageSegment,MessageEvent
from src.clover_image.get_image import get_image_names
from src.clover_image.download_image import download_image
from src.configs.path_config import temp_path


image = on_command("图", rule=to_me(), priority=10)
@image.handle()
async def handle_function():

    local_image_path = await get_image_names()
    await image.finish(MessageSegment.file_image(Path(local_image_path)))


image = on_command("/搜图", rule=to_me(), priority=10, block=True)
@image.handle()
async def handle_function(message: MessageEvent):

    filename = str(message.get_user_id()) + str(random.randint(0, 10000)) + ".jpg"
    image_ptah = temp_path + filename

    await download_image(message.attachments[0].url, image_ptah)
    await image.finish(MessageSegment.file_image(Path(image_ptah)))