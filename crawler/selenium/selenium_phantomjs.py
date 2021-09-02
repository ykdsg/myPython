from selenium import webdriver

# 使用无痕浏览器PhantomJS
browser = webdriver.PhantomJS()
browser.get('https://www.baidu.com')
print(browser.current_url)
