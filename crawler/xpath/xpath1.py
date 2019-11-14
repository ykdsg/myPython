from lxml import etree

text = ''' 
<div> 
<Ul> 
<li class="item-0"><a href ="linkl. html">first item</a></li> 
<li class ="item-1">< a href ="link2.html">second item</a></li> 
<li class ="item-inactive">< a href="link3.html">third item</a></li> 
<li class ="item-1">< a href="link4.html"> fourth item</a></li> 
<li class ＝"item-0"＞＜ a href＝"link5.html"＞fifth item</a></li>  
</ul> 
</div>
'''
htmlStr = etree.HTML(text)
result = etree.tostring(htmlStr)

print(result.decode('utf-8'))
