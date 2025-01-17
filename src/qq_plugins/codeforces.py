import requests
from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.qq import Message, MessageEvent, MessageSegment

cf_query = on_command("cf", rule=to_me(), priority=10, block=True)
@cf_query.handle()
async def get_cf_rounds():
    result = requests.get('https://codeforces.com/api/contest.list?gym=false').json()
    print("正在请求codefoeces比赛API")
    i = False
    all_matches = ""
    for matches in result['result']:
        if i:
            break
        if matches["phase"] == "BEFORE":
            phase = "未开始"
        elif matches["phase"] == "FINISHED":
            phase = "已结束"
        elif matches["phase"] == "CODING":
            phase = "进行中"
        elif matches["phase"] == "PENDING_SYSTEM_TEST":
            phase = "等待判题"
        elif matches["phase"] == "SYSTEM_TEST":
            phase = "判题中"
        elif matches["phase"] == "FINISHED":
            phase = "已结束"
        else:
            phase = "未知"
        one_match = ("\n比赛：" + str(matches["name"]) +
                     "\n状态：" + phase +
                     "\n时长：" + str(int(matches["durationSeconds"]) / 3600) + "h\n")
        all_matches = "".join([all_matches, one_match])

        if phase == "未开始":
            until_start_time_min = 0 - int(matches["relativeTimeSeconds"]) / 60
            if until_start_time_min <= 180:
                until_start = "距开始：" + str(int(until_start_time_min)) + "min\n"
            elif 180 < until_start_time_min <= 1440:
                until_start = "距开始：" + str(int(until_start_time_min / 60)) + "h\n"
            elif until_start_time_min > 1440:
                until_start = "距开始：" + str(int(until_start_time_min / 60 / 24)) + "days\n"
            else:
                until_start = "距开始：未知\n"
            all_matches = "".join([all_matches, until_start])
        if matches["phase"] == "FINISHED":
            i = True
    print(all_matches)
    await cf_query.finish(all_matches)
