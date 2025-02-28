# https://api.bilibili.com/x/web-interface/search/type?keyword=av28465342&search_type=video&page=1

import time
import nonebot.adapters.qq.exception
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.qq import   MessageSegment,MessageEvent, Message
import src.clover_videos.billibili.biliVideos as biliVideos
from src.configs.path_config import video_path

bili_vid = on_command("B站搜索",rule=to_me(), priority=10)
@bili_vid.handle()
async def get_bili_vid_info(message: MessageEvent):
    content = message.get_plaintext().replace("/B站搜索", "").strip()
    response = biliVideos.get_video_info(content)
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


bili_bv_search = on_command("BV搜索", rule=to_me(), priority=10)
@bili_bv_search.handle()
async def get_video_file(message: MessageEvent):
    keyword = message.get_plaintext().replace("/BV搜索", "").strip().split()
    P_num, pages, vid_title, vid_author, vid_pic = biliVideos.get_video_pages_info(keyword[0])
    if len(keyword) == 1:

        if P_num > 1:
            content = "\n标题:" + vid_title + "\nup主: " + vid_author + "\n该视频为多P播放：\n"
            for page in pages:
                content = content + "P" + str(page['page']) + ": " + page['part'] + "\n时长: " + str(page['duration']) + "s\n\n"

            content = content + "请选择您想播放的集数。\n决定好后麻烦回复 /BV搜索+BV号+序号 哦。\n"
            await bili_bv_search.finish(content)

        elif P_num == 1:

            content = ("\n标题: " + vid_title + "\nup主: " + vid_author + "\n视频加载中~请稍后~~~")
            msg = Message([
                MessageSegment.image(vid_pic),
                MessageSegment.text(content),
            ])
            await bili_bv_search.send(msg)

            cid = pages[0]['cid']
            video_url = biliVideos.get_video_file_url(keyword[0], cid)
            # biliVideos.video_download(video_url, cid)
            # biliVideos.transcode_video(f"./src/resources/videos/{cid}.mp4",f"./src/resources/videos/{cid}-o.mp4")

            try:
                # await bili_bv_search.send(Message(MessageSegment.file_video(Path(video_path + f"/{cid}-o.mp4"))))
                await bili_bv_search.send(MessageSegment.video(video_url))
            except nonebot.adapters.qq.exception.ActionFailed as e:
                print("\033[32m" + str(time.strftime("%m-%d %H:%M:%S")) +"\033[0m [" + "\033[31;1mFAILED\033[0m" + "]" + "\033[31;1m nonebot.adapters.qq.exception.ActionFailed \033[0m" + str(e))
                await bili_bv_search.finish("发送失败惹，可能是视频过长，请尽量搜索1分钟以内的视频吧。")

            # biliVideos.delete_video(cid)

    elif len(keyword) >= 2:

        try:
            page_num = int(keyword[1])
        except:
            await bili_bv_search.finish("输入有误\n请确认是否为 /BV搜索+BV号+序号(数字) ")

        if page_num > len(pages):
            page_num = len(pages)
        elif page_num < 1:
            page_num = 1

        content = ("\n标题: " + vid_title + "\nup主: " + vid_author + "\n正在播放共" + str(P_num) + "P中的第" + str(page_num) + "P" + "\n视频加载中~请稍后~~~")
        msg = Message([
            MessageSegment.image(vid_pic),
            MessageSegment.text(content),
        ])
        await bili_bv_search.send(msg)

        cid = pages[page_num - 1]['cid']
        video_url = biliVideos.get_video_file_url(keyword[0], cid)
        # biliVideos.video_download(video_url, cid)
        # biliVideos.transcode_video(VIDEO_PATH / f"{cid}.mp4", VIDEO_PATH / f"{cid}-o.mp4")

        try:
            # await bili_bv_search.send(Message(MessageSegment.file_video(Path(VIDEO_PATH / f"{cid}.mp4"))))
            await bili_bv_search.send(MessageSegment.video(video_url))
        except nonebot.adapters.qq.exception.ActionFailed as e:
            print("\033[32m" + str(time.strftime("%m-%d %H:%M:%S")) +
                  "\033[0m [" + "\033[31;1mFAILED\033[0m" + "]" +
                  "\033[31;1m nonebot.adapters.qq.exception.ActionFailed \033[0m" + str(e))
            await bili_bv_search.finish("发送失败惹，可能是视频过长，请尽量搜索1分钟以内的视频吧。")

        # biliVideos.delete_video(cid)

    await bili_bv_search.finish()
