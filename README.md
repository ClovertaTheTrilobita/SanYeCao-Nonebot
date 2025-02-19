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
- [x] 鲁迅说
- [x] 喜报、悲报
- [x] 查询cf比赛
- [x] 日报
- [x] 查询热门轻小说
- [x] 获取新番信息

#### 待办
- **功能描述**: 用户可以添加、查询和删除个人待办事项。
- **指令**: `/待办`, `/待办查询`, `/新建待办`, `/删除待办`

#### 天气
- **功能描述**: 提供当前天气信息。
- **指令**: `/天气`

#### 今日运势
- **功能描述**: 提供用户的今日运势。
- **指令**: `/今日运势`

#### 今日塔罗
- **功能描述**: 提供一张随机的塔罗牌及其解读。
- **指令**: `/今日塔罗`

#### 点歌
- **功能描述**: 通过网易云音乐API点歌，并将音乐文件以QQ语音的形式发送至群聊。 快点一首你喜欢的歌给群友听吧！
- **指令**: `/点歌`
- **注意事项**: 
  - 使用网易云点歌需要另外安装依赖： npm install crypto-js
  - 初次使用需要扫码登录网易云音乐。
  - 若cookie过期，需要删除 `cloud_music_cookies.cookie` 文件并重新扫码登录。

#### 图
- **功能描述**: 返回图库中的图片。
- **指令**: `/图`

#### 摸摸头
- **功能描述**: 与机器人进行互动，发送“摸摸头”的回复。
- **指令**: `/摸摸头`

#### 接入语言模型
- **功能描述**: 使用第三方大语言模型进行交互。
- **指令**: `/开启ai`, `/关闭ai`  `/角色列表`,`/添加人设`, `/更新人设`, `/删除人设`, `/切换人设`, `/管理员注册`
- **注意事项**: 
  - 需要管理员身份认证。
  - AI功能为每个群单独启动，默认关闭。

