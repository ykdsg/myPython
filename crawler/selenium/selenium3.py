import time

from selenium import webdriver

# 淘宝有反selenum的逻辑，点击的时候会跳去登录
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以开发者模式
# 节点交互
browser = webdriver.Chrome(options=chrome_option)
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_css_selector('.btn-search.tb-bg')
button.click()
