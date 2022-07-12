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
    elementTree: _ElementTree = etree.HTML(html)
    resultList: List[_ElementTree] = elementTree.xpath('//div[@class="result-list"]/div[@class="result"]/div[2]/div')
    for result in resultList:
        name = result.xpath('./h3/a/text()')[0]
        book_url = result.xpath('./h3/a/@href')[0]
        rating_num = result.xpath('./div/span[2]/text()')[0]
        # 这个比较坑，页面上可能没有分数，导致这里需要判断下
        sub_title = result.xpath('./div/span[@class="subject-cast"]/text()')[0]
        print('name=%s,url=%s,rating_num=%s,sub_title=%s' % (name, book_url, rating_num, sub_title))


if __name__ == '__main__':
    requestByUrllib()
