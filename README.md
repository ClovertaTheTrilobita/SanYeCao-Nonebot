# SanYeCao-Nonebot

## 📚介绍

<p align="center">🌟三叶草bot 2.0🌟<br>
🚀使用Nonebot2+官方API搭建的QQ群聊机器人🚀<br><br>
<img alt="Static Badge" src="https://img.shields.io/badge/Python-3.11%2F3.12-blue">
<img alt="Static Badge" src="https://img.shields.io/badge/Nonebot-2.0-green">
<img src="https://img.shields.io/github/last-commit/ClovertaTheTrilobita/SanYeCao-Nonebot" alt="last-commit" /><img alt="Static Badge" src="https://img.shields.io/badge/QQ%E7%BE%A4-710101225-orange"><br><br>
</p>


## 🔖亮点

- 基于[Nonebot2](https://nonebot.dev/)，使用[QQ官方API](https://bot.q.qq.com/wiki/)，更稳定、高效✨
- 多种个性化用法，如天气、每日运势(~~机器人时尚单品~~)、点歌、编辑个人待办等，后续功能开发中🔧
- 使用轻量化数据库sqlite管理数据，实现为每位用户单独存取数据🔍
- 接入第三方大语言模型，实现AI交互💡

<br>

## 🌈目前功能:

- [x] 待办
- [x] 天气 
- [x] 今日运势
- [ ] 今日塔罗
- [x] 点歌（网易云 需扫码登录 在 src\music 目录下）*PC端 QQ可能播放不出来 原因不明*
- [x] 图（返回图库中的图片）
- [x] 摸摸头
- [x] 接入语言模型
- [ ] 今日老婆
- [ ] 群老婆

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
├─node_modules
│  └─crypto-js
│      └─docs
└─src
    ├─ai_chat
    │  ├─config
    ├─common_plugins
    │  ├─cloud_music
    │  └─img
    ├─image
    │  ├─config
    │  ├─MaoYuNa
    │  ├─qq_image
    │  ├─rua
    │  ├─tarot
    │  │  ├─sideTarotImages
    │  │  └─TarotImages
    ├─music
    │  ├─cloud_music
    │  └─netease_music
    ├─my_sqlite
    │  ├─data_init
    |
    ├─onebot_plugins
    │  └─config
    ├─plugins
    └─qq_plugins
        ├─data_init
        ├─test
```

- 基本插件存储在qq_plugins目录中，启动即可使用
- 部分插件通过调用其它目录中的方法完成其功能

<br>

### 🎈四、更多功能

#### 📲所有指令

机器人的指令列表在[<B>src/qq_plugins/check.py</B>](src/qq_plugins/check.py)中，有如下指令：

```python
menu = ['/今日运势','/天气','/图','/点歌','/摸摸头','/群老婆','/今日老婆', '/待办', '/test', '我喜欢你', "❤", "/待办查询", "/新建待办", "/删除待办", "/activate_ai", "/cf", "/管理员确认"]
```

输入其它指令机器人会回复听不懂哦。

<br>

#### ☄️待办、摸一摸、今日运势的初始化

机器人中已经配置好数据库初始化的脚本。若您是第一次启动机器人。会在项目根目录下自动创建<b><i>chat_bot.db</i></b>（数据库文件）

chat_bot.db中包括七张表：

```sql
--摸一摸文本数据
qr_touch
--摸一摸日志
qr_touch_log

--今日运势文本数据
qr_fortune
--今日运势日志，存储该用户是否已经查询过运势
qr_fortune_log

--用户列表
user_list
--用户待办表
user_todo_list

--管理员表
admin_list
```

初始化相关脚本存放在 [<b>src/my_sqlite/data_init</b>](src/my_sqlite/data_init) 目录下。

每次启动机器人，程序会自动检查上述七张表是否存在，有表缺失则会在数据库中自动创建对应的表。

对已存在的表不做处理。

<br>

#### ⛅从图床发送图片

##### 介绍：

机器人支持[<b>SMMS图床</b>](https://sm.ms/)、[<b>聚合图床</b>](https://www.superbed.cn/)、从**本地**发送图片。

获取图片的方法统一编写在[<B>src/image/get_image.py</B>](src/image/get_image.py)下。

##### 使用：

首先找到[<b>src/image/config/image.yaml</b>](src/image/config/image.yaml)

```yaml
image:
  app_id: "<KEY>"
  image_local_qq_image_path: "src/image/qq_image"
  image_local_path: "src/image/MaoYuNa"
  #SMMS图床相关配置
  smms_token: "<KEY>" # sm.ms图床的token
  smms_image_upload_history: "https://sm.ms/api/v2/upload_history" # sm.ms图床获取上传图片历史API地址
  #聚合图床相关配置
  ju_he_token: "<KEY>" # 聚合图床的token
  ju_he_image_list: "https://api.superbed.cn/timeline"  # 聚合图床获取上传图片历史API地址
```

将你的机器人app_id，smms图床Token和聚合图床Token替换上述<i>\<KEY></i>（可以根据自身需求选填）

之后在[<B>get_image.py</B>](src/image/get_image.py)中找到对应的方法，根据自身需求调用。

<br>

#### 🎵使用网易云API实现点歌

##### 介绍：

机器人支持在线点歌，将音乐文件以QQ语音的形式发送至群聊。

快点一首你喜欢的歌给群友听吧！

<br>

*PC端QQ由于未知原因可能会出现播放失败的问题，<u>这绝对不是咱的问题，绝对不是！</u>*

##### 使用：

若您是初次使用点歌功能，在群聊中@机器人后，机器人会提示：

```
登录失效，请联系管理员进行登录
```

此时会在[<b>src/music</b>](src/music)目录下生成一张<i><b>qrcode.png</b></i>，您需要使用手机端网易云音乐**扫码**该二维码，登录您的网易云账号。

<br>

<b>🚨注意：</b>目前点歌的实现方法为获取请求到的第一首歌，并且自动跳过无法下载（付费）歌曲，若您想点的歌原唱为付费，可能会随机到一首翻唱或其它版本。

<br>

#### 💡使用第三方语言模型

打开[<b>src/ai_chat/config/example.chat_ai.yaml</b>](src/ai_chat/config/chat_ai.yaml)

```yaml
chat_ai:
  v3url: "<key>"
  v3key: "<key>"
  deepseek_url: "<key>"
  deepseek_key: "<key>"
  active: "False" # True为启动ai功能，False为关闭功能
```

将你自己的deepseek url和api填入，并将文件重命名为<b><i>chat_ai.yaml</i></b>。

起用ai功能请将active改为True，或详见下一节。

<br>

#### ✋实现管理员身份认证

##### 介绍：

机器人现已更新管理员机制，机器人管理员可以控制是否使用第三方大语言模型进行交互。

后续其它功能更新中。

<br>

##### 使用：

###### 1.注册为管理员

在[<b>src/qq_plugins/check.py</b>](src/qq_plugins/check.py)内，找到

```python
"""
设置管理员鉴权密码
"""
admin_passwd = "1234"
```

在这里，你可以修改你的管理员密码*（默认为1234）*

<br>

设置好你的密码后，在qq中at你的机器人，格式为

```
@<机器人名称> /管理员确认 <密码>
```

例如，使用默认密码对三叶草进行管理员注册时，假如密码是1234，需要

```
@三叶草 /管理员确认 1234
```

<br>

<b>🚨注意：</b>管理员密码请不要泄露给其他人，建议单独创建一个群用于注册管理员。

<br>

注册成为管理员之后，你的member_openid将会被保存至<i>chatbot.db下的admin_list</i>表中。

<br>

###### 2.控制语言模型是否可用

在已经是管理员的情况下，你可以对机器人发送

```
@<机器人名称> /activate_ai
```

实现对AI功能的开关。若此前AI功能处于关闭状态，则机器人会回复

```
成功开启语言模型对话功能。一起来聊天吧~
```

表示AI功能启动成功。反之则回复

```
成功关闭语言模型对话功能。
```

