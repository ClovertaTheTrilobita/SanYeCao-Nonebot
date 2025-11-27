import os
import glob
import threading
import logging

import nonebot
from pathlib import Path
from nonebot import logger
from nonebot.log import default_format
from nonebot.adapters.qq import Adapter as QQAdapter
from apscheduler.schedulers.background import BackgroundScheduler
from src.configs.path_config import log_path,temp_path,video_path,yuc_wiki_path

# 检查配置文件是否都存在，若不存在则直接退出
CURRENT_FILE = Path(__file__).resolve()
ROOT_DIR = CURRENT_FILE.parent
ENV_PROD = ROOT_DIR / ".env.prod"
CONFIG_PATH = ROOT_DIR / "config.yaml"

if not ENV_PROD.is_file():
    raise FileNotFoundError(
        f"未找到配置文件: {ENV_PROD}，请根据README.md，将example.env.prod重命名为.env.prod，并进行正确配置")

if not CONFIG_PATH.is_file():
    raise FileNotFoundError(
        f"未找到配置文件: {CONFIG_PATH}，请根据README.md，将example.config.yaml重命名为config.yaml，并配置机器人设置")


nonebot.init()

from backend import start_flask

driver = nonebot.get_driver()
driver.register_adapter(QQAdapter)  # 注册QQ适配器
nonebot.load_from_toml("pyproject.toml")
logger.add(log_path+"error.log", level="ERROR", format=default_format, rotation="1 week")

from src.clover_sqlite.data_init.db_connect import disconnect, init
driver.on_startup(init)
driver.on_shutdown(disconnect)

def clean_temp_cache():
    """定时清理缓存文件"""
    path_list =  [Path(temp_path), Path(video_path),Path(yuc_wiki_path)]
    print("开始清理文件")
    for folder_path in path_list:
        files = get_files_in_folder(folder_path)
        for file in files:
            os.remove(file)

def get_files_in_folder(folder_path: Path):
    return [Path(f) for f in glob.glob(str(folder_path / "*")) if Path(f).is_file()]

scheduler = BackgroundScheduler()
scheduler.add_job(clean_temp_cache, 'cron', hour=0, minute=0)

if __name__ == "__main__":

    flask_thread = threading.Thread(target=start_flask, daemon=True)
    flask_thread.start()
    scheduler.start()
    nonebot.run()


