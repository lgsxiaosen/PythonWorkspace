#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 
    @create 2018-07-09 14:06
"""


def exchange_mask_int(mask_int):
    """
        转换子网掩码长度
    """
    bin_arr = ['0' for _ in range(32)]
    print(bin_arr)
    for i in range(mask_int):
        bin_arr[i] = '1'
    tmp_mask = [''.join(bin_arr[i * 8:i * 8 + 8]) for i in range(4)]
    tmp_mask = [str(int(tmp_str, 2)) for tmp_str in tmp_mask]
    return '.'.join(tmp_mask)


if __name__ == '__main__':
    a = exchange_mask_int(24)
    print(a)
