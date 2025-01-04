from nonebot.adapters.cqhttp import Bot, Message, GroupMessageEvent, GroupDecreaseNoticeEvent, GroupIncreaseNoticeEvent
from nonebot import on_notice

welcome = on_notice()

# 监听加群事件
@welcome.handle()  # 监听 welcome
async def welcome_new_member(event: GroupIncreaseNoticeEvent):
    user = event.get_user_id()  # 获取新成员的id
    at_ = "爆裂吧！现实！粉碎吧！精神！Banishiment this world！！ 应召唤而来 [CQ:at,qq={}]".format(user)
    msg = at_ + '欢迎加入本群！'
    msg = Message(msg)
    await welcome.finish(message=Message(f'{msg}'))  # 发送消息

