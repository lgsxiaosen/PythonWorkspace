# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-05-27
    
"""
import logging

from Test3 import Test1 as t

a = t.comends

content = {'name': '你好', 'ip1': '发多少', 'ip2': '暗示法才', 'user': '撒反对', 'pwd': '沙发床',
           'nasip': '沙发'}
# a = a.format('2rez', '发多少', '暗示法才', '撒反对', '沙发床', '沙发')
a = a % content
logging.warning('====on_h3c_vfw_created====commands=%s' % a)


# print a






