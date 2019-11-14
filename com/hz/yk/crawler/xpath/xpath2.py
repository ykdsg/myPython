from lxml import etree
from lxml.etree import _ElementTree

html: _ElementTree = etree.parse('./test.html', etree.HTMLParser())
print(type(html))
# 匹配所有节点
result = html.xpath('//*')
# 获取所有子孙节点 选取li节点
result = html.xpath('//li')
# 获取所有子节点 选取直接关联的a 节点
result = html.xpath('//li/a')
print(result)
print(result[0])

# 用@进行属性匹配，注意中括号，用text()方法获取节点中的文本
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)

# 选取所有子孙节点的文本
result = html.xpath('//li[@class="item-0"]//text()')
print(result)
# 获取属性内容
result = html.xpath('//li/a/@href')
print(result)

text = '''<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[@class="li"]/a/text()')
# class是多值，所以这里没有匹配
print(result)
# 多值需要使用contains
result = html.xpath('//li[contains(@class,"li")]/a/text()')
print(result)

# 多属性匹配，可以用 or mod,=,div 等
result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
print(result)

# 使用索引获取特定次序的节点
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[2]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print(result)
result = html.xpath('//li[last()-2]/a/text()')
print(result)

# 节点轴选择，包括获取子元素，兄弟元素，父元素，祖先元素
result = html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
result = html.xpath('//li[1]/descendant::span')
print(result)
