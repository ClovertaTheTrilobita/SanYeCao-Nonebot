from pathlib import Path

import nonebot
from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.qq import  MessageSegment,MessageEvent
from src.clover_yuc_wiki.yuc_wiki import get_yuc_wiki



yuc_wiki = on_command("本季新番",aliases={'下季新番','新番观察'} ,rule=to_me(), priority=10, block=True)
@yuc_wiki.handle()
async def handle_function(message: MessageEvent):
    keyword = message.get_plaintext().replace("/", "").strip(" ")
    yuc_wiki_image = await get_yuc_wiki(keyword)
    if yuc_wiki_image is None:
        await yuc_wiki.finish("暂无新番信息")
    try:
        await yuc_wiki.finish(MessageSegment.file_image(Path(yuc_wiki_image)))
    except Exception:
        await yuc_wiki.finish("新番信息被外星人抢走啦，请重试。这绝对不是咱的错，绝对不是！")
