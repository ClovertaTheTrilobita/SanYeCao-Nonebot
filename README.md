# SanYeCao-Nonebot

## 📚介绍

<p align="center">🌟三叶草bot 2.0🌟<br>
🚀使用Nonebot2+官方API搭建的QQ群聊机器人🚀<br><br>
<img alt="Static Badge" src="https://img.shields.io/badge/Python-3.11%2F3.12-blue">
<img alt="Static Badge" src="https://img.shields.io/badge/Nonebot-2.0-green">
<img src="https://img.shields.io/github/last-commit/ClovertaTheTrilobita/SanYeCao-Nonebot" alt="last-commit" />
<img alt="Static Badge" src="https://img.shields.io/badge/QQ%E7%BE%A4-710101225-orange"><br><br>
</p>


## 🔖亮点

- 基于[Nonebot2](https://nonebot.dev/)，使用[QQ官方API](https://bot.q.qq.com/wiki/)，更稳定、高效✨
- 多种个性化用法，如天气、每日运势(~~机器人时尚单品~~)、点歌、编辑个人待办等，后续功能开发中🔧
- 使用轻量化数据库sqlite管理数据，实现为每位用户单独存取数据🔍
- 接入第三方大语言模型，实现AI交互💡

<br>

###### 我是菜比🏳️🏳️，纯新手写的python 问题肯定多 ，若有兴趣可以帮忙一起完善功能 <br>
###### QQ交流群：[710101225](https://qm.qq.com/q/AQyepzKUJq) 

<br>

- ↑sly是代码领域大神， 👈 ClovertaTheTrilobita 写的

## 🌈目前功能:

- [x] 待办
- [x] 天气 
- [x] 今日运势
- [x] 今日塔罗
- [x] 点歌（网易云 需扫码登录 在 src\music 目录下）*目前cookie过期检测有bug,出现播放不了需要吧cookie文件删掉*
- [x] 图（返回图库中的图片）
- [x] 摸摸头
- [x] 接入语言模型
- [x] 搜索B站视频
- [ ] 今日老婆
- [x] 群老婆

<br>


## 🛠️使用

- 关于Nonebot完整部署使用方法，请查看[官方文档](https://nonebot.dev/)

<br>


### ⚙️一、环境配置

**我们强烈建议您使用虚拟环境**，若您使用Anaconda发行版，请在终端输入

```powershell
conda create --name chatbot python=3.11
```

创建conda环境。

或者将上述 *chatbot* 更换为你喜欢的名字。

<b>🚫注意：</b>机器人<b>不</b>支持<img alt="Static Badge" src="https://img.shields.io/badge/Python-3.13/+-blue">的发行版，推荐使用<img alt="Static Badge" src="https://img.shields.io/badge/Python-3.11%2F3.12-blue">

<br>

此机器人运行所需依赖已全部打包至***requirements.txt***，您只需回到项目根目录

在终端输入：

```powershell
pip install -r requirements.txt
```

安装所需依赖。

<br>

**使用网易云点歌需要另外安装：**

```powershell
npm install crypto-js
```

<br>

**使用BV搜索B站视频需要另外安装：**[<b>Chrome Driver</b>](https://googlechromelabs.github.io/chrome-for-testing/)

安装教程：[chromedriver下载与安装方法，亲测可用-CSDN博客](https://blog.csdn.net/zhoukeguai/article/details/113247342)

<br>

### ✒️二、配置所需文件

在一切开始前，你需要将项目根目录下的[<b>example.env.prod</b>](example.env.prod)文件更名为<b><i>.env.prod</i></b>，这是机器人的账号配置文件。

```
DRIVER=~fastapi+~httpx+~websockets

QQ_IS_SANDBOX=false

QQ_BOTS='
[
  {
    "id": "xxx",
    "token": "xxx",
    "secret": "xxx",
    "intent": {
      "c2c_group_at_messages": true
    },
    "use_websocket": true
  }
]
'
```
分别在id、token、secret处填写你的机器人ID，机器人Token和Apple Secret，需从[QQ开放平台](https://q.qq.com/)获取。

<br>

### 📍二、启动机器人

在项目根目录中，找到 *bot.py* ，在终端输入

```powershell
python bot.by
```

或者选择编译器启动，便可以启动机器人。

<br>

### 🗒️三、项目结构

```
SanYeCao-Nonebot:.
│  .gitignore
│  bot.py
│  chat_bot.db
│  example.env.prod
│  package-lock.json
│  package.json
│  pyproject.toml
│  README.md
│  requirements.txt
│          
├─node_modules
│  └─crypto-js
│              
└─src
    ├─clover_image
    │          
    ├─clover_music
    │  ├─cloud_music         
    │  └─netease_music
    |
    ├─clover_openai
    │          
    ├─clover_sqlite
    │  ├─data_init      
    │  └─models
    │              
    ├─clover_videos
    │  └─billibili
    │              
    ├─configs
    │  └─utils
    │          
    ├─plugins
    │  └─test
    │          
    └─resources
        ├─font
        ├─image
        │  ├─codeforces
        │  ├─github_repo
        │  ├─good_bad_news
        │  ├─MaoYuNa
        │  ├─rua
        │  ├─tarot
        │  │  ├─sideTarotImages
        │  │  └─TarotImages
        │  └─who_say
        │          
        ├─log
        ├─temp
        └─videos
```

- 基本插件存储在plugins目录中，启动即可使用
- 部分插件通过调用其它目录中的方法完成其功能

<br>

### 🎈四、更多功能

#### 📲所有指令

机器人的指令列表在[<B>src/plugins/check.py</B>](src/plugins/check.py)中，有如下指令：

```python
menu = ['/今日运势','/今日塔罗','/图','/点歌','/摸摸头','/群老婆','/今日老婆', "/开启ai","/关闭ai","/角色列表","/添加人设", "/更新人设", "/删除人设", "/切换人设", "/管理员注册",'/待办', '/test','/天气','我喜欢你', "❤", "/待办查询", "/新建待办", "/删除待办" ,"/cf","/B站搜索", "/BV搜索", "/喜报", "/悲报", "/luxun","/鲁迅说","/奶龙", "/repo", "/info", "/menu"]
```

输入其它指令机器人会回复听不懂哦。

<br>

#### ☄️待办、摸一摸、今日运势的初始化

机器人中已经配置好数据库初始化的脚本。若您是第一次启动机器人。会在项目根目录下自动创建<b><i>chat_bot.db</i></b>（数据库文件）

chat_bot.db中包括11张表：

```sql
--摸一摸文本数据
qr_touch
--摸一摸日志
qr_touch_log

--今日运势文本数据
qr_fortune
--今日运势日志，存储该用户是否已经查询过运势
qr_fortune_log

--塔罗牌
major_arcana
--塔罗牌使用 日志
major_arcana_log

--用户表
user_list
--用户待办表
user_todo_list

--群老婆
wife

--所有模型设定
chat_role
--群聊AI状态表
group_chat_role
```

数据库相关脚本存放在 [<b>src/clover_sqlite/models</b>](src/clover_sqlite/models) 目录下。我们使用Tortoise ORM管理数据库。

每次启动机器人，程序会自动检查上述11张表是否存在，有表缺失则会在数据库中自动创建对应的表。

对已存在的表不做处理。

<br>

#### ⛅从图床发送图片

##### 介绍：

机器人支持[<b>SMMS图床</b>](https://sm.ms/)、[<b>聚合图床</b>](https://www.superbed.cn/)、从**本地**发送图片。

获取图片的方法统一编写在[<B>src/clover_image/get_image.py</B>](src/clover_image/get_image.py)下。

##### 使用：

首先找到[<b>src/configs/api_config_example.py</b>](src/configs/api_config_example.py)

```python

app_id="<KEY>"
bot_account= "<KEY>"

"""
图床配置
"""
# SMMS图床相关配置
smms_token= "<KEY>"  # sm.ms图床的token
smms_image_upload_history= "https://sm.ms/api/v2/upload_history"  # sm.ms图床获取上传图片历史API地址

# 聚合图床相关配置
ju_he_token= "<KEY>"  # 聚合图床的token
ju_he_image_list= "https://api.superbed.cn/timeline"  # 聚合图床获取上传图片历史API地址
```

将你的机器人app_id，smms图床Token和聚合图床Token替换上述<i>\<KEY></i>（可以根据自身需求选填）

之后在[<B>get_image.py</B>](src/clover_image/get_image.py)中找到对应的方法，根据自身需求调用。

<br>

#### 🎵使用网易云API实现点歌

##### 介绍：

机器人支持在线点歌，将音乐文件以QQ语音的形式发送至群聊。

快点一首你喜欢的歌给群友听吧！

<br>

##### 使用：

若您是初次使用点歌功能，在群聊中@机器人后，机器人会提示：

```
登录失效，请联系管理员进行登录
```

此时会在[<b>src/music</b>](src/clover_music)目录下生成一张<i><b>qrcode.png</b></i>，您需要使用手机端网易云音乐**扫码**该二维码，登录您的网易云账号。

<br>

<b>🚨注意：</b>我们使用cookie存储用户登录信息，所以会存在登录过期的情况，若cookie过期，机器人会提示

```
歌曲音频获取失败：登录信息失效。
```

此时需要**删除**[<b>cloud_music_cookies.cookie</b>](cloud_music_cookies.cookie)并重新扫码登录。

<br>

#### 💡使用第三方语言模型

打开[<b>src/configs/api_config_example.py</b>](src/configs/api_config_example.py)，找到

```python
"""
AI
"""
admin_password= "123456" # 默认注册管理员密码
# 图灵机器人相关配置
v3url= "https://api.vveai.com/v1/chat/completions"
v3key= "<KEY>"
# DeepSeek相关配置
deepseek_url= "https://api.deepseek.com"
deepseek_key= "<KEY>"
```

将你自己的deepseek url和api填入，并将文件重命名为<b><i>api_config.py</i></b>。

再设置一个管理员认证密码，详见[下一节](#admin_control)。

<br>

#### ✋实现管理员身份认证

##### 介绍：

机器人现已更新管理员机制，机器人管理员可以控制是否使用第三方大语言模型进行交互。

后续其它功能更新中。

##### 使用：

###### 1.注册为管理员<a id="admin_control"></a>

在[**src/configs/api_config_example.py**](src/configs/api_config_example.py)内，找到

```python
admin_password= "123456" # 默认注册管理员密码
```

可以更改为自己的密码。

<br>

设置好密码后，在qq中at你的机器人，格式为

```
@<机器人名称> /管理员注册 <密码>
```

例如，对三叶草进行管理员注册时，假如密码是123456，需要

```
@三叶草 /管理员注册 123456
```

<br>

<b>🚨注意：</b>管理员密码请不要泄露给其他人，建议定期更换密码。

<br>

注册成为管理员之后，你的member_openid将会被保存至<i>chatbot.db下的admin_list</i>表中。

<br>

###### 2.控制语言模型是否可用<a id="ai_control"></a>

在已经是管理员的情况下，你可以对机器人发送

```
@<机器人名称> /开启ai
```

实现对AI功能的开关。若此前AI功能处于关闭状态，则机器人会回复

```
成功开启语言模型对话功能。一起来聊天吧~
```

表示AI功能启动成功。反之则回复

```
成功关闭语言模型对话功能。
```

AI功能为每个群单独启动，默认关闭。

<br>

#### 🔆CodeForces比赛查询

机器人通过访问CodeForces官方API实现获取CF近期比赛。

对机器人发送

```
/cf
```

可查询近期比赛。

<br>

#### 📺B站视频搜索

##### 介绍：

机器人使用哔哩哔哩视频API，可将视频文件发送至群聊。

指令：

```
@<机器人名称> /BV搜索 <BV号>
```

<b>🚨注意：</b>由于QQ的限制，官方bot无法发送时长超出2分钟的视频。

##### 使用：

您需要首先确保自己的电脑安装了[<b>Chrome Driver</b>](https://developer.chrome.google.cn/docs/chromedriver?hl=zh-cn)。

若没安装过，请参考教程：[chromedriver下载与安装方法，亲测可用-CSDN博客](https://blog.csdn.net/zhoukeguai/article/details/113247342)

程序第一次启动时，会获取B站的cookie保存至本地，使用selenium库完成，下载可能较慢，需要稍等一会儿。
