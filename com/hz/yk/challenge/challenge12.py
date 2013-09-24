# -*- coding:utf8 -*-
__author__ = 'ykdsg'
f = open('evil2.gfx','rb')
content = f.read()
f.close()

for i in xrange(5):
    f = open('ch12-%d.jpg' % i, 'wb')
    f.write(content[i::5])
    f.close()