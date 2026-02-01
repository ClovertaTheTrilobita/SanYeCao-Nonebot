from pathlib import Path
from datetime import datetime
from nonebot.rule import to_me
from src.clover_splatoon.splatoon_data import weapons,stage,subweapons,specials, friend_list,stage3,weapons3
from nonebot import on_command
import src.plugins.utils.network as network
from src.configs.api_config import splatoon3_api
from nonebot.adapters.qq import MessageEvent, Bot, ActionFailed, Message, Event
from nonebot.adapters.qq import MessageSegment
from src.clover_splatoon.stages import RegularScheduleItem, BankaraScheduleItem, CoopScheduleItem
from src.configs.path_config import splatoon_path, temp_path
from src.clover_splatoon.html_to_image import generate_splatoon_report_image

stages11 = on_command("Splatoon地图", aliases={"splatoon地图", "喷喷地图"},rule=to_me(), priority=10, block=True)
@stages11.handle()
async def stage_handle():
    await stages11.send("正在专门为超鱿型的您整理比赛场地！\n请稍等哦～ᔦꙬᔨ")

    response = await network.fetch_json(splatoon3_api)
    data = response["data"]
    regular_schedule = data["regularSchedules"]["nodes"]
    bankara_schedule = data["bankaraSchedules"]["nodes"]
    coop_schedule = data["coopGroupingSchedule"]["regularSchedules"]["nodes"]

    regular_match_now = RegularScheduleItem.from_dict(regular_schedule[0])
    bankara_match_now = BankaraScheduleItem.from_dict(bankara_schedule[0])
    coop_match_now = CoopScheduleItem.from_dict(coop_schedule[0])

    await stages11.finish(MessageSegment.file_image(await generate_splatoon_report_image(regular_match_now, bankara_match_now, coop_match_now)))

