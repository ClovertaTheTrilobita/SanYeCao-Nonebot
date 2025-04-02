import re
from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.qq import MessageEvent
from src.clover_jm.jm_comic import download_jm

jm = on_command("jm", rule=to_me(), priority=10,block=False)
@jm.handle()
async def handle_function(message: MessageEvent):

    values = message.get_plaintext().replace("/jm", "").split(" ")

    if 3 > len(values) > 4:
        await jm.finish("请输入正确的格式 /jm+id 或 /jm+id+邮箱号")
    else:
        if not validate_email(values[2]):
            await jm.finish("邮箱格式不正确！")

        await jm.send("正在发送中，请稍等~")
        msg = await download_jm(album_id = values[1],receiver_email = values[2])
        await jm.finish(msg)

def validate_email(email: str) -> bool:
    """验证邮箱格式是否合法"""
    EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
    return re.fullmatch(EMAIL_REGEX, email) is not None