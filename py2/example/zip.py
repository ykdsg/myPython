# -*- coding:utf8 -*-
__author__ = 'ykdsg'
L1 = [1,3,5,7]
L2 = [2,4,6,8]
#使用zip将两个列表合并
print 'hello'+str(zip(L1,L2))
for (a,b) in zip(L1,L2):
    print (a,b)
L3 = [2,4,6]
#当长度不一的时候，多余的被忽略
print zip(L1,L3)#extra items are ignored
#map则不会忽略，例如下例。当L1和L3长度不一的时候，
#会用第一个参数来填充。
print map(None,L1,L3)
#'zip' a dictionary
#使用zip来造出一个字典。
keys = ['name','age']
values = ['Chen Zhe ',22]
print dict(zip(keys,values))
