import os
from PIL import Image, ImageDraw

from src.configs.path_config import image_local_qq_image_path,rua_png


""" rua 头动图生成"""
class rua():
    def __init__(self, img_file):
        self.author = Image.open(img_file)

    def add_png(self, png_d):
        # 重置图片大小
        author = self.author.resize((png_d[0], png_d[1] - png_d[2]))

        # 载入素材
        rua_p1 = Image.open(png_d[3])

        # 创建背景模板
        rua_png1 = Image.new('RGBA', (110, 110), (255, 255, 255, 255))

        # 使用预定义的参数：jd，合成一帧的样例
        rua_png1.paste(author, (110 - png_d[0], 110 - png_d[1] + png_d[2]), author)
        rua_png1.paste(rua_p1, (0, 110 - png_d[1] - png_d[2]), rua_p1)
        return rua_png1

    def add_gif(self):

        # 获取素材列表
        pst = os.listdir(rua_png)
        for i in range(len(pst)):
            pst[i] = rua_png + pst[i]

        # 预调试好的参数，传入素材列表
        jd = [[90, 90, 5, pst[0]],
              [90, 87, 5, pst[2]],
              [90, 84, 10, pst[3]],
              [90, 81, 8, pst[4]],
              [90, 78, 5, pst[5]],
              [90, 75, 5, pst[6]],
              [90, 72, 8, pst[7]],
              [90, 74, 8, pst[8]],
              [90, 77, 9, pst[9]],
              [90, 80, 8, pst[1]]]

        # 重置要生成的图片大小
        self.author = self.author.resize((90, 90))

        # 绘制模板
        alpha_layer = Image.new('L', (90, 90), 0)
        draw = ImageDraw.Draw(alpha_layer)
        draw.ellipse((0, 0, 90, 90), fill=255)
        self.author.putalpha(alpha_layer)

        # gif列表
        gifs = []
        for i in range(len(jd)):
            # 将参数传递给生成方法
            # 添加到gif列表
            gifs.append(self.add_png(jd[i]))

        # 文件名,是否保存所有,图片列表,fps/ms
        gifs[0].save(image_local_qq_image_path + '/rua.gif', "GIF", save_all=True, append_images=gifs, duration=35, loop=0)
        self.author.close()
        return image_local_qq_image_path + '/rua.gif'