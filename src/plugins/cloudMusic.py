import pickle
import time
from pathlib import Path
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.qq import   MessageSegment,MessageEvent
from src.clover_music.cloud_music.cloud_music import *

music = on_command("点歌", rule=to_me(), priority=10, block=True)
@music.handle()
async def handle_function(msg: MessageEvent):
    keyword = msg.get_plaintext().replace("/点歌", "").strip(" ")

    if keyword == "":
        await music.finish("\n请输入“/点歌+歌曲名”喔🎶")

    #获取登录信息 可以获取更换高音质
    session = requests.session()
    if not os.path.exists('cloud_music_cookies.cookie'):
        with open('cloud_music_cookies.cookie', 'wb') as f:
            pickle.dump(session.cookies, f)
    # 读取 cookie
    session.cookies = pickle.load(open('cloud_music_cookies.cookie', 'rb'))
    session, status = netease_cloud_music_is_login(session)
    if not status:
        await music.send("登录失效，请联系管理员进行登录")
        unikey = get_qr_key(session)
        path = create_qr_code(unikey)

        """是否要发送到QQ上面登录 """
        # await clover_music.send(MessageSegment.file_image(Path(path)))
        """是否要发送到QQ上面登录 """

        while True:
            code = check_qr_code(unikey, session)
            if '801' in str(code):
                print('二维码未失效，请扫码！')
            elif '802' in str(code):
                print('已扫码，请确认！')
            elif '803' in str(code):
                print('已确认，登入成功！')
                break
            else:
                print('其他：', code)
            time.sleep(2)
    with open('cloud_music_cookies.cookie', 'wb') as f:
        pickle.dump(session.cookies, f)

    #搜索歌曲
    song_id,song_name,singer,song_url = netease_music_search(keyword,session)
    song_name = str(song_name).replace(".", "·").replace("/", "、")
    if song_id is None:
        await music.finish("\n没有找到歌曲，或检索到的歌曲均为付费喔qwq\n这绝对不是我的错，绝对不是！")
    else:
        await music.send(MessageSegment.text(f" 来源：网易云音乐\n歌曲：{song_name} - {singer}\n请稍等喔🎵"))
        #返回转换后的歌曲路径
        output_silk_path = netease_music_download(song_id, song_name, singer,session)

        if output_silk_path == -1:
            await music.send("歌曲音频获取失败：登录信息失效。")
        elif output_silk_path is None:
            await music.send("歌曲音频获取失败了Σヽ(ﾟД ﾟ; )ﾉ，请重试。")
        else:
            await music.send(MessageSegment.file_audio(Path(output_silk_path)))

        #删除临时文件
        netease_music_delete()
        await music.finish()




