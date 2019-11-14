# -*- coding:utf8 -*-
__author__ = 'wuzheng.yk'
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1
f = fab(5)
print f.next()
for i in fab(5):
    print i