### 🗒️ 项目结构

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

### 📦插件

  - 插件的目录位于src/plugins中<br>
  - 插件的配置文件位于src/configs中<br>
  - 基本插件存储在plugins目录中，启动即可使用<br>
  - 部分插件通过调用其它目录中的方法完成其功能<br>
  - 部分插件需要调用第三方API，需要在配置文件中填写相关配置<br>

<br>

### 🎈更多功能

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







