import time
import aiohttp
import requests
import asyncio
from bs4 import BeautifulSoup


# 豆瓣爬虫 同步版本
async def main():
    url = "https://movie.douban.com/cinema/later/beijin"
    heads = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}
    init_page = requests.get(url, headers=heads).content
    init_soup = BeautifulSoup(init_page, 'lxml')

    all_movies = init_soup.find('div', id='showing-soon')
    tasks = [asyncio.create_task(get_movie(each_movie, heads)) for each_movie in
             all_movies.find_all('div', class_="item")]
    for task in tasks:
        await task


async def get_movie(each_movie, heads):
    all_a_tag = each_movie.find_all('a')
    all_li_tag = each_movie.find_all('li')
    movie_name = all_a_tag[1].text
    url_to_fetch = all_a_tag[1]['href']
    movie_date = all_li_tag[0].text
    response_item = await get_detail(heads, url_to_fetch)
    soup_item = BeautifulSoup(response_item, 'lxml')
    img_tag = soup_item.find('img')
    print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))


# aiohttp 很重要，刚开始没使用这个，结果就会很慢
async def get_detail(header, url_to_fetch):
    async with aiohttp.ClientSession(
            headers=header, connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.get(url_to_fetch) as response:
            return await response.text()


start = time.time()
asyncio.run(main())
end1 = time.time()
print('cost {}'.format(end1 - start))
