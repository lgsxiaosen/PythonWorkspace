#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 
    @create 2018-01-25 13:47
"""

a = [{"id": 1, "a": "w"}, {"id": 3, "a": "w"}, {"id": 13, "a": "w"}, {"id": 41, "a": "w"}]
b = []
for i in a:
    b.append(i['id'])

c = [i['id'] for i in a]
print c



