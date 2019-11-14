from bs4 import BeautifulSoup

html = '''
<html><head><title>The dormouse's stroy</title></head>
<div>
    <Ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html"> fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
        </li>
        <p class="title" name="dromouse">
            Once upon a time there were three 
            <b>The Dormouse's story</b>
            <a href="http://test.com" class="sister" id="link2">Lacie</a>
        </p>
        <p class="story">...</P>
    </ul>
</div>'''
soup: BeautifulSoup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
# 获取title节点的文本
# print(soup.title.string)
# print(type(soup.title))
# print(soup.head)
# print(soup.p)
print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p['class'])
print(soup.p.string)
# 直接子节点
print(soup.p.contents)
print(soup.p.children)

for i, child in enumerate(soup.p.children):
    print(i, child)
