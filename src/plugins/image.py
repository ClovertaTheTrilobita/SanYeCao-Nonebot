import random
from pathlib import Path
from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.qq import  MessageSegment,MessageEvent
from src.clover_image.get_image import get_image_names,get_anosu_image
from src.clover_image.download_image import download_image
from src.clover_image.delete_file import delete_file
from src.configs.path_config import temp_path


image = on_command("图", rule=to_me(), priority=10,block=False)
@image.handle()
async def handle_function():

    local_image_path = await get_image_names()
    await image.finish(MessageSegment.file_image(Path(local_image_path)))



random_keyword_image = on_command("随机图", rule=to_me(), priority=10, block=False)
@random_keyword_image.handle()
async def handle_function(message: MessageEvent):

    values = message.get_plaintext().replace("/随机图", "").split(" ")
    keyword,is_r18,num = "",0,1

    for value in values:
        if value.isdigit():
            num = int(value)
        elif value.lower() == "r18":
            is_r18 = 1
        else:
            keyword = value
    urls = await get_anosu_image(keyword=keyword,is_r18=is_r18,num=num)
    file_paths = []
    for url in urls:
        filename = f"{message.get_user_id()}{random.randint(0, 10000)}.jpg"
        image_path = temp_path + filename
        file_paths.append(image_path)
        await download_image(url,image_path)

    try:
        for file_path in file_paths:
            try:
                await random_keyword_image.send(MessageSegment.file_image(Path(file_path)))
            except Exception as e:
                print(f"发送文件 {file_path} 时出错: {e}")
                await random_keyword_image.send("某个图被外星人抢走啦，请重试")
    finally:
        # 删除所有临时文件
        for file_path in file_paths:
            await delete_file(file_path)



# search_image = on_command("/搜图", rule=to_me(), priority=10, block=True)
# @image.handle()
# async def handle_function(message: MessageEvent):
#
#     filename = str(message.get_user_id()) + str(random.randint(0, 10000)) + ".jpg"
#     image_ptah = temp_path + filename
#
#     await download_image(message.attachments[0].url, image_ptah)
#     await image.finish(MessageSegment.file_image(Path(image_ptah)))

