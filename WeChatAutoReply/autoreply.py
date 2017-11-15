# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-11-10
    
"""
import itchat
from itchat.content import TEXT
from itchat.content import *
import sys
import time
import re
import requests, json
# import aiml
import os


# When recieve the following msg types, trigger the auto replying.
@itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO], isFriendChat=True, isMpChat=True)
def text_reply(msg):
    global auto_reply, robort_reply, peer_list

    # The command signal of "[自动回复]"
    if msg['FromUserName'] == myUserName and msg['Content'] == u"开启自动回复":
        auto_reply = True
        itchat.send_msg(u"[自动回复]已经打开。\n", msg['FromUserName'])
    elif msg['FromUserName'] == myUserName and msg['Content'] == u"关闭自动回复":
        auto_reply = False
        itchat.send_msg(u"[自动回复]已经关闭。\n", msg['FromUserName'])
    # elif not msg['FromUserName'] == myUserName:
    else:
        if auto_reply is True:
            itchat.send_msg(u"[自动回复]您好，我现在有事不在，一会再和您联系。\n", msg['FromUserName'])
        else:
            '''
            For none-filehelper message,
            if recieve '= =', start robort replying.
            if recieve 'x x', stop robort replying.
            '''
            if msg['Content'] == u"= =":
                robort_reply = True
                peer_list.append(msg['ToUserName'])
                return
            elif msg['Content'] == u"x x":
                robort_reply = False
                peer_list.remove(msg['ToUserName'])
                return

            # Let Turing reply the msg.
            if robort_reply is True and msg['FromUserName'] in peer_list:
                # Sleep 1 second is not necessary. Just cheat human.
                time.sleep(1)

                cont = requests.get(
                    'http://www.tuling123.com/openapi/api?key=8edce3ce905a4c1dbb965e6b35c3834d&info=%s' % msg['Content']).content
                m = json.loads(cont)
                itchat.send(m['text'], msg['FromUserName'])
                if m['code'] == 200000:
                    itchat.send(m['url'], msg['FromUserName'])
                if m['code'] == 302000:
                    itchat.send(m['list'], msg['FromUserName'])
                if m['code'] == 308000:
                    itchat.send(m['list'], msg['FromUserName'])
    return


# Main
if __name__ == '__main__':
    # Set the hot login
    itchat.auto_login(hotReload=True)

    # Get your own UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    print myUserName
    auto_reply = False
    robort_reply = False
    peer_list = []

    itchat.run()


