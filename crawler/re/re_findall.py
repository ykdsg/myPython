import re

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
# 只是获取第⼀个内容，可以⽤ search ⽅法。当需要提取多个内容时，可以⽤ ﬁndall ⽅法
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(results)
print(type(results))

for queen_list in results:
    print(queen_list)
    print(queen_list[0], queen_list[1], queen_list[2])
