# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    lgs 2016 -11 -14
    接收任意列表（或者列表的列表），在屏幕显示，一次显示一行，如果需要，嵌套列表可以缩进
"""


def print_lol(the_list, indent=False, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    # print("\t", end='') 适用于Python3
                    print('\t'),
            print(each_item)
