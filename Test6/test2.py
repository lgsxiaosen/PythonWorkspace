# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-09-18
    
"""


a = {"sa": 8, "adsa": None, "sada": 0}
# print a
# b = [True if v else False for k, v in a.items()]
# print b
# print b[0]
if None in [v for k, v in a.items()]:
    print a
if None in a.values():
    print a







