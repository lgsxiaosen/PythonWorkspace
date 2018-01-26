#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 
    @create 2018-01-26 9:31
"""

a = [{"id": 1, "uuid": "wesa", "name": "123"}, {"id": 2, "uuid": "rty", "name": "456"},
     {"id": 3, "uuid": "3rts", "name": "789"}, {"id": 4, "uuid": "4yuj", "name": "345"}]

b = {i['id']: i['uuid'] for i in a}

print b