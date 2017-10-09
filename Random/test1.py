# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-09-18
    
"""
import random

list = ['A', 'B', 'C', 'D']


def weight_choice(list_, weight):
    """
    :param weight: list对应的权重序列
    :return:选取的值在原列表里的索引
    """
    t = random.randint(0, sum(weight) - 1)
    for i, val in enumerate(weight):
        t -= val
        if t < 0:
            return list_[i]


if __name__ == "__main__":
    # print(list[weight_choice([5, 2, 2, 1])])
    print weight_choice(['A', 'B', 'C', 'D'], [50, 2, 2, 1])