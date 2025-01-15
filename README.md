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



## 🌈目前功能:

- [x] 待办
- [x] 天气 
- [x] 今日运势
- [x] 点歌（网易云 需扫码登录 在 src\music 目录下）*PC端 QQ可能播放不出来 原因不明*
- [x] 图（返回图库中的图片）
- [ ] 摸摸头（待实现动图）
- [ ] 今日老婆
- [ ] 群老婆




## 🛠️使用

- 关于Nonebot完整部署使用方法，请查看[官方文档](https://nonebot.dev/)




### ⚙️一、环境配置

**我们强烈建议您使用虚拟环境**，若您使用Anaconda发行版，请在终端输入

```powershell
conda create --name chatbot python=3.11
```

创建conda环境。

或者将上述 *chatbot* 更换为你喜欢的名字。



此机器人运行所需依赖已全部打包至***requirements.txt***，您只需回到项目根目录

在终端输入：

```powershell
pip install -r requirements.txt
```

安装所需依赖。



**使用网易云点歌需要另外安装：**

```powershell
npm install crypto-js
```



### ✒️二、配置所需文件

在一切开始前，你需要将项目根目录下的 [example.env.prod](example.env.prod)文件更名为<b><i>.env.prod</i></b>，这是机器人的账号配置文件。

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
    "use_websocket": false
  }
]
'
```
分别在id、token、secret处填写你的机器人ID，机器人Token和Apple Secret，需从[QQ开放平台](https://q.qq.com/)获取。



### 📍二、启动机器人

在项目根目录中，找到 *bot.py* ，在终端输入

```powershell
python bot.by
```

或者选择编译器启动，便可以启动机器人。



### 🗒️三、项目结构

```
└─src
    ├─common_plugins
    │  ├─cloud_music
    │  │          
    │  └─img
    │              
    ├─image
    │  │  get_image.py
    │  │  
    │  ├─config
    │  │      image.yaml
    │  │      
    │  ├─MaoYuNa
    │  │      
    │  ├─tarot
    │     ├─sideTarotImages
    │     │      
    │     └─TarotImages
    │          
    ├─music
    │  │  qrcode.png
    │  │  
    │  ├─cloud_music
    │  │     agent.py
    │  │     cloud_music.py
    │  │     jsdm.js
    │  │          
    │  └─netease_music
    |
    ├─my_sqlite
    │  │  chat_bot.db
    │  │  fortune_by_sqlite.py
    │  │  todo_by_sqlite.py
    │  │  touch_by_sqlite.py
    │  │  
    │  ├─data_init
    │        chat_bot.db
    │        data_init.py
    │        fortune_init_data.py
    │        todo_init.py
    │        touch_init_data.py
    │        
    │          
    ├─onebot_plugins
    │  │  tarot.py
    │  │  test.py
    │  │  welcome.py
    │  │  
    │  └─config
    │          controller.yaml
    │          
    ├─plugins
    │          
    └─qq_plugins
        │  check.py
        │  cloudMusic.py
        │  fortune.py
        │  image.py
        │  today_wife.py
        │  touch.py
        │  to_do.py
        │  weather.py
        │  
        ├─data_init
        │          
        ├─test
               a-testMain.py
```

- 基本插件存储在qq_plugins目录中，启动即可使用
- 部分插件通过调用其它目录中的方法完成其功能



### 🎈四、更多功能

