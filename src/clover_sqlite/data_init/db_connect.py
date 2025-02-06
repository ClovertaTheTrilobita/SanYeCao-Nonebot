from tortoise import Tortoise
from tortoise.connection import connections
from tortoise.models import Model as Model_

import nonebot
from nonebot.drivers import Driver

driver: Driver = nonebot.get_driver()

MODELS: list[str] = []

class Model(Model_):
    """
    自动添加模块

    Args:
        Model_: Model
    """
    def __init_subclass__(cls, **kwargs):
        MODELS.append(cls.__module__)

@driver.on_startup
async def init():
    """
        初始化数据库
    """
    await Tortoise.init(
            db_url="sqlite://chat_bot.db",
            modules={"models": MODELS},
            timezone="Asia/Shanghai",
        )
    # 生成数据库表
    await Tortoise.generate_schemas()



async def disconnect():
    """
    关闭数据库连接
    :return:
    """
    await connections.close_all()
