from tortoise import fields
from typing_extensions import Self
from src.clover_sqlite.data_init.db_connect import Model


class ToDoList(Model):
    id = fields.IntField(primary_key=True, generated=True, auto_increment=True)
    user_id = fields.CharField(max_length=64, description="用户member_openid")
    content = fields.TextField()

    class Meta:
        table = "user_todo_list"
        table_description = "用户待办表"

    @classmethod
    async def _get_data(cls, user_id: str | None) -> list | None:
        """
            获取对应用户的待办
        """
        if not user_id:
            return None
        else:
            return await cls.filter(user_id=user_id).order_by("id").values_list("id", "user_id", "content")

    @classmethod
    async def get_todo_list(cls, user_id: str | None) -> Self | None:
        todo_table = await cls._get_data(user_id)
        todo_list = [row[2] for row in todo_table]
        if todo_list:
            return todo_list
        else:
            return False

    @classmethod
    async def insert_todo_list(cls, user_id: str | None, content: str | None) -> bool:

        if content.lstrip(" ") == "":
            return False
        data = {
            "user_id": user_id,
            "content": content
        }
        await cls.create(**data)
        return True

    @classmethod
    async def delete_user_todo(cls, user_id: str | None, del_line_num: int | None) -> int:
        todo_table = await cls._get_data(user_id)

        if not todo_table:
            return -1

        max_length = len(todo_table)
        if del_line_num > max_length or del_line_num < 1:
            return 1

        del_id = todo_table[del_line_num - 1][0]
        await cls.filter(id=del_id).delete()
        return 0
