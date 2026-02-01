import asyncio
import aiohttp

async def fetch_json(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            resp.raise_for_status()           # 不是 2xx 就抛异常
            return await resp.json()          # 解析 JSON（返回 dict/list）

async def main():
    url = "https://httpbin.org/json"
    data = await fetch_json(url)
    print(data)

if __name__ == "__main__":
    asyncio.run(main())
