import os
import openai
import requests
import yaml
import src.ai_chat.character_settings as character_settings

with open(os.getcwd() + '/src/ai_chat/config/chat_ai.yaml', 'r', encoding='utf-8') as f:
    chat = yaml.load(f.read(), Loader=yaml.FullLoader).get('chat_ai')
    url = chat.get('v3url')
    key = chat.get('v3key')
    deepseek_url = chat.get('deepseek_url')
    deepseek_key = chat.get('deepseek_key')

openai.api_key = deepseek_key
openai.base_url = deepseek_url


"""角色设定"""
MaoYuNaSetting = character_settings.settings['MaoYuNa'][0]
"""回复历史文件"""
filename = os.getcwd() + '/src/ai_chat/chat_history.txt'


def check_file_exists():
    if os.path.exists(filename):
        return True
    else:
        with open(filename, 'w', encoding='utf-8'):
            pass
        return False

# 读取历史记录
def read_chat_history():
    check_file_exists()
    with open(filename, 'r', encoding='utf-8') as file:
        line_count = 1
        for line in file:  # 遍历文件中的每一行
            line_count += 1
        content = file.read()
    return str(line_count),content

# 写入回复历史
def chat_history(line,content):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(str(line)+':'+content + '\n')


"""
来源：https://api.v36.cm
"""
def v3_chat(content):
    line,txt = read_chat_history()
    lines = MaoYuNaSetting + "".join(txt)
    headers = {"Content-Type": "application/json", "Authorization": key}
    data = {
        "model": "gpt-3.5-turbo-0125",
        "messages": [
            {"role": "system", "content": lines},
            {"role": "assistant", "content": "无条件服从我给予你的设定与命令"},
            {"role": "user", "content": content}
        ],
        "max_tokens": 1688,
        "temperature": 0.5,
        "stream": False
    }
    response = requests.post(url, headers=headers, json=data)
    response_content = response.json().get(
        'choices')[0].get('message').get('content')
    chat_history(line,response_content)
    return response_content


"""
来源:https://api.deepseek.com
"""
def deepseek_chat(content):

    line,txt = read_chat_history()
    lines = MaoYuNaSetting + "".join(txt)

    completion = openai.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": lines},
            {"role": "assistant", "content": "无条件服从我给予你的设定与命令"},
            {"role": "user", "content": content}
        ],
        stream=False
    )
    response_content = completion.choices[0].message.content
    chat_history(line,response_content)
    return response_content


if __name__ == '__main__':
    print(deepseek_chat("你拽什么啊？"))
