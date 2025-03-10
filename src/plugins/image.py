import random
from pathlib import Path
from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.qq import  MessageSegment,MessageEvent
from src.clover_image.get_image import get_image_names
from src.clover_image.download_image import download_image
from src.clover_image.delete_file import delete_file
from src.configs.path_config import temp_path


image = on_command("图", rule=to_me(), priority=10)
@image.handle()
async def handle_function():

    local_image_path = await get_image_names()
    await image.finish(MessageSegment.file_image(Path(local_image_path)))

random_keyword_image = on_command("随机图", rule=to_me(), priority=10, block=False)
@random_keyword_image.handle()
async def handle_function(message: MessageEvent) -> None:
    value = message.get_plaintext().split(" ")
    keyword = ""
    if len(value) == 2:
        keyword = value[1]
    if len(value) > 2:
        await random_keyword_image.finish("格式不对捏，请试一下 /随机图+关键字")

    filename = f"{message.get_user_id()}{random.randint(0, 10000)}.jpg"
    image_path = temp_path + filename

    await download_image(f"https://image.anosu.top/pixiv/direct?keyword={keyword}", image_path)

    try:
        await random_keyword_image.send(MessageSegment.file_image(Path(image_path)))
    except Exception as e:
        print(e)
        await random_keyword_image.finish("图被外星人抢走啦，请重试")

    await delete_file(image_path)


# search_image = on_command("/搜图", rule=to_me(), priority=10, block=True)
# @image.handle()
# async def handle_function(message: MessageEvent):
#
#     filename = str(message.get_user_id()) + str(random.randint(0, 10000)) + ".jpg"
#     image_ptah = temp_path + filename
#
#     await download_image(message.attachments[0].url, image_ptah)
#     await image.finish(MessageSegment.file_image(Path(image_ptah)))

