# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-09-14
    
"""
import os

ALLOWED_EXTENSIONS = set(["xls", "xlsx", "csv", "et"])

file = "虚墙策略需要的参数.xlsx"
if '.' in file and file.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS:
    print file.rsplit('.', 1)[1]
print file.rsplit('.', 1)
print file.rsplit('.')
print file.rsplit('.')[-1]
print os.getcwd()




