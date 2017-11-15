# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-10-11
    
"""
import pandas as pd


# s = pd.Series([1, 2, 3, 4])
# print s

a = {"name": ["Elliot", "Dave", "Jon"],
     "age": [12, 32, 22],
     "sex": ['man', 'woman', 'man']}
df = pd.DataFrame(a)
# print df
# print df.ix[0]
df['country'] = 'china'
print df




