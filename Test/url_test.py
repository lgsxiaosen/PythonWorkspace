# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    lgs 2017-01-11
    
"""
import urllib2

request = urllib2.Request("http://tieba.baidu.com/f?kw=%E8%92%B8%E6%B1%BD%E6%98%86%E8%99%AB&red_tag=2820804220")
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
           'Referer': 'http://www.zhihu.com/articles'}
response = urllib2.urlopen(request)
print response.read()
