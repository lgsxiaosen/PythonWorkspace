# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-05-26
    
"""
import datetime
import time

a = [{'c': "2017-05-26 10:03:45"}]
b = datetime.datetime.now()
c = datetime.datetime.strptime(a[0]['c'], "%Y-%m-%d %H:%M:%S")
# d = datetime.datetime(* c[:6])
d = b-c-datetime.timedelta(1)
t = d.days
print a[0]['c'], type(a[0]['c'])
print b, type(b)
print c, type(c)
print d, type(d)
print t, type(t)
print datetime.datetime.now() - datetime.timedelta(30)






