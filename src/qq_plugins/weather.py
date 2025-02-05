from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg

weather = on_command("天气", rule=to_me(), aliases={"weather", "查天气"}, priority=10, block=True)

@weather.handle()
async def handle_function(args: Message = CommandArg()):

    # 提取参数纯文本作为地名，并判断是否有效
    if location := args.extract_plain_text():
        # 调用天气查询API获取天气数据
        weather_data = format_weather(location)
        await weather.finish(weather_data)
    else:
        await weather.finish("请输入地名")


import requests

def get_weather(location):
    # 设置请求的URL和参数
    url = f'https://apis.juhe.cn/simpleWeather/query?key=50a3bd415158e186903d6e6994157589&city={location.rstrip("市").rstrip("县").rstrip("区")}'
    # 发送GET请求
    response = requests.get(url)
    # 检查请求是否成功
    if response.status_code == 200:
        # 解析返回的JSON数据
        data = response.json()

        # 检查是否查询成功
        if data['reason'] == '查询成功!' or data['reason'] == '查询成功':
            # 返回天气数据
            return data['result']
        else:
            return {"error": "查询失败: " + data['reason']}
    else:
        return {"error": "请求失败，状态码: " + str(response.status_code)}


# 调用函数并处理返回的天气数据
def format_weather(location):
    # 假设这里你已经有了城市的URL编码，这里用'%E9%87%8D%E5%BA%86'作为示例
    city_encoded = location  # 重庆的URL编码
    weather_data = get_weather(city_encoded)

    # 检查是否返回了错误
    if 'error' in weather_data:
        return weather_data['error']
    else:
        # 实时天气
        realtime_weather = weather_data['realtime']
        result = "\n" + location.rstrip("市").rstrip("县").rstrip("区") + f"实时天气:" + "\n" +  f"{realtime_weather['info']}, 温度: {realtime_weather['temperature']}℃, 湿度: {realtime_weather['humidity']}%, 风向: {realtime_weather['direct']}, 风力: {realtime_weather['power']}级, AQI: {realtime_weather['aqi']}"
        # 未来几天的天气
        result = result + "\n" + "未来几天的天气:🌤⛈️☔️"
        for day in weather_data['future']:
            result = result + "\n" + f"日期: {day['date']}, 天气: {day['weather']}, 温度: {day['temperature']}, 风向: {day['direct']}"
        return result

