# -*- coding:utf8 -*-
__author__ = 'ykdsg'

#! /usr/bin/env python
'''''python challenge level 10
question url: http://www.pythonchallenge.com/pc/return/bull.html
answer url: http://www.pythonchallenge.com/pcc/return/5808.html
'''
#Look-and-say sequence的特殊数列。
# 这种数列是使用后一个数来描述前一个数，例如sequence.txt文件中的5个数字：11描述前一个数1为1个1,21描述前一个数11为2个1,
# 1211描述前一个数21为1个2,1个1,111221描述前一个数1211为1个1,1个2,2个1

#前一位数字，初始值是1
a = '1'
for i in xrange(30):
    #数字指针，从0开始
    pos = 0
    #用来存放计算出来的数字
    tmp = ''
    str_len = len(a)
    while pos < str_len:
        count = 1
        while pos + 1 < str_len and a[pos] == a[pos+1]:
            count += 1
            pos += 1

        tmp += '%d%s' % (count, a[pos])
        pos += 1

    a = tmp

print len(a)