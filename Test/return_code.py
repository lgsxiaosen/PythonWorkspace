# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-02-03
    

"""

a = [1, 0, 1, 0, 0, 0]
count = 2
for i in range(count-1):
    if 0 in a:
        s = a.index(0)
        a[s] = 1
print a.index(0)
