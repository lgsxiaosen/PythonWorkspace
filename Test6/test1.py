# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-09-14
    
"""



a = 'sdas_dsaf_2'
b = a.split('_')
b[-1] = str(6)
a = '-'.join(b)
print a
print b
