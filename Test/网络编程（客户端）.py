#!/usr/bin/python
# encoding=utf-8

import socket

s = socket.socket  # 创建socket对象
host = s.gethostname()  # 获取本地主机名
port = 12345  # 设置端口号

s.connect(host, port)
print s.recv(1024)
s.close()
