from selenium import webdriver

# 根据 XPath、CSS 选择器等获取的方式
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third)
# 查找所有满足条件的节点，需要用 find_elements()
lis = browser.find_elements_by_css_selector('.service-bd li')
print(lis)
browser.close()
