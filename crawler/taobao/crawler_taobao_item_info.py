import re
import xlwt
import time
import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import matplotlib

# 参考https://blog.csdn.net/qjk19940101/article/details/79593381 ，对爬虫和数据分析有一定的参考意义

# 计时开始
start = time.process_time()
# plist 为1-100页的URL的编号num
plist = []
for i in range(1, 101):
    j = 44 * (i - 1)
    plist.append(j)

listno = plist
datatmsp = pd.DataFrame(columns=[])

while True:
    def network_programming(num):
        url = 'https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E6%B2%99%E5%8F%91&suggest=history_1&_input_charset=utf-8&wq=shafa&suggest_query=shafa&source=suggest&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s=' + str(
            num)
        web = requests.get(url, headers=headers)
        web.encoding = 'utf-8'
        return web


    # 多线程
    def multithreading():
        # 每次爬取未爬取成功的页
        number = listno
        event = []

        with ThreadPoolExecutor(max_workers=10) as executor:
            for result in executor.map(network_programming, number, chunksize=10):
                event.append(result)

        return event


    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'

    }

    listpg = []
    event = multithreading()
    for i in event:
        json = re.findall(
            '"auctions":(.*?),"recommendAuctions"', i.text)
        if len(json):
            table = pd.read_json(json[0])
            datatmsp = pd.concat([datatmsp, table],
                                 axis=0, ignore_index=True)

            pg = re.findall(
                '"pageNum":(.*?),"p4pbottom_up"', i.text)[0]
            listpg.append(pg)

    lists = []
    for a in listpg:
        b = 44 * (int(a) - 1)
        lists.append(b)

    listn = listno

    listno = []
    for p in listn:
        if p not in lists:
            listno.append(p)

    if len(listno) == 0:
        break

datatmsp.to_excel('./data/datastmsp.xls', index=False)

end = time.process_time()
print("爬取完成，用时: ", end - start, 's')
