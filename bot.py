import nonebot
from nonebot.adapters.qq import Adapter as QQAdapter
from nonebot import logger
from nonebot.log import default_format
from apscheduler.schedulers.blocking import BlockingScheduler
from src.configs.path_config import log_path
from src.plugins.platform import clean_temp_cache

nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter(QQAdapter)  # 注册QQ适配器
nonebot.load_from_toml("pyproject.toml")
logger.add(log_path, level="ERROR", format=default_format, rotation="1 week")

from src.clover_sqlite.data_init.db_connect import disconnect, init
driver.on_startup(init)
driver.on_shutdown(disconnect)
scheduler = BlockingScheduler()
scheduler.add_job(clean_temp_cache, 'cron', hour=0, minute=0)
scheduler.start()

if __name__ == "__main__":
    nonebot.run()
