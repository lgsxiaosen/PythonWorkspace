# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-09-18
    
"""
import random


def weight_choice(list, weight):
    """
    :param list: 待选取序列
    :param weight: list对应的权重序列
    :return:选取的值
    """
    new_list = []
    for i, val in enumerate(list):
        new_list.extend(val * weight[i])
    return random.choice(new_list)


if __name__ == "__main__":
    print(weight_choice(['A', 'B', 'C', 'D'], [50, 2.7, 2, 1]))



