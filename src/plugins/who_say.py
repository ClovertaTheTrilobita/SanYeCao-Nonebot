import random
from pathlib import Path
from nonebot.plugin import on_command
from nonebot.adapters.qq import  MessageEvent, MessageSegment
from src.clover_image.add_text_to_image import add_text_to_image
from src.clover_image.delete_file import delete_file
from src.configs.path_config import who_say_path,font_path,temp_path


luxun = on_command("luxun", aliases={"鲁迅说"}, rule=None)
@luxun.handle()
async def handle(message: MessageEvent):

    filename = str(message.get_user_id()) + str(random.randint(0, 10000)) + ".jpg"
    value = message.get_plaintext().split(" ")
    keyword, content = value[0], value[1]
    if len(value) < 2 or len(value) > 2 or value[1] == "":
        await luxun.finish("你让鲁迅说点啥?格式不对自己捋一捋吧~")
    if len(content) >= 24:
        await luxun.finish("太长了, 鲁迅说不完! 24字以内~")
    else:
        await add_text_to_image(image_path=who_say_path + "luxun.jpg", output_path=temp_path + filename, content="      "+content+"   —鲁迅",
                                font_path=font_path + "华文行楷.TTF", font_size=28, text_color=(255, 255, 255),text_position="left",
                                position="bottom left corner 9/10")
        await luxun.send(MessageSegment.file_image(Path(temp_path + filename)))
        await delete_file(temp_path + filename)