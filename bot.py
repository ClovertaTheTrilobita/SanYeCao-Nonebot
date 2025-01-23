import nonebot
from nonebot.adapters.qq import Adapter as QQAdapter

nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter(QQAdapter)  # 注册QQ适配器
nonebot.load_from_toml("pyproject.toml")

from src.my_sqlite.data_init.db_connect import disconnect, init
driver.on_startup(init)
driver.on_shutdown(disconnect)


if __name__ == "__main__":
    nonebot.run()
