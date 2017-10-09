# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-08-21
    
"""
import time

import datetime


# def get_previous_date():
#     """
#     zhangxue 20170816获取当前时间前一天 格式 yyyy-mm-dd hh:mm:ss
#     :return:
#     """
#     now = datetime.datetime.now()
#     dayscount = datetime.timedelta(days=1)
#     dayto = now - dayscount
#     previous_date = dayto.strftime('%Y-%m-%d %H:%M:%S')
#     return previous_date
#
#
# def get_previous_date_time(hour, mint, sec):
#     """
#     zhangxue 20170816获取当前时间前一天 格式 yyyy-mm-dd hh:mm:ss
#     :return:
#     """
#     now = datetime.datetime.now()
#     dayscount = datetime.timedelta(days=1)
#     dayto = now - dayscount
#     previous_date = dayto.strftime('%Y-%m-%d {}:{}:{}'.format(hour, mint, sec))
#     return previous_date
#
#
# previous_date = int(time.mktime(time.strptime(get_previous_date_time('07','00','00'), '%Y-%m-%d %H:%M:%S')))
# print get_previous_date_time('07','00','00')
# print previous_date
#
#
# previous_date_ = int(time.mktime(time.strptime(get_previous_date(), '%Y-%m-%d %H:%M:%S')))
# print get_previous_date()
# print previous_date_


print time.time()


def get_previous_date_time(hour='%H', mint='%M', sec='%S', now_=True):
    """
    add by gsliu 获取前一天某一时间或者今天某一时间 参数为字符串格式
    :return:
    """
    now = datetime.datetime.now()
    if now_:
        previous_date = now.strftime('%Y-%m-%d {}:{}:{}'.format(hour, mint, sec))
    else:
        dayscount = datetime.timedelta(days=1)
        dayto = now - dayscount
        previous_date = dayto.strftime('%Y-%m-%d {}:{}:{}'.format(hour, mint, sec))
    return previous_date

now = int(time.mktime(time.strptime(get_previous_date_time('07', '00', '00'), '%Y-%m-%d %H:%M:%S')))
now_ = str(time.mktime(time.strptime(get_previous_date_time('07', '00', '00'), '%Y-%m-%d %H:%M:%S')))
print now
print now_
print str(now)

print get_previous_date_time('07','00','00')
print get_previous_date_time('07','00','00', False)
print get_previous_date_time()
print get_previous_date_time(now_=False)





