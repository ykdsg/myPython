import os
import time
from hashlib import md5
from multiprocessing.pool import Pool
from urllib.parse import urlencode

import requests

headers = {
    'Referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'sec-fetch-mode': 'cors',
    'X-Requested-With': 'XMLHttpRequest',
    'accept': 'application/json, text/javascript',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7_selenium,en-GB;q=0.6,de-DE;q=0.5,de;q=0.4',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'UM_distinctid=16bc06ff08c5d5-09dd51a8e1dc88-37647e05-13c680-16bc06ff08d787; csrftoken=9beb11f3d94237876f377359f709f3e8; tt_webid=6710034618089014797; CNZZDATA1259612802=288383582-1562300742-%7C1563947404; tt_webid=6710034618089014797; s_v_web_id=420513427e46c67a26c363869e43e42e; WEATHER_CITY=%E5%8C%97%E4%BA%AC; __tasessionId=bldyfntjb1568768956438',
    'pragma': 'no-cache',
    'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    'sec-fetch-site': 'same-origin',
    'x-requested-with': 'XMLHttpRequest',
}


def get_page(offset):
    timestamp = int(round(time.time() * 1000))
    params = {
        'aid': '24',
        'offset': offset,
        'app_name': 'web_search',
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'en_qc': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': timestamp
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(response.json())
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                yield {'image': image.get('url'),
                       'title': title
                       }


def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


GROUP_START = 0
GROUP_END = 2

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
