import requests
from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.adapters.qq import Message, MessageEvent, MessageSegment
from pathlib import Path
from src.configs.path_config import path

cf_query = on_command("cf", rule=to_me(), priority=10, block=True)
@cf_query.handle()
async def get_cf_rounds():
    await cf_query.send("正在为您整理近期比赛信息哦~\n请稍等💭💡🎈")
    try:
        result = requests.get('https://codeforces.com/api/contest.list?gym=false').json()
    except BaseException:
        await cf_query.finish("API请求失败，这绝对不是咱的错，绝对不是！")
    all_matches = ""
    for matches in result['result']:
        phase = get_match_phase(matches["phase"])
        one_match = ("\n比赛：" + str(matches["name"]) + "\n状态：" + phase + "\n时长：" + str(int(matches["durationSeconds"]) / 3600) +"h\n")
        all_matches = "".join([all_matches, one_match])
        if phase == "未开始":
            until_start_time_min = 0 - int(matches["relativeTimeSeconds"]) / 60
            until_start = get_until_start_time(until_start_time_min)
            all_matches = "".join([all_matches, until_start])
        if matches["phase"] == "FINISHED":
            break

    cf_image_path = path + "/image/codeforces/cfContestQR.png"
    msg = Message([
        MessageSegment.file_image(Path(cf_image_path)),
        MessageSegment.text(all_matches),
    ])

    await cf_query.finish(msg)


def get_match_phase(phase):
    phase_map = {
        "BEFORE": "未开始",
        "FINISHED": "已结束",
        "CODING": "进行中",
        "PENDING_SYSTEM_TEST": "等待判题",
        "SYSTEM_TEST": "判题中",
    }
    return phase_map.get(phase, "未知")


def get_until_start_time(until_start_time_min):
    if until_start_time_min <= 180:
        return "距开始：" + str(int(until_start_time_min)) + "min\n"
    elif 180 < until_start_time_min <= 1440:
        return "距开始：" + str(int(until_start_time_min / 60)) + "h\n"
    elif until_start_time_min > 1440:
        return "距开始：" + str(int(until_start_time_min / 60 / 24)) + "days\n"
    else:
        return "距开始：未知\n"
