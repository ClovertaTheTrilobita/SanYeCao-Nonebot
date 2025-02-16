from pathlib import Path
from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.qq import  MessageSegment,MessageEvent
from src.clover_yuc_wiki.yuc_wiki import get_yuc_wiki



yuc_wiki = on_command("本季新番",aliases={'新番观察'} ,rule=to_me(), priority=10, block=True)
@yuc_wiki.handle()
async def handle_function(message: MessageEvent):
    keyword = message.get_plaintext().replace("/", "").strip(" ")
    yuc_wiki_image = await get_yuc_wiki(keyword)
    await yuc_wiki.finish(MessageSegment.file_image(Path(yuc_wiki_image)))
