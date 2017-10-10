# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    lgs 2017-01-10
    
"""
# import datetime
#
# print u'你好'+'\n'+str(110)
#
# a = datetime.datetime.now() + datetime.timedelta(2)
# a = a.strftime("%Y-%m-%d %H:%M:%S")
# print a
import urllib

from flask import json

data = {"username":"a,b,d","password":123}
values = urllib.urlencode(data)
print values
url = "http://www.baidu.com"
geturl = url + "?" +values
print geturl

res_info = {"volume_size": 8, "logic_server_id": "1,2,3"}
uri = "http://10.220.43.204:5000/app/scheduler/vmware/volumeaddcheck?volume_size='%s'&logic_server_id=%s" \
      % (int(res_info['volume_size']), str(res_info['logic_server_id']))
uri1 = "http://10.220.43.204:5000/app/scheduler/vmware/volumeaddcheck?volume_size=%s&logic_server_id=%s" \
      % (int(res_info['volume_size']), str(res_info['logic_server_id']))
print uri
pr






