# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    lgs 2016-12-20
    
"""

# a =[chr(i) for i in range(97,123)]
# b =[ i for i in range(1,27)]
# c = []
# for i in range(26):
#     print (str(b[i]) + a[i])
#     # print c

# args = {'size': '2,3,4,243,53,5,1,4', 'name': 'dsa,答复,fsaa'}
# a = [i for i in args['size'].split(',')]
# b = [i for i in args['name'].split(',')]
# for i in range(len(a)):
#     print a[i], b[i]

args = {'size': '2,3,4,243,53,5,1,4'}
a = [i for i in args['size'].split(',')]
for i in range(len(a)):
    args['sizes'] = a[i]
print args['sizes']



