import os
from pathlib import Path

path = os.path.join(os.getcwd(), '/src/resources')


# 塔罗牌图片路径
image_local_qq_image_path =  os.path.join(path,'/image/qq_image')
os.makedirs(image_local_qq_image_path, exist_ok=True)
# 个人图片路径
image_local_path= os.path.join(path,"/image/MaoYuNa")
os.makedirs(image_local_path, exist_ok=True)
# 塔罗牌图片路径
tarots_img_path = os.path.join(path,'/image/tarot/TarotImages/')
os.makedirs(tarots_img_path, exist_ok=True)
# 摸摸头图片路径
rua_png = os.path.join(path,'/image/rua/')
os.makedirs(rua_png, exist_ok=True)
# 喜报、悲报图片路径
good_bad = os.path.join(path,'/image/good_bad_news/')
os.makedirs(good_bad, exist_ok=True)
#谁说 生成图片路径
who_say_path = os.path.join(path,'/image/who_say/')
os.makedirs(who_say_path, exist_ok=True)
#yuc_wiki 动漫wiki
yuc_wiki_path = os.path.join(path , '/image/yuc_wiki/')
os.makedirs(yuc_wiki_path, exist_ok=True)
# 字体路径
font_path = os.path.join(path , '/font/')
os.makedirs(font_path, exist_ok=True)
# 临时数据路径
temp_path = os.path.join(path , '/temp/')
os.makedirs(temp_path, exist_ok=True)
# 日志路径
log_path = os.path.join(path,'/log/')
os.makedirs(log_path, exist_ok=True)
# 视频路径
video_path = os.path.join(path,'/video/')
os.makedirs(video_path, exist_ok=True)



# # 语音路径
# RECORD_PATH = Path() / "src" / "resources" / "record"
# # 文本路径
# TEXT_PATH = Path() / "src" / "resources" / "text"
# # 数据路径
# DATA_PATH = Path() / "src" / "data"
# # 网页模板路径
# TEMPLATE_PATH = Path() / "src" / "resources" / "template"
# # 视频路径
# VIDEO_PATH = Path() / "src" / "resources" / "videos"