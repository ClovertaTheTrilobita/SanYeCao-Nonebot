from pathlib import Path
from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.qq import Message, MessageEvent, MessageSegment, exception
import urllib.parse
import requests
import time
import httpx
from src.clover_image.add_text_to_image import add_text_to_image
from src.clover_image.delete_file import delete_file
from src.configs.path_config import font_path,good_bad,temp_path

# good_news = on_command("喜报", rule=to_me(), priority=10, block=True, aliases={"悲报"})
# @good_news.handle()
# async def good_news_img(message: MessageEvent):
#     if message.get_plaintext().startswith("/喜报"):
#         content = message.get_plaintext().replace("/喜报", "").strip()
#         url = "https://cdn.uuuix.com/api/v1/xbs/xb.php?"
#     else:
#         content = message.get_plaintext().replace("/悲报", "").strip()
#         url = "https://cdn.uuuix.com/api/v1/xbs/biob.php?"
#
#     params = {
#         'msg': content
#     }
#
#     await good_news.send("图片绘制中，请稍后~\n技术支持: JianDan大佬\nwww·uuuix·com")
#
#     query = urllib.parse.urlencode(params)
#     response = requests.get(url + query).json()
#
#     if response['code'] != 1:
#         await good_news.finish("请输入 /喜(悲)报+内容 哦。")
#
#     img_url = response['url']
    # try:
    #     await good_news.finish(MessageSegment.clover_image(img_url))
    # except BaseException:
    #     await good_news.finish("出错啦，请重试。")


good_news = on_command("喜报", rule=to_me(), priority=10, block=True, aliases={"悲报"})
@good_news.handle()
async def function(message: MessageEvent):
    value = message.get_plaintext().split(" ")
    filename = ""
    if len(value) < 2 or len(value) > 2:
        await good_news.finish("请输入 正确的格式哦~ /喜报+内容 或者 /悲报+内容")
    keyword, content = value[0], value[1]
    if value[1] == "":
        await good_news.finish("请输入 正确的格式哦~ /喜报+内容 或者 /悲报+内容")
    if keyword == "/喜报":
        filename = "good_news.png"
        await add_text_to_image(image_path=good_bad + filename, output_path=temp_path + filename, content=content,
                                font_path=font_path + "微软雅黑.ttc", font_size=72, text_color=(255, 0, 0),text_position="center",
                                position="center")
        await good_news.finish(MessageSegment.file_image(Path(temp_path + filename)))
    elif keyword == "/悲报":
        filename = "bad_news.png"
        await add_text_to_image(image_path=good_bad + filename, output_path=temp_path + filename, content=content,
                                font_path=font_path + "微软雅黑.ttc", font_size=72, text_color=(128, 128, 128),text_position="center",
                                position="center")
        await good_news.finish(MessageSegment.file_image(Path(temp_path+filename)))
    await delete_file(temp_path + filename)