from nonebot.rule import to_me
from pathlib import Path
from nonebot.plugin import on_command
from nonebot.adapters.qq import  MessageSegment
from src.common_plugins.img.get_image import get_image_names

image = on_command("图", rule=to_me(), aliases={"图图", "美图"}, priority=10, block=True)

@image.handle()
async def handle_function():
    local_image_path = get_image_names()
    await image.finish(MessageSegment.file_image(Path(local_image_path)))
