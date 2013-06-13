# -*- coding:utf8 -*-
__author__ = 'wuzheng.yk'
import re
import zipfile

r = re.compile(r'(\d+)$')
comment = []
nextNum = '90052'
f = zipfile.ZipFile('./channel.zip')

# while (1):
#     try:
#         # f = open('./%s.txt' % nextnothing)
#         data = f.read('%s.txt' % nextnothing)
#         print data
#         nextnothing = r.search(data).group()
#     except:
#         break

while (1):
    try:
        comment.append(f.getinfo('%s.txt' % nextNum).comment)
        nextNum = r.search(f.read('%s.txt' % nextNum)).group()
    except:
        print ''.join(comment)
        break

