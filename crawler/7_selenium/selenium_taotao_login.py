from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq

# 配置chrome 参数，加上登录可以实现数据的爬取

option = webdriver.ChromeOptions()
option.add_argument("--disable-blink-features=AutomationControlled")
option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以开发者模式

browser = webdriver.Chrome(options=option)
wait = WebDriverWait(browser, 10)


def search():
    browser.get('https://www.taobao.com')
    try:
        search_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
        )
        search_submit = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button'))
        )
    finally:
        pass
    search_input.send_keys('美食')
    search_submit.click()
    login()


def login():
    try:
        # login_before = wait.until(
        #     EC.presence_of_element_located(
        #         (By.CSS_SELECTOR, '#J_QRCodeLogin > div.login-links > a.forget-pwd.J_Quick2Static'))
        # )
        # login_before.click()

        username = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#fm-login-id'))
        )
        password = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#fm-login-password'))
        )
        username.send_keys('****')  # 用户名
        password.send_keys('****')  # 密码
        login_submit = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#login-form div.fm-btn> button.fm-button.fm-submit.password-login'))
        )
        login_submit.click()
    finally:
        pass


def main():
    search()


if __name__ == '__main__':
    main()
