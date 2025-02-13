from PIL import Image, ImageDraw,ImageFont


"""
图文合成
"""
async def add_text_to_image(image_path, output_path,content,font_path, font_size, text_color,text_position ,position):
    """
    给图片添加文字
    :param image_path: 输入图片的路径
    :param output_path: 合成后的图片名称
    :param content: 要添加的文字内容
    :param font_path: 字体文件路径
    :param font_size: 文字的字体大小
    :param text_color: 文字颜色 (255, 0, 0) "#FF0000" "red"
    :param text_position: 文字对齐方式，可选值："left", "center", "right"
    :param position: 文字位置，可选值："left", "right", "center", "top", "bottom", "top left corner", "top right corner", "bottom left corner", "bottom right corner"
    :return:
    """
    # 打开图片
    image = Image.open(image_path)
    # 创建一个可用于绘制的对象
    draw = ImageDraw.Draw(image)
    # 设置字体和字体大小
    font = ImageFont.truetype(font_path, font_size)

    wrapped_text,current_width = "",0

    # 遍历文本中的每个字符
    for char in content:
        # 获取字符的宽度
        char_width, _ = draw.textbbox((0, 0), char, font=font)[2:]
        # 如果当前行的宽度加上字符宽度超过图片指定宽度，则换行
        if current_width + char_width > image.width * 9 // 10:  # 这里是图片的十分之九
            wrapped_text += "\n"
            current_width = 0
        # 将字符添加到当前行
        wrapped_text += char
        # 更新当前行的宽度
        current_width += char_width

    # 获取换行后文本的宽度和高度
    text_width, text_height = draw.textbbox((0, 0), wrapped_text, font=font)[2:]

    # 根据位置参数计算文本的位置
    if position == "left":
        position = (0, (image.height - text_height) // 2)
    elif position == "right":
        position = (image.width - text_width, (image.height - text_height) // 2)
    elif position == "center":
        position = ((image.width - text_width) // 2, (image.height - text_height) // 2)
    elif position == "top":
        position = ((image.width - text_width) // 2, 0)
    elif position == "bottom":
        position = ((image.width - text_width) // 2, image.height - text_height)
    elif position == "top left corner":
        position = (0, 0)
    elif position == "top right corner":
        position = (image.width - text_width, 0)
    elif position == "bottom left corner":
        position = (0, image.height - text_height)
    elif position == "bottom right corner":
        position = (image.width - text_width, image.height - text_height)
    elif position == "bottom left corner 9/10":
        position = (0, image.height * 9 // 10 - text_height)

    # 在图片上绘制文本
    draw.multiline_text(position, wrapped_text, font=font, fill=text_color, align=text_position)
    # 保存合成后的图片
    image.save(output_path)
    # 关闭图片
    # image.close()