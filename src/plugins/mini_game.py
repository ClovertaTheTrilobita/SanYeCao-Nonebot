import random
from pathlib import Path
from nonebot.params import CommandArg
from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.matcher import Matcher
from nonebot.internal.params import ArgPlainText
from nonebot.adapters.qq import MessageSegment, Message
from src.clover_image.color_sensitive_game import game_flow,check_guess
from src.configs.path_config import temp_path
from src.clover_image.delete_file import delete_file

color_sensitive_game = on_command("绝对色感", rule=to_me(), priority=10)
@color_sensitive_game.handle()
async def handle_function(matcher: Matcher, args: Message = CommandArg()):
    level = args.extract_plain_text().replace("/绝对色感","").strip(" ")

    if level not in ["初级","中级","高级","超神"]:
        await color_sensitive_game.finish("请输入正确的参数, \n 如:/绝对色感  初级、中级、高级、超神")

    file_path = temp_path + str(random.randint(0, 10000)) + ".jpeg"
    result_list = await game_flow(level_decision = level,file_path = file_path)
    await color_sensitive_game.send(MessageSegment.file_image(Path(result_list[0])))
    matcher.state["result_list"] = result_list
    matcher.set_arg("guess", args)
    await delete_file(file_path)

@color_sensitive_game.got("guess", prompt="请输入坐标")
async def got_location(matcher: Matcher,guess: str = ArgPlainText()):
    result_list = matcher.state.get("result_list")
    target_row = result_list[1] # x
    target_col = result_list[2] # y
    boolean, msg = await check_guess(guess, target_row, target_col)
    if boolean :
        await color_sensitive_game.finish(msg)
    await color_sensitive_game.reject(msg)