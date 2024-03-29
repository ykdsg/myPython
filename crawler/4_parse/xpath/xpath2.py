from lxml import etree
from lxml.etree import _ElementTree

html: _ElementTree = etree.parse('./test.html', etree.HTMLParser())
print(type(html))
# 匹配所有节点
queen_list = html.xpath('//*')
# 获取所有子孙节点 选取li节点
queen_list = html.xpath('//li')
# 获取所有子节点 选取直接关联的a 节点
queen_list = html.xpath('//li/a')
print(queen_list)
print(queen_list[0])

# 用@进行属性匹配，注意中括号，用text()方法获取节点中的文本
queen_list = html.xpath('//li[@class="item-0"]/a/text()')
print(queen_list)

# 选取所有子孙节点的文本
queen_list = html.xpath('//li[@class="item-0"]//text()')
print(queen_list)
# 获取属性内容
queen_list = html.xpath('//li/a/@href')
print(queen_list)

text = '''<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
queen_list = html.xpath('//li[@class="li"]/a/text()')
# class是多值，所以这里没有匹配
print(queen_list)
# 多值需要使用contains
queen_list = html.xpath('//li[contains(@class,"li")]/a/text()')
print(queen_list)

# 多属性匹配，可以用 or mod,=,div 等
queen_list = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
print(queen_list)

# 使用索引获取特定次序的节点
html = etree.parse('./test.html', etree.HTMLParser())
queen_list = html.xpath('//li[2]/a/text()')
print(queen_list)
queen_list = html.xpath('//li[last()]/a/text()')
print(queen_list)
queen_list = html.xpath('//li[position()<3]/a/text()')
print(queen_list)
queen_list = html.xpath('//li[last()-2]/a/text()')
print(queen_list)

# 节点轴选择，包括获取子元素，兄弟元素，父元素，祖先元素
queen_list = html.xpath('//li[1]/ancestor::*')
print(queen_list)
queen_list = html.xpath('//li[1]/ancestor::div')
print(queen_list)
queen_list = html.xpath('//li[1]/ancestor::*')
print(queen_list)
queen_list = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(queen_list)
queen_list = html.xpath('//li[1]/descendant::span')
print(queen_list)
