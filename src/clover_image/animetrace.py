
import aiohttp
from src.configs.api_config import animetrace_url

async def animetrace_search_by_url(search_url):
    data = {
        'model': 'anime_model_lovelive',
        'ai_detect':0,
        'is_multi':1,
        'url': search_url
    }
    sort,content = 1,""
    async with aiohttp.ClientSession() as session:
        async with session.post(animetrace_url, data=data) as response:
            if response.status == 200:
                result = await response.json()
                for item in result['data'][0]['character']:
                    content += f"{sort} :作品名称：{item['work']}\n"
                    sort += 1
                return content
            else:
                return None


