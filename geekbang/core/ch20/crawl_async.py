import asyncio
import time


def logg(func):
    # 接受任意数量和类型的参数
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("cost:{}s".format(end - start))

    return wrapper


async def crawl_page(url):
    print('crawling{}'.format(url))
    sleep_time = int(url.split('_')[-1])
    # await 执行和 Python 正常执行是一样的，也就是说程序会阻塞在这里
    await asyncio.sleep(sleep_time)
    print('ok {}'.format(url))


async def main(urls):
    for url in urls:
        await crawl_page(url)


async def main2(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    for task in tasks:
        await task


async def main3(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    # *tasks 解包列表，将列表变成了函数的参数；与之对应的是， ** dict 将字典变成了函数的参数。
    await asyncio.gather(*tasks)


start = time.time()
asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
end1 = time.time()
print('cost {}'.format(end1 - start))
asyncio.run(main2(['url_1', 'url_2', 'url_3', 'url_4']))
end2 = time.time()
print('cost {}'.format(end2 - end1))
