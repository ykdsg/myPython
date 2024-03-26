import concurrent
import time
from concurrent.futures import BrokenExecutor, CancelledError

import requests
from requests import HTTPError, Timeout, TooManyRedirects


def download_one(url):
    resp = requests.get(url)
    print("read {} from {}".format(len(resp.content), url))


# 单线程方式
def download_all(sites):
    for site in sites:
        download_one(site)


# 多线程版下载
def download_all_futures(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_one, sites)


# 另一种写法的并发版本
def download_all_futures2(sites):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        to_do = []
        for site in sites:
            future = executor.submit(download_one, site)
            to_do.append(future)
        for future in concurrent.futures.as_completed(to_do):
            future.result()


# 并行版 ， 实际运行效果不如多线程
def download_all_futures_process(sites):
    # 函数 ProcessPoolExecutor() 表示创建进程池，使用多个进程（默认cpu 核数）并行的执行程序。
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(download_one, sites)


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
    try:
        start_time = time.perf_counter()
        download_all(sites)
        end_time = time.perf_counter()
        print("单线程版下载了{}个网站，耗时{}".format(len(sites), end_time - start_time))

        start_time = time.perf_counter()
        download_all_futures2(sites)
        end_time = time.perf_counter()
        print("另一个并发版下载了{}个网站，耗时{}".format(len(sites), end_time - start_time))

        start_time = time.perf_counter()
        download_all_futures(sites)
        end_time = time.perf_counter()
        print("多线程版下载了{}个网站，耗时{}".format(len(sites), end_time - start_time))

        start_time = time.perf_counter()
        download_all_futures_process(sites)
        end_time = time.perf_counter()
        print("并行版下载了{}个网站，耗时{}".format(len(sites), end_time - start_time))


    # 处理requests异常
    except ConnectionError as err:
        print(err)
    except HTTPError as err:
        print(err)
    except Timeout as err:
        print(err)
    # 处理futures异常
    except TooManyRedirects as err:
        print(err)
    except CancelledError as err:
        print(err)
    except TimeoutError as err:
        print(err)
    except BrokenExecutor as err:
        print(err)
    except:
        print("发生错误")
