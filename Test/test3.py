# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    lgs 2016-12-22
    
"""



info = list()
id_ = '1,2'
sizes = '3,4,5'
for i in id_.split(','):
        size = [i for i in sizes.split(',')]
        for k in range(len(size)):
                args = dict()
                args['order'] = '88'
                args['server_id'] = '99'
                args['cluster_id'] = '00'
                args['size'] = size[k]
                pp = args
                info.append(pp)
print info



