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
- [x] 点歌（网易云 需扫码登录 在 src\music 目录下）
- [x] 图（返回图库中的图片）
- [x] 摸摸头
- [x] 接入语言模型
- [x] 搜索B站视频
- [ ] 今日老婆
- [x] 群老婆
- [x] 鲁迅说
- [x] 喜报、悲报
- [x] 查询cf比赛
- [x] 日报
- [x] 查询热门轻小说
- [x] 获取新番信息
- [x] 绝对色感

#### 更多详细功能请查看<b>[features.md](docs/features.md)</b>.


## 🛠️ 安装

- 关于Nonebot完整部署使用方法，请查看[官方文档](https://nonebot.dev/)

<br>


### ⚙️一、环境配置

**我们强烈建议您使用虚拟环境**，若您使用Anaconda发行版，请在终端输入

```powershell
conda create --name chatbot python=3.11
```

创建conda环境。

之后

```powershell
conda activate chatbot
```

以启用您刚刚创建的虚拟环境。

你也可以将上述 *chatbot* 更换为你喜欢的名字。

<b>🚫注意：</b>机器人<b>不</b>支持<img alt="Static Badge" src="https://img.shields.io/badge/Python-3.13/+-blue">的发行版，推荐使用<img alt="Static Badge" src="https://img.shields.io/badge/Python-3.11%2F3.12-blue">

<br>

### 🧪 安装所需依赖

<br>

此机器人运行所需依赖已全部打包至***requirements.txt***，您只需回到项目根目录

在终端输入：

```powershell
pip install -r requirements.txt
```
<br>

### 🎵 网易云点歌依赖安装

#### 1. 安装 Node.js 环境
- **官网下载**：访问 [Node.js 官网](https://nodejs.org/) 下载 LTS 版本（推荐 v18.x+）
- **安装注意**：
  - 勾选 `Add to PATH` 选项（自动配置环境变量）
  - 完成安装后重启终端使配置生效
  验证 Node.js 版本
- **对于Debian/Ubuntu**
- 你可以直接用以下命令安装
  ```shell
  sudo apt install nodejs npm
  ```
#### 2. 验证安装结果
```powershell
npm -v
```
#### 3. 安装 crypto-js 库
在项目根目录执行：
```powershell
npm install crypto-js
```
<br>

### ✒️二、配置所需文件

在一切开始前，你需要将项目根目录下的[<b>example.env.prod</b>](example.env.prod)文件更名为<b><i>.env.prod</i></b>，这是机器人的账号配置文件。

我加了神必小代码，如果你没配置这两个配置文件是启动不起来的，因为有<span style="color:gray">~~海量~~</span>个例显示，很多人不看README就想当然地启动bot，并在群里问为什么会有报错（

```
DRIVER=~fastapi+~httpx+~websockets

QQ_IS_SANDBOX=false

QQ_BOTS="
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
"
```
分别在id、token、secret处填写你的机器人ID，机器人Token和Apple Secret，需从[QQ开放平台](https://q.qq.com/)获取。

<br>

#### 📄 需要修改的配置文件

首先找到 [**example.config.yaml**](example.config.yaml) ，将其重命名为<b>config.yaml</b>

并根据需要替换以下配置项：

```yaml
#######################################
# 如果您已经配置好了，请将此字段改为 ‘False’#
#######################################
default: "True" # 配置完成后，请将这个字段改为 False

bot:
  app_id: ""
  bot_account: ""

############################
#     三叶草邮箱发信设置      #
############################
mail:
  google:
    enabled: 'False'
    smtp_server: 'smtp.gmail.com'
    email: 'xxxxxx@gmail.com'
    password: '1234567891234567' # 16 位应用码

  qq:
    enabled: 'True'
    smtp_server: 'smtp.qq.com'
    email: 'xxxxxxxx@qq.com'
    password: '1234567891234567' # qq邮箱应用码

  server: # 自建服务器
    enabled: 'False'
    smtp_server: 'mail.example.com' # 自建邮局域名
    email: 'user_name@example.com'
    password: '123456'
    port: '587'

############################
#       三叶草图床设置       #
############################
image_hosting:
  smms: # sm.ms图床
    enabled: 'False'
    token: '<KEY>'
    smms_image_upload_history: "https://sm.ms/api/v2/upload_history"

  superbed: # 聚合图床
    enabled: 'False'
    token: '<KEY>'
    superbed_image_list: "https://api.superbed.cn/timeline"

  random_pic: "https://image.anosu.top/pixiv/json"

  animetrace:
    url: "https://api.animetrace.com/v1/search"

############################
#        三叶草AI设置        #
############################
ai:
  admin:
    password: '123456'

  api:
    v3:
      enabled: "False"
      url: "https://api.vveai.com/v1/chat/completions"
      key: '<KEY>'

    deepseek:
      enabled: "False"
      url: "https://api.deepseek.com"
      key: '<KEY>'

    silicon_flow:
      enabled: "True"
      url: "https://api.siliconflow.cn/v1/chat/completions"
      model: "Pro/deepseek-ai/DeepSeek-V3"
      key: '<KEY>'

############################
#       其他时尚小功能       #
############################

wenku8:
  # 通过wenku8.com获取最新轻小说咨询
  # 此功能需要启用代理
  enabled: 'False'
  user_name: '<user_name>'
  password: '<passwd>'

proxy:
  # 目前代码中仅支持多米HTTP代理
  enabled: 'False'
  key: '<KEY>'

qr:
  # 二维码生成api
  url: "https://api.qrserver.com/v1/create-qr-code/"
  size: "200x200"

codeforces:
  # 查询codeforces比赛列表
  key: "<KEY>"
  secret: "<KEY>"
```

<b>🚫注意：</b> 将你的 `app_id` 和 `smms_token` 替换为实际值（可以根据自身需求选填）

<br>

### 📍三、启动机器人

在项目根目录中，找到 *bot.py* ，在终端输入

```powershell
python bot.py
```

<br>

<br>

### 🎨 功能补充说明


#### 🎵 使用网易云API实现点歌

若您是初次使用点歌功能，在群聊中 @ 机器人后，机器人会提示：

```
登录失效，请联系管理员进行登录
```


此时会在 [**src/music**](src/clover_music) 目录下生成一张 **qrcode.png**，您需要使用手机端网易云音乐扫码该二维码，登录您的网易云账号。

<b>注意：</b> 我们使用 cookie 存储用户登录信息，所以会存在登录过期的情况。若 cookie 过期，机器人会提示：

```
歌曲音频获取失败：登录信息失效。
```


此时需要并重新扫码登录。

<br>

#### ✋ 管理员身份认证

##### 介绍

机器人管理员可以控制是否使用第三方大语言模型进行交互。后续其它功能更新中。

##### 使用

###### 1. 注册为管理员 <a id="admin_control"></a>

在 [**config.yaml**](config.yaml) 内，找到：

```python
ai:
  admin:
    password: '123456'
```


可以更改为自己的密码。

设置好密码后，在 QQ 中 at 你的机器人，格式为：

```
@<机器人名称> /管理员注册 <密码>
```


例如，对三叶草进行管理员注册时，假如密码是 123456，需要：

```
@三叶草 /管理员注册 123456
```


<b>注意：</b> 管理员密码请不要泄露给其他人，建议定期更换密码。

注册成为管理员之后，你的 `member_openid` 将会被保存至 `chatbot.db` 下的 `admin_list` 表中。

<br>

<br>

### 更多配置内容，请详见[configuration.md](docs/configuration.md)



