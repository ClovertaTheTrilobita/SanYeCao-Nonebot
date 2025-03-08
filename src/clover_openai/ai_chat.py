import openai
import requests
from src.clover_sqlite.models.chat import GroupChatRole
from src.configs.api_config import v3url, v3key, deepseek_url, deepseek_key,silicon_flow_key
import aiohttp

"""
来源：https://api.v36.cm
"""
async def v3_chat(group_openid,content):

    await GroupChatRole.save_chat_history(group_openid, {"role": "user", "content": content})
    messages = await GroupChatRole.get_chat_history(group_openid)
    headers = {"Content-Type": "application/json", "Authorization": v3key}
    data = {
        "model": "gpt-3.5-turbo-0125",
        "messages": messages,
        "max_tokens": 1688,
        "temperature": 0.5,
        "stream": False
    }
    response = requests.post(v3url, headers=headers, json=data)
    reply_content = response.json().get('choices')[0].get('message').get('content')
    await GroupChatRole.save_chat_history(group_openid, {"role": "assistant", "content": reply_content})
    return reply_content


"""
来源:https://api.deepseek.com
"""
async def deepseek_chat(group_openid,content):
    """
    ai 角色扮演聊天
    :param group_openid:
    :param content:
    :return:
    """
    openai.api_key = deepseek_key
    openai.base_url = deepseek_url
    await GroupChatRole.save_chat_history(group_openid, {"role": "user", "content": content})
    messages = await GroupChatRole.get_chat_history(group_openid)
    completion = openai.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        stream=False
    )
    reply_content = completion.choices[0].message.content
    await GroupChatRole.save_chat_history(group_openid, {"role": "assistant", "content": reply_content})
    return reply_content

async def silicon_flow(group_openid, content):
    await GroupChatRole.save_chat_history(group_openid, {"role": "user", "content": content})
    messages = await GroupChatRole.get_chat_history(group_openid)
    url = "https://api.siliconflow.cn/v1/chat/completions"
    payload = {
        "model": "Pro/deepseek-ai/DeepSeek-V3",
        "stream": False,
        "messages": messages
    }
    headers = {
        "Authorization": f"Bearer {silicon_flow_key}",
        "Content-Type": "application/json"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as response:
            result = await response.json()
            print(result)
            reply_content = result["choices"][0]["message"]["content"]

    await GroupChatRole.save_chat_history(group_openid, {"role": "assistant", "content": reply_content})
    return reply_content

if __name__ == '__main__':
    print(deepseek_chat("你拽什么啊？"))
