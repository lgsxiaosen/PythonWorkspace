# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-10-17
    
"""
import datetime
import json
import time


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


previous_date = int(time.mktime(time.strptime(get_previous_date_time('07', '00', '00', False), '%Y-%m-%d %H:%M:%S')))

now = int(time.mktime(time.strptime(get_previous_date_time('07', '00', '00'), '%Y-%m-%d %H:%M:%S')))

print previous_date, now

# a = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(1508269113)))
# print a

a = [{u'res': u'71', u'client': u'b1715066738-1', u'start': u'1508375308', u'state': u'3', u'sche': u'backup_full',
      u'policy': u'LOG_b1715066738-1_1198', u'endtime': u'1508376114', u'type': u'0', u'id':
          {u'master': u'vm-vmw80337-t', u'jobId': u'1017'}}, {u'res': u'1', u'client': u'', u'start': u'1508375413',
        u'state': u'3', u'sche': u'', u'policy': u'', u'endtime': u'1508375413', u'type': u'17', u'id': {u'master':
      u'vm-vmw80337-t', u'jobId': u'1018'}}, {u'res': u'24', u'client':
    u'y1715063926-1', u'start': u'1508377871', u'state': u'5', u'sche': u'', u'policy': u'', u'endtime': u'0000000000',
    u'type': u'2', u'id': {u'master': u'vm-vmw80337-t', u'jobId': u'1019'}}, {u'res': u'24', u'client':
    u'y1715063926-1', u'start': u'1508377995', u'state': u'5', u'sche': u'', u'policy': u'', u'endtime':
    u'0000000000', u'type': u'2', u'id': {u'master': u'vm-vmw80337-t', u'jobId': u'1020'}},
     {u'res': u'1', u'client': u'', u'start': u'1508379611', u'state': u'3', u'sche': u'', u'policy': u'',
      u'endtime': u'1508379611', u'type': u'17', u'id': {u'master': u'vm-vmw80337-t', u'jobId': u'1030'}},
     {u'res': u'2800', u'client': u'w8415077017-1', u'start': u'1508380754', u'state': u'5', u'sche': u'',
      u'policy': u'', u'endtime': u'0000000000', u'type': u'2', u'id': {u'master': u'vm-vmw80337-t', u'jobId': u'1037'}},
     {u'res': u'71', u'client': u's8615057147-1', u'start': u'1508386405', u'state': u'3', u'sche': u'backup_incr',
      u'policy': u'LOG_s8615057147-1_1911', u'endtime': u'1508387212', u'type': u'0', u'id': {u'master': u'vm-vmw80337-t',
    u'jobId': u'1038'}}, {u'res': u'1', u'client': u'', u'start': u'1508386510', u'state': u'3', u'sche': u'',
    u'policy': u'', u'endtime': u'1508386510', u'type': u'17', u'id': {u'master': u'vm-vmw80337-t', u'jobId': u'1039'}},
     {u'res': u'71', u'client': u's8615057147-1', u'start': u'1508386713', u'state': u'3', u'sche': u'backup_incr',
      u'policy': u'LOG_s8615057147-1_2312', u'endtime': u'1508387518', u'type': u'0', u'id':
          {u'master': u'vm-vmw80337-t', u'jobId': u'1040'}}, {u'res': u'1', u'client': u'', u'start': u'1508391872',
    u'state': u'3', u'sche': u'', u'policy': u'', u'endtime': u'1508391873', u'type': u'17', u'id':
    {u'master': u'vm-vmw80337-t', u'jobId': u'1044'}}, {u'res': u'2800', u'client': u'w8415077017-1', u'start':
        u'1508393750', u'state': u'5', u'sche': u'', u'policy': u'', u'endtime': u'0000000000', u'type': u'2', u'id':
    {u'master': u'vm-vmw80337-t', u'jobId': u'1046'}}, {u'res': u'2800', u'client': u'w8415077017-1', u'start':
        u'1508394059', u'state': u'5', u'sche': u'', u'policy': u'', u'endtime': u'0000000000', u'type': u'2', u'id':
        {u'master': u'vm-vmw80337-t', u'jobId': u'1047'}}, {u'res': u'50', u'client': u'n2615065806-1', u'start':
        u'1508394772', u'state': u'2', u'sche': u'backup_full', u'policy': u'LOG_n2615065806-1_710', u'endtime':
        u'0000000000', u'type': u'0', u'id': {u'master': u'vm-vmw80337-t', u'jobId': u'1048'}}, {u'res': u'50',
    u'client': u'o2315065806-1', u'start': u'1508394878', u'state': u'2', u'sche': u'backup_full', u'policy':
u'LOG_o2315065806-1_709', u'endtime': u'0000000000', u'type': u'0', u'id': {u'master': u'vm-vmw80337-t', u'jobId':
    u'1049'}}, {u'res': u'50', u'client': u'w6315075331-1', u'start': u'1508395686', u'state': u'2', u'sche':
u'backup_full', u'policy': u'LOG_w6315075331-1_1062', u'endtime': u'0000000000', u'type': u'0', u'id':
        {u'master': u'vm-vmw80337-t', u'jobId': u'1050'}}]


b = json.dumps(a)
print b






