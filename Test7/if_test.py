# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-10-10
    
"""


a = 1
b = None
c = "as"
d = ''

if not (a or b or c or d):
    print "YES1"
print a, b, c, d
print (a or b or c or d)
if not a or not b or not c or not d:
    print "YES2"
if b:
    print 213

if None in (a , b , c , d):
    print "have None"





