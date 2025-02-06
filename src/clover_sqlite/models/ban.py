import time
from tortoise import fields
from typing_extensions import Self
from src.clover_sqlite.data_init.db_connect import Model

class BanConsole(Model):
    id = fields.IntField(primary_key=True, generated=True, auto_increment=True)
    user_id = fields.CharField(max_length=255,description="用户id" ,null=True)
    group_id = fields.CharField(max_length=255, description="群组id",null=True)
    ban_level = fields.IntField(description="使用ban命令的用户等级")
    ban_time = fields.BigIntField(description="ban开始的时间")
    duration = fields.BigIntField(description="ban时长")
    operator = fields.CharField(max_length=255,description="使用Ban命令的用户")

    class Meta:
        table = "ban_console"
        table_description = "封禁人员/群组数据表"


    @classmethod
    async def _get_data(cls, user_id: str | None, group_id: str | None) -> Self | None:
        """获取数据

        参数:
            user_id: 用户id
            group_id: 群组id

        异常:
            UserAndGroupIsNone: 用户id和群组id都为空

        返回:
            Self | None: Self
        """
        if not user_id and not group_id:
            print("用户id和群组id都为空")
        if user_id:
            return (
                await cls.get_or_none(user_id=user_id, group_id=group_id)
                if group_id
                else await cls.get_or_none(user_id=user_id, group_id__isnull=True)
            )
        else:
            return await cls.get_or_none(user_id="", group_id=group_id)

    @classmethod
    async def check_ban_level(
        cls, user_id: str | None, group_id: str | None, level: int
    ) -> bool:
        """检测ban掉目标的用户与unban用户的权限等级大小

        参数:
            user_id: 用户id
            group_id: 群组id
            level: 权限等级

        返回:
            bool: 权限判断，能否unban
        """
        user = await cls._get_data(user_id, group_id)
        if user:
            return user.ban_level <= level
        return False

    @classmethod
    async def check_ban_time(
        cls, user_id: str | None, group_id: str | None = None
    ) -> int:
        """检测用户被ban时长

        参数:
            user_id: 用户id

        返回:
            int: ban剩余时长，-1时为永久ban，0表示未被ban
        """
        user = await cls._get_data(user_id, group_id)
        if not user and user_id:
            user = await cls._get_data(user_id, None)
        if user:
            if user.duration == -1:
                return -1
            _time = time.time() - (user.ban_time + user.duration)
            return 0 if _time > 0 else int(time.time() - user.ban_time - user.duration)
        return 0

    @classmethod
    async def is_ban(cls, user_id: str | None, group_id: str | None = None) -> bool:
        """判断用户是否被ban

        参数:
            user_id: 用户id

        返回:
            bool: 是否被ban
        """
        if await cls.check_ban_time(user_id, group_id):
            return True
        else:
            await cls.unban(user_id, group_id)
        return False

    @classmethod
    async def ban(
        cls,
        user_id: str | None,
        group_id: str | None,
        ban_level: int,
        duration: int,
        operator: str | None = None,
    ):
        """ban掉目标用户

        参数:
            user_id: 用户id
            group_id: 群组id
            ban_level: 使用命令者的权限等级
            duration: 时长，分钟，-1时为永久
            operator: 操作者id
        """
        target = await cls._get_data(user_id, group_id)
        if target:
            await cls.unban(user_id, group_id)
        await cls.create(
            user_id=user_id,
            group_id=group_id,
            ban_level=ban_level,
            ban_time=int(time.time()),
            duration=duration,
            operator=operator or 0,
        )

    @classmethod
    async def unban(cls, user_id: str | None, group_id: str | None = None) -> bool:
        """unban用户

        参数:
            user_id: 用户id
            group_id: 群组id

        返回:
            bool: 是否被ban
        """
        user = await cls._get_data(user_id, group_id)
        if user:
            await user.delete()
            return True
        return False