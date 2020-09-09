import json, asyncio, aiohttp

class Fetcher:
    @staticmethod
    async def get(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.text()

    @staticmethod
    async def post(url, data):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json = data) as resp:
                return await resp.text()

    @staticmethod
    async def delete(url):
        async with aiohttp.ClientSession() as session:
            async with session.delete(url) as resp:
                return await resp.text()