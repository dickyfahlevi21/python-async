import asyncio, json
from fetch import *


async def fetch_user(id):
    url_user = await Fetcher.get('https://jsonplaceholder.typicode.com/users/{id}')
    data_user = json.loads(url_user)
    return data_user

async def fetch_post():
    url_post = await Fetcher.get('https://jsonplaceholder.typicode.com/posts')
    data_post = json.loads(url_post)
    return data_post

async def combine():
    list_combine = []
    for post in await fetch_post():
        user = asyncio.create_task(fetch_user(post['userId']))
        list_combine.append(user)
        for task in list_combine:
            post['user'] = await task
        print(json.dumps(post, indent=4))
    

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(combine())