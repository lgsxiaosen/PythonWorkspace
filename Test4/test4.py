# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-09-07
    
"""



list_ = []
aa = [{"name": "ds", "age": 54, "page": 3, "sex": "boy", "flag": True},
     {"name": "agfrews", "age": 4, "page": 33, "sex": "girl", "flag": False},
     {"name": "dfd", "age": 6, "page": 35, "sex": "boy", "flag": False},
     {"name": "adfs", "age": 235, "page": 36, "sex": "girl", "flag": True},
     {"name": "hj", "age": 465, "page": 73, "sex": "boy", "flag": False},
     {"name": "jhg", "age": 65, "page": 9, "sex": "girl", "flag": True},
     {"name": "alkls", "age": 234, "page": 656, "sex": "boy", "flag": False}]
for i in range(5):
    if i:
        for c in aa:
            dict_ = {}
            dict_['hello']=c['name'],
            dict_['asa']=c['age']
            list_.append(dict_)
print list_
