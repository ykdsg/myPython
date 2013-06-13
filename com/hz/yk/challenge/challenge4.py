# -*- coding:utf8 -*-
__author__ = 'wuzheng.yk'
import urllib2
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = "12345"
search = re.compile(" (\d*)$")
search_html = re.compile("\.html$")

for i in xrange(300):
    print "%s: " % nothing,
    line = urllib2.urlopen("%s%s" % (url, nothing)).read()
    print line
    # handle the solution (last) line
    if search_html.findall(line):
        break
    match = search.findall(line)
    if match:
    # next nothing
        nothing = match[0]
    else:
    # handle the divide by two line
        nothing = str(int(nothing) / 2)