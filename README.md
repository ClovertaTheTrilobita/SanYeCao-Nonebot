# SanYeCao-Nonebot

## How to start

1. generate project using `nb create` .
2. install plugins using `nb plugin install` .
3. run your bot using `nb run` .

## Documentation

See [Docs](https://nonebot.dev/)

pip install -r requirements.txt

你需要把你 [example.env.prod](example.env.prod)文件改为你自己的配置文件
如果没有可以自己创建一个
.env.prod

内容如下

```
DRIVER=~fastapi+~httpx+~websockets

QQ_IS_SANDBOX=false

QQ_BOTS='[{
    "id": "",
    "token": "",
    "secret": "",
    "intent": {
        "guild_messages": true,
        "c2c_group_at_messages": true
        },
    	"use_websocket": false
    }]'
```

