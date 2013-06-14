# -*- coding:utf8 -*-
# image 库的使用
__author__ = 'wuzheng.yk'
import re, Image

i = Image.open("oxygen.png") # http://www.pythonchallenge.com/pc/def/oxygen.png
print i.mode,i.size,i.format
row = [i.getpixel((x, 45)) for x in range(0, i.size[0], 7)]
ords = [r for r, g, b, a in row if r == g == b]

print "".join(map(chr, map(int, re.findall("\d+", "".join(map(chr, ords))))))