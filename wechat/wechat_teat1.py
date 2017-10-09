# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-04-24
    
"""
import itchat

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])

itchat.auto_login(hotReload=True)
itchat.run()