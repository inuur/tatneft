import asyncio
import os
import time
import aiohttp


def write_file(data):
    with open(f'images/{time.time_ns()}.jpeg', 'wb') as f:
        f.write(data)


async def get_page_content(url: str, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_file(data)


async def get_web_pages_data(urls: list[str]):
    tasks = list()
    async with aiohttp.ClientSession() as session:
        for i, url in enumerate(urls):
            task = asyncio.ensure_future(
                get_page_content(url, session)
            )
            tasks.append(task)
            if i % 20 == 0:
                await asyncio.gather(*tasks)
                tasks = list()
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    if not os.path.exists('images'):
        os.mkdir('images')
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    urls = ['https://loremflickr.com/320/240'] * 100
    asyncio.run(get_web_pages_data(urls))
