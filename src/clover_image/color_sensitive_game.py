import random
from PIL import Image, ImageDraw,ImageFont
from src.configs.path_config import font_path


async def generate_diff_color(base_color, level):
    """生成差异颜色"""
    factor = 1.1
    if level == 2:
        factor = 1.08
    elif level == 3:
        factor = 1.05
    elif level == 4:
        factor = 1.02

    new_color = [
        min(255, max(0, int(c * factor)))
        for c in base_color
    ]
    return tuple(new_color)
async def generate_base_color():
    """生成基础颜色"""
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )
async def init_game_state(level_decision):
    """初始化"""
    level = 1 if level_decision == "初级" else 2 if level_decision == "中级" else 3 if level_decision == "高级" else 4
    size = 3 if level == 1 else 5 if level == 2 else 7 if level == 3 else 9

    return {
        "level": level,
        "size": size,
        "cell_size": 50,
        "base_color": await generate_base_color(),
        "diff_color": None,
        "target_row": None,
        "target_col": None
    }

async def generate_new_level(state):
    """生成新关卡"""
    state["base_color"] = await generate_base_color()
    state["diff_color"] = await generate_diff_color(state["base_color"], state["level"])
    state["target_row"] = random.randint(0, state["size"] - 1)
    state["target_col"] = random.randint(0, state["size"] - 1)
    return state

async def create_image(state, image_path):
    """创建图片"""
    cell_size = state["cell_size"]
    image_width = (state["size"] + 1) * cell_size
    image_height = (state["size"] + 1) * cell_size

    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path+ "微软雅黑.ttc", cell_size // 2)

    for row in range(state["size"]):
        y_center = (row + 1) * cell_size + cell_size // 2
        text = str(row + 1)
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_x = cell_size // 2 - (text_bbox[2] - text_bbox[0]) // 2
        text_y = y_center - (text_bbox[3] - text_bbox[1]) // 2
        draw.text((text_x, text_y), text, fill="black", font=font)

    for col in range(state["size"]):
        x_center = (col + 1) * cell_size + cell_size // 2
        text = str(col + 1)
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_x = x_center - (text_bbox[2] - text_bbox[0]) // 2
        text_y = cell_size // 2 - (text_bbox[3] - text_bbox[1]) // 2
        draw.text((text_x, text_y), text, fill="black", font=font)

    for row in range(state["size"]):
        for col in range(state["size"]):
            x1 = (col + 1) * cell_size
            y1 = (row + 1) * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            color = state["diff_color"] if (row == state["target_row"] and col == state["target_col"]) else state["base_color"]
            draw.rectangle([x1, y1, x2, y2], fill=color)

    image.save(image_path)
    return [image_path, state["target_row"], state["target_col"]]


async def game_flow(level_decision: str, file_path: str):

    game_state = await init_game_state(level_decision)
    updated_state = await generate_new_level(game_state)
    return await create_image(updated_state, file_path)



async def check_guess(guess, target_row, target_col):
    """验证答案"""
    if guess == "#":
        return True, "游戏结束！"
    if len(guess) != 2 or not guess.isdigit():
        return False, "请输入两位数字（例如：12），输入 # 退出游戏"

    guessed_row = int(guess[0]) - 1
    guessed_col = int(guess[1]) - 1

    return (guessed_row == target_row and guessed_col == target_col), "恭喜！回答正确！" if (
                guessed_row == target_row and guessed_col == target_col) else "回答错误，请再试一次！"

