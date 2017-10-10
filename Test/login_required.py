# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    lgs 2016 -11 -23
    验证用户登录的装饰器
    在调用函数前，先检查session里有没有用户。
    此后，我们只需将此装饰器加在每个需要验证登录的请求方法上即可
    加上@login_required
"""

from functools import wraps
from flask import session, abort, app


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            abort(401)
        return func(*args, **kwargs)

    return decorated_function

app.secret_key = '12345678'
