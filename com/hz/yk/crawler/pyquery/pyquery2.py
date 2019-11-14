html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
from pyquery import PyQuery as pq

doc = pq(html)
items = doc('.list')
# 直接父节点
container = items.parent()
print(type(container))
print('container:' + str(container))
# 所有父节点
parents = items.parents()
print(type(parents))
print('parents:' + str(parents))

# 想要筛选某个祖先节点的话，可以向 parents 方法传入 CSS 选择器，这样就会返回祖先节点中符合 CSS 选择器的节点
parent = items.parents('.wrap')
print('parents warp:' + str(parent))

li = doc('.list .item-0.active')
print('siblings:' + str(li.siblings()))

print('siblings active:' + str(li.siblings('.active')))
# 对于多个节点的结果，我们就需要遍历来获取了。例如，这里把每一个 li 节点进行遍历，需要调用 items 方法
lis = doc('li').items()
print('type list li:', type(lis))
for li in lis:
    print('li:', li, type(li))
