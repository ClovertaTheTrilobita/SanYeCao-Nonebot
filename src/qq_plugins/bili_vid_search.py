# https://api.bilibili.com/x/web-interface/search/type?keyword=av28465342&search_type=video&page=1

import time
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.qq import   MessageSegment,MessageEvent, Message
import src.videos.billibili.biliVideos as biliVideos

bili_vid = on_command("B站搜索",rule=to_me(), priority=10, block=True)
@bili_vid.handle()
async def get_bili_vid_info(message: MessageEvent):
    content = message.get_plaintext().replace("/B站搜索", "").strip()
    response = biliVideos.get(content)
    if response['code'] != 0:
        bili_vid.finish(response['message'])
    search_result = response['data']['result']

    i = 0
    for vid_info in search_result:
        i += 1
        if i >= 4:
            break
        pic = "https:" + str(vid_info['pic'])
        # print(pic)
        if vid_info['description'].strip() == "":
            dis = "无"
        else:
            dis = vid_info['description']
        description = ("\n标题: " + str(vid_info['title']).replace('<em class="keyword">', "").replace('</em>', "") +
                       "\nup主: " + vid_info['author'] +
                       "\n" + vid_info['bvid'])
        msg = Message([
            MessageSegment.image(pic),
            MessageSegment.text(description),
        ])
        await bili_vid.send(msg)
        time.sleep(0.5)

    await bili_vid.finish(f"展示{len(search_result)}条结果中的前3条。")
