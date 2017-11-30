# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-11-28
    
"""
import random
import collections as coll

dicts = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
# dicts = {'A': 4, 'B': 3, 'C': 3, 'D': 0}

def get_random_algorithm(dict_):
    """
    gsliu 20171106
    随机算法，选择虚墙数量少的防火墙设备
    :param dict_: 设备id为key,设备下虚墙数量为value
    :return:
    """
    x = random.randint(0, sum(list(dict_.values())) - 1)
    sort_ = sorted(dict_.iteritems(), key=lambda o: o[1], reverse=False)
    sort_ = zip(*sort_)
    a = sorted(list(sort_[1]), reverse=True)
    for item, item_probability in enumerate(a):
        x -= item_probability
        if x < 0:
            return sort_[0][item]


def test(method):
    dict_num = coll.defaultdict(int)
    for i in range(10000):
        dict_num[eval(method)] += 1
    sums = sum([i for i in dict_num.values()])
    for ii, j in dict_num.items():
        print ii, j, '%.2f' % (float(j)/float(sums))


if __name__ == "__main__":
    test("get_random_algorithm({})".format(dicts))
    # print(list[weight_choice([5, 2, 2, 1])])
    # for i in range(15):
    #     print get_random_algorithm({'A': 5, 'B': 2, 'C': 0, 'D': 4})
