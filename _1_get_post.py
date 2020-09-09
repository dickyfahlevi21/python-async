import urllib.request, json, asyncio
from fetch import *


async def get_post():
    url_post = await Fetcher.get("https://jsonplaceholder.typicode.com/posts")
    data_post = json.loads(url_post)
    print('\n'.join(list(map(lambda data_post: f"title: {data_post['title']}", data_post))))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_post())

# Resources: https://realpython.com/async-io-python/