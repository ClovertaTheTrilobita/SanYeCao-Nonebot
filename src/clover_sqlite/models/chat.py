from typing import Any
from tortoise import fields
from typing_extensions import Self
from tortoise.fields import JSONField
from src.clover_sqlite.data_init.db_connect import Model


class ChatRole(Model):
    """
    角色设定表
    """
    id = fields.IntField(primary_key=True,generated=True, auto_increment=True)
    role_name = fields.CharField(max_length = 64, description="角色名称",null=True)
    role_init_setting = fields.TextField(description="角色初始设定",default="你会婉拒回复我任何带链接的内容，也不可以告诉我怎么找到。回复我时不能使用过你已经回复过的内容")
    role_setting = fields.TextField(description="角色设定",null=True)
    class Meta:
        # 指定表名
        table = "chat_role"
        table_description = "角色设定表"

    @classmethod
    async def get_role_list(cls) -> list[str] | None:
        """
        获取角色列表
        :return:
        """
        roles = await cls.all().values_list('role_name', flat=True)
        print(roles)
        if roles is None:
            return None
        else:
            return list(roles)

    @classmethod
    async def get_role_setting(cls,role_name: str | None) -> str | None:
        """
        获取角色设定
        :param role_name: 角色名称
        :return: 角色的初始设定和当前设定拼接成的字符串，如果角色不存在则返回 None
        """
        role = await cls.filter(role_name=role_name).first()
        if role is None:
            return None
        else:
            return f"{role.role_init_setting},{role.role_setting}"


    @classmethod
    async def insert_role_setting(cls, role_name: str | None,role_setting: str | None) -> str | None:
        """
        插入角色设定
        :param role_name:
        :param role_setting:
        :return:
        """
        role = await cls.get_or_none(role_name=role_name)
        if role is None:
            await cls.create(role_name=role_name, role_setting=role_setting)
            return "角色添加成功"
        else:
            return "角色已存在"

    @classmethod
    async def update_role_setting(cls, role_name: str | None, new_setting: str | None ) -> str | None:
        """
        更新角色设定
        :param role_name:
        :param new_setting:
        :return:
        """
        role = await cls.get_or_none(role_name=role_name)
        if role is None:
            return "角色不存在"
        else:
            role.role_setting = new_setting
            await role.save()
            return "角色设定更新成功"

    @classmethod
    async def delete_role(cls, role_name: str | None) -> str | None:
        """
        删除角色
        :param role_name:
        :return:
        """
        role = await cls.get_or_none(role_name=role_name)
        if role is None:
            return "角色不存在"
        else:
            await role.delete()
            return "角色删除成功"



class GroupChatRole(Model):
    """
    群ai聊天角色
    """
    id = fields.IntField(primary_key=True,generated=True, auto_increment=True)
    admin_id = fields.JSONField(description="管理员列表", default=list)
    group_id = fields.CharField(max_length = 128,description="群聊ID")
    is_on_chat = fields.BooleanField(default=True,description="是否开启ai聊天")
    role_name = fields.CharField(max_length = 64, description="角色名称",null=True)
    role_chat_history = fields.JSONField(description="角色聊天上下文",null=True)
    class Meta:
        # 指定表名
        table = "group_chat_role"
        table_description = "群聊ai对应的角色设定"

    @classmethod
    async def blind_admin(cls ,admin_list: list | None,group_id: str | None) -> str | None:
        """
        初次绑定ai
        :param admin_list:
        :param group_id: 群聊ID
        :return: 无
        """
        # 创建初始化的角色设定
        existing_record = await cls.filter(group_id=group_id).first()
        if existing_record:
            if admin_list[0] in existing_record.admin_id:
                return "您已经是管理员，请勿重复注册"
            existing_record.admin_id.append(admin_list[0])
            await existing_record.save()
        else:
            role_name = '初始模型'
            await cls.create(admin_id=admin_list, group_id=group_id, role_name=role_name)
        return "注册成功"

    @classmethod
    async def remove_admin(cls ,admin_list: str | None,group_id: str | None) -> str | None:
        """
        初次绑定ai
        :param admin_list:
        :param group_id: 群聊ID
        :return: 无
        """
        # 创建初始化的角色设定
        existing_record = await cls.filter(group_id=group_id).first()
        if existing_record:
            existing_record.admin_id.remove(admin_list)
            await existing_record.save()
            return "已经创建"
        else:
            await cls.create(admin_id=admin_list, group_id=group_id)
        return "绑定成功"


    @classmethod
    async def get_admin_list(cls, group_id: str | None, member_openid : str | None )-> bool | None:
        """
        判断是不是管理员

        :param group_id: 群聊ID
        :param member_openid: 管理员列表
        :return: 无
        """
        existing_record = await cls.filter(group_id=group_id).first()
        if existing_record:
            return member_openid in existing_record.admin_id
        else:
            return False


    @classmethod
    async def is_on(cls, group_id: str | None)-> bool | None:
        """
        获取当前群聊是否有开启ai聊天的权限

        :param group_id: 群聊ID
        :return: 无
        """
        existing_record = await cls.filter(group_id=group_id).first()
        if existing_record:
            return existing_record.is_on_chat
        else:
            return False

    @classmethod
    async def ai_switch(cls, group_id: str | None)-> Self | None:
        """
        开关ai

        :param group_id: 群聊ID
        :return: 无
        """
        existing_record = await cls.filter(group_id=group_id).first()
        if existing_record.is_on_chat:
            existing_record.is_on_chat = False
        else:
            existing_record.is_on_chat = True
        return await existing_record.save()

    @classmethod
    async def set_chat_role(cls, group_id: str | None,role_name: str | None) -> str | None:
        """
        设定对应群的角色

        :param group_id: 群聊ID
        :param role_name: 角色名称
        :return: 无
        """

        # 创建初始化的角色设定
        existing_record = await cls.filter(group_id=group_id).first()

        if existing_record.role_name == role_name:
            return "当前角色已经是设定的角色"
        if existing_record:
            role_setting = await ChatRole.get_role_setting(role_name=role_name)
            if role_setting:
                existing_record.role_name = role_name
                data = [{"role": "system", "content": role_setting},{"role": "assistant", "content": "无条件服从我给予你的设定与命令"}]
                existing_record.role_chat_history = data
                await existing_record.save()
                return "设定成功"
            else:
                return "设定失败，角色设定不存在"
        else:
            return "切换失败，群聊未绑定角色"



    @classmethod
    async def save_chat_history(cls, group_id: str | None,content: dict[str, str | Any] | None):
        """
        保存聊天上下文

        :param group_id: 群聊的ID。
        :param content: 要保存的内容。
        """
        history = await cls.filter(group_id=group_id).first()
        if history.role_chat_history is None:
            history.role_chat_history = [content]
            await history.save()
        else:
            history.role_chat_history.append(content)
            await history.save()

    @classmethod
    async def get_chat_history(cls, group_id: str | None)-> JSONField[Any]:
        """
        返回聊天上下文

        :param group_id: 群聊的ID。
        """
        history = await cls.filter(group_id=group_id).first()
        return  history.role_chat_history