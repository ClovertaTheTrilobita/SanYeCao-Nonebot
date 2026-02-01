import yaml
from pathlib import Path
from nonebot import logger

CURRENT_FILE = Path(__file__).resolve()
ROOT_DIR = CURRENT_FILE.parent.parent.parent   # config -> src -> project root
CONFIG_PATH = ROOT_DIR / "config.yaml"

try:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
except FileNotFoundError:
    raise FileNotFoundError(f"未找到配置文件: {CONFIG_PATH}，请根据README.md，将example.config.yaml重命名为config.yaml，并正确配置机器人设置")

default_config = config['default']

if default_config == "True":
    logger.warning(f"正在使用未经配置的配置文件，若你不想看到此警告，请将 {CONFIG_PATH} 第一行的default字段改为：False")

app_id = config['bot']['app_id']
bot_account = config['bot']['bot_account']
"""
谷歌邮箱配置
"""
google_enabled = config['mail']['google']['enabled']
google_smtp_server = config['mail']['google']['smtp_server']
google_email = config['mail']['google']['email']
google_password = config['mail']['google']['password']
"""
qq 邮箱配置
"""
qq_enabled = config['mail']['qq']['enabled']
qq_smtp_server = config['mail']['qq']['smtp_server']
qq_email = config['mail']['qq']['email']
qq_password = config['mail']['qq']['password']

"""
自建邮箱配置
"""
server_enabled = config['mail']['server']['enabled']
server_smtp_server = config['mail']['server']['smtp_server']
server_email = config['mail']['server']['email']
server_password = config['mail']['server']['password']
server_port = int(config['mail']['server']['port'])

"""
图床配置
"""
# SMMS图床相关配置
smms_enabled = config['image_hosting']['smms']['enabled']
smms_token= config['image_hosting']['smms']['token']
smms_image_upload_history= config['image_hosting']['smms']['smms_image_upload_history']

# 聚合图床相关配置
ju_he_enabled = config['image_hosting']['superbed']['enabled']
ju_he_token= config['image_hosting']['superbed']['token']
ju_he_image_list= config['image_hosting']['superbed']['superbed_image_list']

#随机图 anosu
anosu_url = config['image_hosting']['random_pic']

# 搜番/acg api
animetrace_url = config['image_hosting']['animetrace']['url']
"""
AI
"""
admin_password= config['ai']['admin']['password']
# 图灵机器人相关配置
v3_enabled = config['ai']['api']['v3']['enabled']
v3url= config['ai']['api']['v3']['url']
v3key= config['ai']['api']['v3']['key']
# DeepSeek相关配置
deepseek_enabled = config['ai']['api']['deepseek']['enabled']
deepseek_url= config['ai']['api']['deepseek']['url']
deepseek_key= config['ai']['api']['deepseek']['key']

#硅基流动
silicon_flow_enabled = config['ai']['api']['silicon_flow']['enabled']
silicon_flow_url = config['ai']['api']['silicon_flow']['url']
silicon_flow_key = config['ai']['api']['silicon_flow']['key']
silicon_flow_model = config['ai']['api']['silicon_flow']['model']

"""
Wenku8账号
"""
wenku8_username = config['wenku8']['user_name']
wenku8_password = config['wenku8']['password']

"""
多米HTTP代理api
"""
proxy_enabled = config['proxy']['enabled']
proxy_api = config['proxy']['key']

"""
二维码生成 API 参数
"""
qrserver_url = config['qr']['url']
qrserver_size= config['qr']['size']

"""
CodeForces API
"""
codeforces_key = config['codeforces']['key']
codeforces_secret = config['codeforces']['secret']

"""
Splatoon3 API
"""

splatoon3_api = config['splatoon']['v3']["schedules"]