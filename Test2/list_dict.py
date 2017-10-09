# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-05-18
    
"""

list1 = [
    {'name': 'as', 'age': 2},
    {'name': 'asw', 'age': 4},
    {'name': 'asf', 'age': 5}
]
list2 = [
    {'name': 'as', 'age': 2},
    {'name': 'asw', 'age': 4}
]

for i in list1:
    for x in list2:
        if i['name'] != x['name'] and list2.index(x)+1 == len(list2):
            list2.append(i)
        if i['name'] == x['name']:
            break

print list1
print list2


