from pathlib import Path
from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.qq import  MessageSegment,MessageEvent
from src.clover_jm.jm_comic import download_jm
from src.clover_image.delete_file import delete_file

jm = on_command("jm", rule=to_me(), priority=10,block=False)
@jm.handle()
async def handle_function(message: MessageEvent):
    key = message.get_plaintext().replace("/jm", "").strip(" ")

    output_file = await download_jm(key)
    await jm.send(MessageSegment.file_image(Path(output_file)))
    await delete_file(output_file)
