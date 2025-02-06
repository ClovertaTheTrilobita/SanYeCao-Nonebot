from pathlib import Path
from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.qq import Message, MessageEvent, MessageSegment, exception
import urllib.parse, requests
import time
import httpx

good_news = on_command("喜报", rule=to_me(), priority=10, block=True, aliases={"悲报"})
@good_news.handle()
async def good_news_img(message: MessageEvent):
    if message.get_plaintext().startswith("/喜报"):
        content = message.get_plaintext().replace("/喜报", "").strip()
        url = "https://cdn.uuuix.com/api/v1/xbs/xb.php?"
    else:
        content = message.get_plaintext().replace("/悲报", "").strip()
        url = "https://cdn.uuuix.com/api/v1/xbs/biob.php?"

    params = {
        'msg': content
    }

    await good_news.send("图片绘制中，请稍后~\n技术支持: JianDan大佬\nwww·uuuix·com")

    query = urllib.parse.urlencode(params)
    response = requests.get(url + query).json()

    if response['code'] != 1:
        await good_news.finish("请输入 /喜(悲)报+内容 哦。")

    img_url = response['url']
    # try:
    #     await good_news.finish(MessageSegment.clover_image(img_url))
    # except BaseException:
    #     await good_news.finish("出错啦，请重试。")

    try:
        await good_news.finish(MessageSegment.image(img_url))
    except exception.ActionFailed as e:
        print("\033[32m" + str(time.strftime("%m-%d %H:%M:%S")) +
              "\033[0m [" + "\033[31;1mFAILED\033[0m" + "]" +
              "\033[31;1m nonebot.adapters.qq.exception.ActionFailed \033[0m" + str(e))
        await good_news.finish("图片发送失败，请重试。这绝对不是咱的错，绝对不是！")

