import os
import openai
import requests
import yaml
from src.ai_chat.chat_history import save_chat_history,get_chat_history

with open(os.getcwd() + '/src/ai_chat/config/chat_ai.yaml', 'r', encoding='utf-8') as f:
    chat = yaml.load(f.read(), Loader=yaml.FullLoader).get('chat_ai')
    url = chat.get('v3url')
    key = chat.get('v3key')
    deepseek_url = chat.get('deepseek_url')
    deepseek_key = chat.get('deepseek_key')

openai.api_key = deepseek_key
openai.base_url = deepseek_url

"""
来源：https://api.v36.cm
"""
def v3_chat(content):

    save_chat_history({"role": "user", "content": content})
    messages = get_chat_history()
    headers = {"Content-Type": "application/json", "Authorization": key}
    data = {
        "model": "gpt-3.5-turbo-0125",
        "messages": messages,
        "max_tokens": 1688,
        "temperature": 0.5,
        "stream": False
    }
    response = requests.post(url, headers=headers, json=data)
    reply_content = response.json().get('choices')[0].get('message').get('content')
    save_chat_history({"role": "assistant", "content": reply_content})
    return reply_content


"""
来源:https://api.deepseek.com
"""
def deepseek_chat(content):

    save_chat_history({"role": "user", "content": content})
    messages = get_chat_history()
    completion = openai.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        stream=False
    )
    reply_content = completion.choices[0].message.content
    save_chat_history({"role": "assistant", "content": reply_content})
    return reply_content

if __name__ == '__main__':
    print(deepseek_chat("你拽什么啊？"))
