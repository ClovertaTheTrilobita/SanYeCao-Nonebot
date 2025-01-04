from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.console import MessageSegment
from nonebot.rule import to_me

# 创建一个消息事件处理器，当收到消息时触发
reply = on_command("你好", rule=to_me(), priority=10, block=True)


@reply.handle()
async def handle_reply(bot: Bot, event: Event):
    # 获取用户发送的消息
    user_message = event.get_message().extract_plain_text().strip().replace(" ", "").replace("/", "")


    # 这里构建Markdown格式的消息内容
    # markdown_message = MessageSegment.markdown(
    #     """
    #     ### 这是标题
    #     这是一段正文内容，你可以在这里按照[Markdown语法](https://www.markdown.com.cn/)添加更多元素，比如**加粗**、*斜体*等。
    #     - 列表项1
    #     - 列表项2
    #      - 今天天气怎么样？
    #                ⛅ 多云 20℃~24℃
    #                🌡️ 风速 1-2级
    #                💨 10-15公里/小时
    #                🌬️ 微风 2-3级
    #                🌡️ 降水概率 50%
    #                🌡️ 降水强度 微弱
    #                🌡️ 紫外线强度 弱
    #                🌡️ 能见度 10公里
    #
    #     """
    # )
    # await bot.send(event=event, message=markdown_message, at_sender=True)
    # 定义回复内容
    if user_message == "你好":
        reply_message = "你好呀！我是你的机器人助手。"
    elif user_message == "今天天气怎么样":
        reply_message = "抱歉，我暂时无法得知天气信息哦 你可以通过天气预报网站查询。"
    else:
        reply_message = "我不太理解你的意思呢，你可以换个说法试试。"
    # 发送回复消息
    await bot.send(event=event, message=reply_message)

# @reply.handle()
# async def hp(bot: Bot, event: Event):
#     # 获取全部群列表
#     group_list = await bot.get_group_list()
#
#     for group in group_list:
#         print(group)
#         # 获取群成员列表
#         member_list = await bot.get_group_member_list(group_id=group['group_id'])
#         for member in member_list:
#             print(member)
#             # 获取群成员信息
# await bot.get_group_member_info(group_id=group['group_id'],
# user_id=member['user_id'])
