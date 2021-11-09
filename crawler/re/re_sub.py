import re

# 利用正则表达式替换
content = '54aK54yr5oiR54ix5L2g'
content = re.sub('\d', '', content)
print(content)

html = '''<div id="songs-list">
<h2 class="title"> 经典⽼歌 </h2>
<p class="introduction">
经典⽼歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2"> ⼀路上有你 </li>
<li data-view="7_selenium">
<a href="/2.mp3" singer="任贤⻬齐"> 沧海⼀声笑 </a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="⻬齐秦"> 往事随⻛风 </a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond"> 光辉岁⽉ </a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳"> 记事本 </a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君"> 但愿⼈⻓长久 </a>
</li> </ul> </div>'''

# 直接将a 节点去掉，只留下⽂本，方便后续处理
html = re.sub('<a.*?>|</a>', '', html)
print(html)
results = re.findall('<li.*?>(.*?)</li>', html, re.S)
for queen_list in results:
    print(queen_list.strip())
