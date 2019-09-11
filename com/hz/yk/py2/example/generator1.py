# -*- coding:utf8 -*-
__author__ = 'wuzheng.yk'
def genMul2(N):
    for i in range(N):
        yield i * 2
for i in genMul2(5):print i