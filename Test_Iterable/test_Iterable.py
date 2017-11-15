# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-10-23
    
"""
from collections import Iterable, Iterator

# print isinstance({}, Iterable)  # --> True
# print isinstance((), Iterable)  # --> True
# print isinstance(100, Iterable)  # --> False
# print isinstance('', Iterable)

print isinstance({}, Iterator)  # --> False
print isinstance((), Iterator) # --> False
print isinstance( (x for x in range(10)), Iterator)  # --> True
print isinstance('1234', Iterator)
print isinstance(12, Iterator)


