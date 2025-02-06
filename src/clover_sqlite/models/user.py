from datetime import datetime, timedelta
import random
from tortoise import fields
from src.clover_sqlite.data_init.db_connect import Model

class UserList(Model):
    user_id = fields.CharField(max_length=64, description="用户member_openid")
    group_id = fields.CharField(max_length=64, description="用户所在群聊id")
    last_used_time = fields.DateField(auto_now_add=True, description="用户最近一次使用时间")

    class Meta:
        table = "user_list"
        table_description = "用户表"


    @classmethod
    async def get_user_id(cls, user_id: str | None, group_id: str | None, days: int = 3) -> str | None:
        """
        获取指定天数内有活动的用户ID，并随机选择一个作为伴侣ID。

        :param user_id: 用户ID
        :param group_id: 群组ID
        :param days: 最近活动天数，默认为3天
        :return: 随机选择的伴侣ID，如果没有符合条件的用户则返回None
        """
        # 检查用户是否已有伴侣
        has_wife = await Wife.has_wife(user_id=user_id, group_id=group_id)
        if has_wife:
            return has_wife

        # 获取最近指定天数内有活动的用户
        start_date = datetime.now().date() - timedelta(days=days)
        end_date = datetime.now().date()
        user_ids = await cls.filter(group_id=group_id, last_used_time__range=(start_date, end_date)) \
            .exclude(user_id=user_id).values_list("user_id", flat=True)

        if user_ids:
            wife_id = random.choice(user_ids)
            await Wife.save_wife(user_id=user_id, group_id=group_id, wife_id=wife_id)
            return wife_id
        else:
            return None

    @classmethod
    async def insert_user(cls, user_id: str | None, group_id: str | None):
        """
        插入用户数据
        :param user_id:
        :param group_id:
        :return:
        """
        user_table = await cls.filter(user_id=user_id, group_id=group_id).first()
        if user_table:
            user_table.last_used_time = datetime.now().date()
            await user_table.save()
        else:
            await cls.create(user_id=user_id,group_id=group_id,last_used_time=datetime.now().date())


class Wife(Model):
    """
    群今日老婆记录表（包含群老婆和二次元老婆）
    """
    id = fields.IntField(primary_key=True, generated=True, auto_increment=True)
    user_id = fields.CharField(max_length=64, description="用户id", null=True)
    group_id = fields.CharField(max_length=64, description="群聊id", null=True)
    wife_id = fields.CharField(max_length=64, description="对应群聊用户抽取到的id", null=True)
    wife_name = fields.CharField(max_length=64, description="名称", null=True)
    wife_description = fields.CharField(max_length=64, description="描述", null=True)
    create_time = fields.DateField(auto_now_add=True, description="创建时间", null=True)

    class Meta:
        # 指定表名
        table = "wife"
        table_description = "群今日老婆记录表"



    @classmethod
    async def has_wife(cls, user_id: str | None, group_id: str | None) -> str | None:
        """
        查询是否有今日群老婆
        :param user_id:
        :param group_id:
        :return:
        """

        wife = await cls.filter(user_id=user_id, group_id=group_id, create_time=datetime.now().date()).first()
        if wife is None:
            return None
        else:
            return wife.wife_id

    @classmethod
    async def save_wife(cls, user_id: str | None, group_id: str | None, wife_id: str | None):
        """
        保存今日群老婆
        :param user_id:
        :param group_id:
        :param wife_id:
        :return:
        """
        data = {
            "user_id":user_id,
            "group_id":group_id,
            "wife_id":wife_id,
            "create_time":datetime.now().date()
        }
        await cls.create(**data)


