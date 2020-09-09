import json, asyncio
from fetch import *

async def fetched():
    jsonData = {
        "id": 30,
        "name": "Someone"
    }

    get_fetch = await Fetcher.get("https://httpbin.org/get")
    del_fetch = await Fetcher.delete("https://httpbin.org/delete")
    post_fetch = await Fetcher.post("https://httpbin.org/post", jsonData)
    print(json.dumps(json.loads(get_fetch), indent = 4), "INI GET")
    print(json.dumps(json.loads(del_fetch), indent = 4), "INI DELETE")
    print(json.dumps(json.loads(post_fetch), indent = 4), "INI POST")


if __name__ == "__main__":
    run_complete = asyncio.get_event_loop()
    run_complete.run_until_complete(fetched())