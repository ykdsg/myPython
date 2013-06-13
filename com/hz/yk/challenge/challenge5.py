# -*- coding:utf8 -*-
__author__ = 'wuzheng.yk'

import cPickle as p
import urllib2

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
line = urllib2.urlopen(url).read()
dataList = p.loads(line)
for elt in dataList:
    # print [e[1] * e[0] for e in elt]
    print "".join([e[1] * e[0] for e in elt])
print dataList