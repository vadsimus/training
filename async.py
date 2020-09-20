import asyncio
import aiohttp
import requests
from time import time


def get_file(url):
    response = requests.get(url, allow_redirects=True)
    return response


def write_file(response):
    filename = response.url.split('/')[-1]
    with open(f'temp/{filename}', 'wb') as file:
        file.write(response.content)


def write_image(data):
    filename = f'file-{int(time() * 1000)}.jpeg'
    with open(f'temp/{filename}', 'wb') as file:
        file.write(data)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)


def main():
    url = 'https://loremflickr.com/320/240'
    for i in range(10):
        write_file(get_file(url))


async def main2():
    url = 'https://loremflickr.com/320/240'
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time()
    asyncio.run(main2())
    print(f'async:{time() - t0}')

    t0 = time()
    main()
    print(f'sync:{time() - t0}')
