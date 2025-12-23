from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

option = webdriver.ChromeOptions()
option.add_argument("--disable-blink-features=AutomationControlled")
option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以开发者模式

browser = webdriver.Chrome(options=option)
wait = WebDriverWait(browser, 10)
KEYWORD = '茶叶'
MAX_PAGE = 1


# 现在已经不能这样操作了，会直接跳去登录
# 可以先进入首页，再进行搜索
def index_page(page):
    print('正在爬取第', page, '页')
    try:
        url = 'https://www.taobao.com/'
        browser.get(url)
        key_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#J_TSearchForm div.search-combobox-input-wrap> input')))

        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm div.search-button> button.btn-search.tb-bg')))
        key_input.clear()
        key_input.send_keys(KEYWORD)
        submit.click()

        # url = 'https://s.taobao.com/search?q=' + quote(
        #     KEYWORD) + '&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20210902&ie=utf8'
        # browser.get(url)
        #
        # if page > 1:
        #     input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form> input')))
        #     submit = wait.until(
        #         EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form> span.btn.J_Submit')))
        #
        #     input.clear()
        #     input.send_keys(page)
        #     submit.click()
        #
        # wait.until(
        #     EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active> span'), str(page)))
        # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.mitemlist .items .item')))
        #
        # get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()

    for item in items:
        product = {'image': item.find('.pic .img').attr('data-src'), 'price': item.find('.price').text(),
                   'deal': item.find('.deal-cnt').text(), 'title': item.find('.title').text(),
                   'shop': item.find('.shop').text(), 'location': item.find('.location').text()}
        print(product)


if __name__ == "__main__":
    for i in range(1, MAX_PAGE + 1):
        index_page(i)
