import json, asyncio
from fetch import *


async def get_specific_data():
    url_json = await Fetcher.get('https://res.cloudinary.com/sivadass/raw/upload/v1535817394/json/products.json')
    data_json = json.loads(url_json)
    for data in list(data for data in data_json if data['category'] == 'fruits'):
        print(json.dumps(data, indent=2))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_specific_data())