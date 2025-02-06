
from pydantic import BaseModel


class BotSetting(BaseModel):
    """"
    Bot 配置
    """
    #数据库链接
    db_url: str = "sqlite://./chat_bot.db"
    # 超级用户
    platform_superusers = {"QQ": [""]}
    #官bot id:账号id
    bot_id_data =  {"BOT_ACCOUNT":"bot1","BOT_APPID": "user1",}

    def get_bot_uid(self, bot_id: str) -> str | None:
        """获取官bot账号id

        参数:
            bot_id: 官bot id

        返回:
            str: 账号id
        """
        return self.bot_id_data.get(bot_id)

    def get_superuser(self, platform: str) -> list[str]:
        """获取超级用户

        参数:
            platform: 对应平台

        返回:
            list[str]: 超级用户id
        """
        if self.platform_superusers:
            return self.platform_superusers.get(platform, [])
        return []

    def get_sql_type(self) -> str:
        """获取数据库类型

        返回:
            str: 数据库类型, postgres, mysql, sqlite
        """
        return self.db_url.split(":", 1)[0] if self.db_url else ""

