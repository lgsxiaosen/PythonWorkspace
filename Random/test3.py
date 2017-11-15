# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-11-02
    
"""
# 以指定的概率获取元素 以一个列表为基准概率，从一个列表中随机获取元素

import random


def random_pick(dict_):
    # sums = float(sum(proportion_list))
    # pro = [list_ / sums for list_ in proportion_list]
    # cumulative_probability = 0.0
    # dict_ = dict(zip(source_list, proportion_list))
    print list(dict_.values())
    x = random.randint(0, sum(list(dict_.values())) - 1)
    sort_ = sorted(dict_.iteritems(), key=lambda o: o[1], reverse=False)
    # print sort_
    sort_ = zip(*sort_)
    # sort_[1].sort()
    # print sort_
    a = sorted(list(sort_[1]), reverse=True)
    # print a
    for item, item_probability in enumerate(a):
        # cumulative_probability += item_probability
        x -= item_probability
        if x < 0:
            return sort_[0][item]
    # return item


some_list = ['a', 'b', 'c', 'd']
probabilities = [2, 1, 6, 1]

for i in range(10):
    print random_pick(dict(zip(some_list, probabilities)))

print random_pick(dict(zip(some_list, probabilities)))

