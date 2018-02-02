#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 
    @create 2018-02-01 16:42
"""
import datetime
import re

import dateutil.parser


st_time = '2017-11-02T00:37:38Z'
#
# st = dateutil.parser.parse(st_time)
# #将#将utc时间2017-12-21T04:57:42.000Z 转化为时间本地时间2017-12-21 12:57:42+00:00
# start_time =(st+datetime.timedelta(hours=8))
#
# date = datetime.datetime.strftime(start_time, "%Y-%m-%d %H:%M:%S")
#
# print start_time
#
# print date


def utc2localtime(utc_time):
    date_all = re.findall(r"(\d{4}[-/]\d{1,2}[-/]\d{1,2}[\sT]\d{1,2}:\d{1,2}:\d{1,2}Z?)", utc_time)
    if date_all:
        # 将字符串转换成日期格式
        date_time = dateutil.parser.parse(utc_time)
        # date_time = datetime.datetime.strptime(st_time, "%Y-%m-%dT%H:%M:%SZ")
        if 'T' and 'Z' in utc_time:
            # 将utc时间2017-12-21T04:57:42.000Z 转化为时间本地时间2017-12-21 12:57:42+00:00
            date_time = (date_time+datetime.timedelta(hours=8))
            # 格式化时间
        format_time = datetime.datetime.strftime(date_time, "%Y-%m-%d %H:%M:%S")
        return format_time
    else:
        return utc_time



print utc2localtime(st_time)
# print datetime.datetime.strptime(st_time, "%Y-%m-%dT%H:%M:%SZ")
print utc2localtime("2017-11-02 00:37:38")
print utc2localtime("2017/11/02T00:37:38Z")
print utc2localtime("2017-12-21T04:57:42.93Z")
print utc2localtime("2017/11/02 00:37:38")

# date_all = re.findall(r"(\d{4}[-/]\d{1,2}[-/]\d{1,2}[\sT]\d{1,2}:\d{1,2}:\d{1,2}Z?)", "2017/11/02 00:37:38")
# print date_all