#### 搜索B站视频
- **功能描述**: 通过BV号搜索B站视频，并将视频文件发送至群聊。
- **指令**: `/BV搜索 <BV号>`
- **注意事项**: 
  - <b>🚨注意：</b> 由于QQ的限制，官方bot无法发送文件大于10M。
  - 需要安装 Chrome Driver。您需要首先确保自己的电脑安装了[<b>Chrome Driver</b>](https://developer.chrome.google.cn/docs/chromedriver?hl=zh-cn)。
  - 若没安装过，请参考教程：[chromedriver下载与安装方法，亲测可用-CSDN博客](https://blog.csdn.net/zhoukeguai/article/details/113247342)
  - 程序第一次启动时，会获取B站的cookie保存至本地，使用selenium库完成，下载可能较慢，需要稍等一会儿。

#### 今日老婆
- **功能描述**: 提供今日老婆的信息。
- **指令**: `/今日老婆`
- **状态**: 待开发

#### 群老婆
- **功能描述**: 提供群内成员的老婆信息。
- **指令**: `/群老婆`

#### 鲁迅说
- **功能描述**: 提供鲁迅的经典语录。
- **指令**: `/鲁迅说`,`/luxun`

#### 喜报、悲报
- **功能描述**: 提供喜报和悲报的信息。
- **指令**: `/喜报`, `/悲报`

#### 查询cf比赛
- **功能描述**: 通过CodeForces官方API查询近期比赛。
- **指令**: `/cf`

#### 日报
- **功能描述**: 提供每日的新闻或信息。
- **指令**: `/日报`

#### 查询热门轻小说
- **功能描述**: 查询当前热门的轻小说。
- **指令**: `/轻小说`

#### 获取新番信息
- **功能描述**: 获取当季动漫的新番信息和预期新番上线信息。
- **指令**: `/本季新番`, `/新番观察`

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

### 📍二、启动机器人

在项目根目录中，找到 *bot.py* ，在终端输入

```powershell
python bot.py
```

或者选择编译器启动，便可以启动机器人。

<br>

当然可以！以下是根据您提供的文件内容整理后的项目结构：

### 🗒️ 三、项目结构

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
    │  └─get_image.py
    │          
    ├─clover_music
    │  ├─cloud_music         
    │  │  ├─cloud_music_cookies.cookie
    │  │  └─qrcode.png
    │  └─netease_music
    │          
    ├─clover_openai
    │  ├─api_config_example.py
    │  └─api_config.py
    │          
    ├─clover_sqlite
    │  ├─data_init      
    │  │  ├─init_tables.py
    │  │  └─...
    │  └─models
    │     ├─models.py
    │     └─...
    │              
    ├─clover_videos
    │  └─billibili
    │     ├─bilibili_search.py
    │     └─...
    │              
    ├─configs
    │  ├─path_config.py
    │  ├─api_config_example.py
    │  └─utils
    │     ├─utils.py
    │     └─...
    │          
    ├─plugins
    │  ├─check.py
    │  ├─todo.py
    │  ├─weather.py
    │  ├─fortune.py
    │  ├─tarot.py
    │  ├─music.py
    │  ├─image.py
    │  ├─petpet.py
    │  ├─openai.py
    │  ├─bilibili.py
    │  ├─news.py
    │  ├─light_novel.py
    │  ├─anime.py
    │  └─...
    │          
    └─resources
        ├─font
        │  ├─font.ttf
        │  └─...
        ├─image
        │  ├─codeforces
        │  │  ├─image1.png
        │  │  └─...
        │  ├─github_repo
        │  │  ├─image2.png
        │  │  └─...
        │  ├─good_bad_news
        │  │  ├─image3.png
        │  │  └─...
        │  ├─MaoYuNa
        │  │  ├─image4.png
        │  │  └─...
        │  ├─rua
        │  │  ├─image5.png
        │  │  └─...
        │  ├─tarot
        │  │  ├─sideTarotImages
        │  │  │  ├─image6.png
        │  │  │  └─...
        │  │  └─TarotImages
        │  │     ├─image7.png
        │  │     └─...
        │  └─who_say
        │     ├─image8.png
        │     └─...
        ├─log
        │  ├─bot.log
        │  └─...
        ├─temp
        │  ├─temp_file1.tmp
        │  └─...
        └─videos
           ├─video1.mp4
           └─...
```


### 详细说明

- **根目录文件**
  - `.gitignore`: 忽略文件配置。
  - `bot.py`: 机器人启动文件。
  - `chat_bot.db`: SQLite 数据库文件。
  - `example.env.prod`: 示例环境配置文件。
  - `package-lock.json`: npm 依赖锁定文件。
  - `package.json`: npm 依赖配置文件。
  - `pyproject.toml`: Python 项目配置文件。
  - `README.md`: 项目说明文档。
  - `requirements.txt`: Python 依赖配置文件。

- **node_modules**
  - `crypto-js`: 加密库。

- **src 目录**
  - **clover_image**
    - `get_image.py`: 图片获取模块。
  
  - **clover_music**
    - **cloud_music**
      - `cloud_music_cookies.cookie`: 网易云音乐 cookie 文件。
      - `qrcode.png`: 网易云音乐扫码登录二维码。
    - **netease_music**
      - 网易云音乐相关模块。
  
  - **clover_openai**
    - `api_config_example.py`: 示例 API 配置文件。
    - `api_config.py`: 实际 API 配置文件。
  
  - **clover_sqlite**
    - **data_init**
      - `init_tables.py`: 数据库初始化脚本。
      - 其他初始化脚本。
    - **models**
      - `models.py`: 数据库模型定义。
      - 其他模型定义文件。
  
  - **clover_videos**
    - **bilibili**
      - `bilibili_search.py`: B站视频搜索模块。
      - 其他 B站相关模块。
  
  - **configs**
    - `path_config.py`: 路径配置文件。
    - `api_config_example.py`: 示例 API 配置文件。
    - **utils**
      - `utils.py`: 工具函数。
      - 其他工具函数文件。
  
  - **plugins**
    - `check.py`: 指令检查模块。
    - `todo.py`: 待办事项模块。
    - `weather.py`: 天气模块。
    - `fortune.py`: 运势模块。
    - `tarot.py`: 塔罗牌模块。
    - `music.py`: 点歌模块。
    - `image.py`: 图片模块。
    - `petpet.py`: 摸摸头模块。
    - `openai.py`: AI 模块。
    - `bilibili.py`: B站视频模块。
    - `news.py`: 日报模块。
    - `light_novel.py`: 轻小说模块。
    - `anime.py`: 新番信息模块。
    - 其他插件模块。
  
  - **resources**
    - **font**
      - `font.ttf`: 字体文件。
      - 其他字体文件。
    - **image**
      - **codeforces**
        - `image1.png`: 图片文件。
        - 其他图片文件。
      - **github_repo**
        - `image2.png`: 图片文件。
        - 其他图片文件。
      - **good_bad_news**
        - `image3.png`: 图片文件。
        - 其他图片文件。
      - **MaoYuNa**
        - `image4.png`: 图片文件。
        - 其他图片文件。
      - **rua**
        - `image5.png`: 图片文件。
        - 其他图片文件。
      - **tarot**
        - **sideTarotImages**
          - `image6.png`: 图片文件。
          - 其他图片文件。
        - **TarotImages**
          - `image7.png`: 图片文件。
          - 其他图片文件。
      - **who_say**
        - `image8.png`: 图片文件。
        - 其他图片文件。
    - **log**
      - `bot.log`: 日志文件。
      - 其他日志文件。
    - **temp**
      - `temp_file1.tmp`: 临时文件。
      - 其他临时文件。
    - **videos**
      - `video1.mp4`: 视频文件。
      - 其他视频文件。

<br>
### 📦三、插件
  - 插件的目录位于src/plugins中<br>
  - 插件的配置文件位于src/configs中<br>
  - 基本插件存储在plugins目录中，启动即可使用<br>
  - 部分插件通过调用其它目录中的方法完成其功能<br>
  - 部分插件需要调用第三方API，需要在配置文件中填写相关配置<br>

<br>

### 🎈四、更多功能

#### 📲所有指令

机器人的指令列表在[<B>src/plugins/check.py</B>](src/plugins/check.py)中，有如下指令：

```python
menu = ["/重启","/今日运势","/今日塔罗","/图","/日报","/点歌","/摸摸头","/群老婆","/今日老婆", "/开启ai","/关闭ai",
        "/角色列表","/添加人设", "/更新人设", "/删除人设", "/切换人设", "/管理员注册","/待办", "/test","/天气",
        "我喜欢你", "❤", "/待办查询", "/新建待办", "/删除待办" ,"/cf","/B站搜索", "/BV搜索", "/喜报", "/悲报",
        "/luxun","/鲁迅说", "/奶龙", "/repo", "/info", "/menu", "/轻小说","/本季新番","/新番观察"]
```

输入其它指令机器人会回复听不懂哦。

<br>



### 🎨 功能补充说明

#### 📄 需要替换的文件

首先找到 [**src/configs/api_config_example.py**](src/configs/api_config_example.py) 文件，并根据需要替换以下配置项：

```python
app_id = "<KEY>"
bot_account = "<KEY>"

"""
图床配置
"""
# SMMS图床相关配置
smms_token = "<KEY>"  # sm.ms图床的token
smms_image_upload_history = "https://sm.ms/api/v2/upload_history"  # sm.ms图床获取上传图片历史API地址

# 聚合图床相关配置
ju_he_token = "<KEY>"  # 聚合图床的token
ju_he_image_list = "https://api.superbed.cn/timeline"  # 聚合图床获取上传图片历史API地址

"""
AI
"""
admin_password = "123456"  # 默认注册管理员密码
# 图灵机器人相关配置
v3url = "https://api.vveai.com/v1/chat/completions"
v3key = "<KEY>"
# DeepSeek相关配置
deepseek_url = "https://api.deepseek.com"
deepseek_key = "<KEY>"

"""
Wenku8账号
"""
wenku8_username = "<user_name>"
wenku8_password = "<passwd>"

"""
多米HTTP代理api
"""
proxy_api = "<KEY>"
```


将你的 `app_id` 和 `smms_token` 替换为实际值（可以根据自身需求选填），然后将文件重命名为 **api_config.py**。

<br>

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


此时需要 **删除** [**cloud_music_cookies.cookie**](cloud_music_cookies.cookie) 并重新扫码登录。

<br>

#### ✋ 管理员身份认证

##### 介绍

机器人现已更新管理员机制，机器人管理员可以控制是否使用第三方大语言模型进行交互。后续其它功能更新中。

##### 使用

###### 1. 注册为管理员 <a id="admin_control"></a>

在 [**src/configs/api_config_example.py**](src/configs/api_config_example.py) 内，找到：

```python
admin_password = "123456"  # 默认注册管理员密码
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

希望这些优化后的说明能更好地帮助您！如果有任何进一步的需求或修改，请告诉我。



