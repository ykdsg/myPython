# 异步网页下载
import asyncio
import concurrent
import multiprocessing
import time

import aiohttp


async def download_one(url):
    # 必须使用aiohttp 才能兼容 async
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print("read {} from {}".format(resp.content.total_bytes, url))


async def download_all(sites):
    tasks = [asyncio.create_task(download_one(site)) for site in sites]
    # 在 event loop 中运行tasks序列的所有任务
    await asyncio.gather(*tasks)


# 思考题 求列表中元素的整数平方和 常规版本
def cpu_bound(number):
    print("number={}, result={}".format(number, sum(i * i for i in range(number))))


def calculate_sums(numbers):
    for number in numbers:
        cpu_bound(number)


def calcuter_normal(numbers):
    start_time = time.perf_counter()
    calculate_sums(numbers)
    end_time = time.perf_counter()
    print("普通版本，耗时{}秒".format(end_time - start_time))


# 思考题 并行版本
def calculate_sums_future(numbers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(cpu_bound, numbers)


def calcuter_future(numbers):
    start_time = time.perf_counter()
    calculate_sums_future(numbers)
    end_time = time.perf_counter()
    print("多进程版本，耗时{}秒".format(end_time - start_time))


# 思考题的multiprocessing版本
def calculate_sums_multiprocessing(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)


def calcuter_multiprocessing(numbers):
    start_time = time.perf_counter()
    calculate_sums_multiprocessing(numbers)
    end_time = time.perf_counter()
    print("multiprocessing版本，耗时{}秒".format(end_time - start_time))


if __name__ == "__main__":
    sites = [
        'https://www.dapenti.com/blog/more.asp?name=xilei&id=177662',
        'https://www.dapenti.com/blog/more.asp?name=xilei&id=177663',
        'https://www.dapenti.com/blog/more.asp?name=xilei&id=177664',
        'https://www.dapenti.com/blog/more.asp?name=xilei&id=177665',
        'https://www.dapenti.com/blog/more.asp?name=xilei&id=177666',
        'https://www.dapenti.com/blog/more.asp?name=xilei&id=177667',
        'https://www.dapenti.com/blog/more.asp?name=xilei&id=177668',
        'https://www.dapenti.com/blog/more.asp?name=xilei&id=177669',
        'https://www.dapenti.com/blog/more.asp?name=xilei&id=177670',
        'https://www.dapenti.com/blog/more.asp?name=xilei&id=177671',
        'https://www.dapenti.com/blog/more.asp?name=xilei&id=177672',
        'https://www.dapenti.com/blog/more.asp?name=xilei&id=177673',
        'https://www.dapenti.com/blog/more.asp?name=xilei&id=177674',
        'https://www.dapenti.com/blog/more.asp?name=xilei&id=177675',
        'https://www.dapenti.com/blog/more.asp?name=xilei&id=177676',
        'https://www.dapenti.com/blog/more.asp?name=xilei&id=177677',
        'https://www.dapenti.com/blog/more.asp?name=xilei&id=177678',
    ]
    start_time = time.perf_counter()
    asyncio.run(download_all(sites))
    end_time = time.perf_counter()
    print("异步版下载了{}个网站，耗时{}".format(len(sites), end_time - start_time))

    # 思考题
    numbers = [1000000 + x for x in range(10)]
    calcuter_normal(numbers)
    calcuter_future(numbers)
    calcuter_multiprocessing(numbers)
