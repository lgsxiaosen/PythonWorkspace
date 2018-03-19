#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 
    @create 2018-03-06 16:47
"""
import httplib
import time
import os

import httplib2

"""
通过网络时间修改本地时间
"""


def get_webservertime(host):
    # 使用httplib获取的时间会慢几分钟 故不使用此方法，改用httplib2

    # conn = httplib.HTTPConnection(host)
    # conn.request("GET", "/")
    # 添加代理
    conn = httplib.HTTPConnection('172.17.18.80', 8080)
    conn.request("GET", host)
    r=conn.getresponse()
    #r.getheaders() #获取所有的http头
    ts=  r.getheader('date') #获取http头date部分
    #将GMT时间转换成北京时间
    ltime= time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
    print(ltime)
    ttime=time.localtime(time.mktime(ltime)+8*60*60)
    print(ttime)
    dat="date %u-%02u-%02u"%(ttime.tm_year,ttime.tm_mon,ttime.tm_mday)
    tm="time %02u:%02u:%02u"%(ttime.tm_hour,ttime.tm_min,ttime.tm_sec)
    print (dat,tm)
    # os.system(dat)
    # os.system(tm)


def http2(url):
    # 没有代理
#     h = httplib2.Http()
    h = httplib2.Http(proxy_info=httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP, '172.17.18.80', 8080))
    status, result = h.request(method='GET', uri=url)
    date = status.get("date")
    print date
    ltime = time.strptime(date[5:25], "%d %b %Y %H:%M:%S")
    print(ltime)
    ttime = time.localtime(time.mktime(ltime) + 8 * 60 * 60)
    print(ttime)
    dat = "date %u-%02u-%02u" % (ttime.tm_year, ttime.tm_mon, ttime.tm_mday)
    tm = "time %02u:%02u:%02u" % (ttime.tm_hour, ttime.tm_min, ttime.tm_sec)
    print (dat, tm)
    os.system(dat)
    os.system(tm)


if __name__ == '__main__':
    # 使用httplib获取的时间会慢几分钟
    # get_webservertime('www.baidu.com')
    http2('http://www.baidu.com')

