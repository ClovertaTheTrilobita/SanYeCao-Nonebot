from datetime import datetime
from pathlib import Path
from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.qq import  MessageSegment
from src.clover_lightnovel.html_to_img import get_ln_image
from src.configs.path_config import light_novel_path


light_novel = on_command("轻小说", rule=to_me(), priority=10, block=True)
@light_novel.handle()
async def get_ln():
    await get_ln_image()
    now = datetime.now().date()
    await light_novel.finish(MessageSegment.file_image(Path(light_novel_path+f"{now}.png")))