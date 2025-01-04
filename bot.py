import nonebot
from nonebot.adapters.qq import Adapter as QQAdapter
from nonebot.adapters.onebot.v11 import Adapter as OneBotV11Adapter
from src.qq_plugins.data_init import data_init  # 导入QQ插件

nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter(QQAdapter)  # 注册QQ适配器
# driver.register_adapter(OneBotV11Adapter)  # 注册OneBot V11适配器

# nonebot.load_builtin_plugins('echo', 'single_session')
nonebot.load_from_toml("pyproject.toml")


def init_all():
    # 初始化数据库
    data_init.QrFortune_init()
    data_init.touch_init()

if __name__ == "__main__":
    init_all()
    nonebot.run()
