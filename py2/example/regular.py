# -*- coding:utf8 -*-
import re

__author__ = 'ykdsg'

for i,j in re.findall(r"(\d)(\1*)", "11112222"):
    print (str(i)+"   "+str(j))