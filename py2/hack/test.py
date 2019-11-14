# -*- coding:utf8 -*-
__author__ = 'ykdsg'
# import urllib2, urllib, socket
#
# url = "http://zhicall.com/login"
# socket.setdefaulttimeout(200)
# params = {"code": "justdoit", "password": "doit"}
# i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",
#              "Accept": "text/plain"}
# req = urllib2.Request(url, data=urllib.urlencode(params))
# content_stream = urllib2.urlopen(req)
#
# print content_stream.read()


import urllib2,urllib,sys
import threading

url = "http://zhicall.com/login"
search = urllib.urlencode([('code','hello')])
params = urllib.urlencode({"code":"a","password":"2"})
i_headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
             "Accept-Encoding":"gzip,deflate,sdch",
             "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
             "Cache-Control":"max-age=0",
             "Connection":"keep-alive",
             "Host":"zhicall.com",
             "Referer":"http://zhicall.com/",
}
req = urllib2.Request(url,data=params, headers=i_headers)
content_stream=urllib2.urlopen(req)
print  content_stream.read()


