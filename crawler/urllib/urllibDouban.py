import http
import re
from http.client import HTTPResponse
from urllib import request
from urllib.error import URLError, HTTPError

import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7,en-GB;q=0.6,de-DE;q=0.5,de;q=0.4',
    'Cache-Control': 'no-cache',
    'Host': 'www.douban.com',

}

url = 'https://www.douban.com/search?q=on+java&cat=1001'


def requestByUrllib():
    req = request.Request(url=url, headers=headers, method='GET')
    try:
        response = request.urlopen(req)
    except HTTPError as e:
        print(e.reason, e.code, e.headers, sep='\n')
        return
    except URLError as e:
        print(e.reason)
        return
    html = response.read().decode('utf-8', "ignore")
    print(html)

    # 正则表达式处理简单的结构还行，对于复杂结构还是会有一些莫名其妙的问题
    # 使用单个搜索search 的时候是ok的，但是使用findall 可能出不来
    result = re.search('<div class="title".*?href="(.*?)".*?>(.*?)</a>.*?<span class="rating_nums">(.*?)</span>', html,
                       re.S)
    print(result.group(1), result.group(2), result.group(3))

    # results = re.findall('<div class="title".*?href="(.*?)".*?>(.*?)</a>',
    #                      html, re.S)
    # for result in results:
    #     print(result)


def requestByRequests():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.text)


if __name__ == '__main__':
    requestByRequests()
    requestByUrllib()
