#!/usr/bin/python
# encoding=utf

import time

import calendar

# 获取格式化时间
localtime = time.asctime(time.localtime(time.time()))
print "本地时间：" , localtime

# 格式化日期
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

# 获取某月日历
cal = calendar.month(2016,2)
print cal

call = calendar.calendar(2016,2,1,6,3)
print call




