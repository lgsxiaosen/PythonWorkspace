# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-09-18
    
"""
import random
import bisect

list = ['A', 'B', 'C', 'D']


def weight_choice(weight):
    """
    :param weight: list对应的权重序列
    :return:选取的值在原列表里的索引
    """
    weight_sum = []
    sum = 0
    for a in weight:
        sum += a
        weight_sum.append(sum)
    t = random.randint(0, sum - 1)
    # 返回t插入的位置
    return bisect.bisect_right(weight_sum, t)


if __name__ == "__main__":
    print(list[weight_choice([5, 2, 2, 1])])
