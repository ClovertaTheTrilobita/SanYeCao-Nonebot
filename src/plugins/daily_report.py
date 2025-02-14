from datetime import datetime
from pathlib import Path
from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.qq import  MessageSegment
from src.clover_report.data_source import Report
from src.configs.path_config import daily_news_path


daily_report = on_command("日报", rule=to_me(), priority=10, block=True)
@daily_report.handle()
async def handle_function():
    await Report.get_report_image()
    now = datetime.now().date()
    await daily_report.finish(MessageSegment.file_image(Path(daily_news_path+f"{now}.png")))
