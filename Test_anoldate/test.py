# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-10-11
    
"""
import pandas as pd


df = pd.read_csv('input_data.csv')
# print df.head()
# print df.tail()

# print df.columns
# print df.index
# print df.T
# print df.ix[:, 0].head()
print df.describe()



