import string
from typing import List
from urllib import request
from urllib.error import HTTPError, URLError

from lxml import etree
from lxml.etree import _ElementTree

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7,en-GB;q=0.6,de-DE;q=0.5,de;q=0.4',
    'Cache-Control': 'no-cache',
    'Host': 'www.douban.com',

}
url = 'https://www.douban.com/search?q=on+java&cat=1001'


def requestByUrllib():
    html = requestUrl()
    res = parseStructure(html)
    print(res)


def parseStructure(html: str) -> List:
    res = []
    if html is None or len(html) == 0:
        return res
    elementTree: _ElementTree = etree.HTML(html)
    resultList: List[_ElementTree] = elementTree.xpath('//div[@class="result-list"]/div[@class="result"]/div[2]/div')
    for result in resultList:
        item = dict()
        item['name'] = result.xpath('./h3/a/text()')[0]
        item[' book_url'] = result.xpath('./h3/a/@href')[0]
        item['rating_num'] = result.xpath('./div/span[2]/text()')[0]
        item['sub_title'] = result.xpath('./div/span[@class="subject-cast"]/text()')[0]
        res.append(item)

    return res


def requestUrl() -> str:
    req = request.Request(url=url, headers=headers, method='GET')
    try:
        response = request.urlopen(req)
    except HTTPError as e:
        print(e.reason, e.code, e.headers, sep='\n')
        return ''
    except URLError as e:
        print(e.reason)
        return ''
    html = response.read().decode('utf-8', "ignore")
    return html


if __name__ == '__main__':
    requestByUrllib()
