# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-12-14
    
"""
from app.utils.http import HttpHelper
import json
from urlparse2 import urlsplit


def get_token(keystone_url, user_name, password, domain, project_id):
    """
    根据用户名、密码、domian、租户id获取scoped token
    :param keystone_url:keystone地址
    :param user_name:用户名称
    :param domain:域信息
    :param password:用户密码
    :param project_id:租户ID
    :return:
    """
    # 请求参数
    # 请求参数 如果可以去到user id的话 则不需要 指定用户名字 和 domain id或者name
    params = '{"auth": {"identity": {"methods": ["password"],"password": {"user": {"name": "' + user_name +\
             '","domain":{"id":"' + domain + '"},"password": "' + password + '"}}},' \
             ' "scope": {"project": {"id": "' + str(project_id) + '"}}}}'
    request_url = keystone_url + '/v3/auth/tokens'
    # 调用请求方法
    status, headers, data = HttpHelper.post(url=request_url, params=str(params))
    # 处理返回结果
    print 'status——————————————'
    print status
    print 'headers——————————————'
    print headers
    print 'data——————————————'
    print data
    result = dict()
    result['status'] = status
    if status == 201:
        token_id = headers['x-subject-token']
        data = json.loads(data)
        catalogs = data['token']['catalog']
        for catalog in catalogs:
            key = catalog['name']
            values = catalog['endpoints']
            for value in values:
                if value['interface'] == 'internal':
                    url = urlsplit(value['url'])
                    result[key] = url.scheme + "://" + url.netloc
        result['token_id'] = token_id
    else:
        result['status'] = status
        result['msg'] = data
    print('GET SCOPED TOKEN:' + str(result['token_id']))
    return result


def main():
    # url = 'http://172.16.97.10:5000'
    # domain = 'fcda581fb51641108b90ac97a54cba2b'
    # user = 'admin'
    # password = 'Hangxinyun208'
    # # admin project
    # # project_id = '85b83ee39c6a4f80bcec2b99f3dc33af'
    # # project_id = 'f92ecd43c4ed442aaeaa02741a493c3e'
    # project_id = '85b83ee39c6a4f80bcec2b99f3dc33af'

    url = 'http://172.16.251.60:5000'
    domain = 'b26c3124de7c47e49d520f590d9223a8'
    user = 'admin'
    password = 'root'
    project_id = '6d5f1a62ebce4da0ab092dd4b954d72e'
    result = get_token(url, user, password, domain, project_id)
    print result


if __name__ == "__main__":
    main()


