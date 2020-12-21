from lxml import etree

text = ''' 
<div> 
<Ul> 
<li class="item-0"><a href ="linkl. html">first item</a><a href ="link2.html">second item</a></li> 
<li class ="item-1"><a href ="link2.html">second item</a></li> 
<li class ="item-inactive"><a href="link3.html">third item</a></li> 
<li class ="item-1"><a href="link4.html"> fourth item</a></li> 
<li class ＝"item-0"＞＜a href＝"link5.html"＞fifth item</a></li>  
</ul> 
</div>
'''
htmlStr = etree.HTML(text)  # type:etree._Element
html = etree.tostring(htmlStr)
lis = htmlStr.xpath('//li')
# 这种方式不行，xpath 还是针对的是全局的数据，并不是lis[0] 下的节点
# hrefs = lis[0].xpath('/a')
print(html.decode('utf-8'))
