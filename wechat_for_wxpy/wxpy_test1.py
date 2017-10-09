# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-08-24
    
"""

from wxpy import *


bot = Bot(cache_path=True, console_qr=True)

# 给机器人自己发送消息
bot.self.send('Hello World!')
# 给文件传输助手发送消息
bot.file_helper.send('Hello World!')

# 查找昵称为'乙醚。'的好友
my_friend = bot.friends().search(u'Jason')[0]
# <Friend: 乙醚。>
# 发送文本
# my_friend.send('Hello, WeChat!')
# 发送图片
# my_friend.send_image('my_picture.png')
# # 发送视频
# my_friend.send_video('my_video.mov')
# # 发送文件
# my_friend.send_file('my_file.zip')
# # 以动态的方式发送图片
# my_friend.send('@img@my_picture.png')

# 获取所有类型的消息（好友消息、群聊、公众号，不包括任何自己发送的消息）
# 并将获得的消息打印到控制台
@bot.register()
def print_others(msg):
    print(msg)

# 回复 my_friend 发送的消息
@bot.register(my_friend)
def reply_my_friend(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)

# 自动接受新的好友请求
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈哈，我自动接受了你的好友请求,Hello, World!')

# 回复发送给自己的消息，可以使用这个方法来进行测试机器人而不影响到他人
@bot.register(bot.self, except_self=False)
def reply_self(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)

# 打印出所有群聊中@自己的文本消息，并自动回复相同内容
# 这条注册消息是我们构建群聊机器人的基础
@bot.register(Group, TEXT)
def print_group_msg(msg):
    if msg.is_at:
        print(msg)
        msg.reply(msg.text)

# 进入 Python 命令行、让程序保持运行
# 推荐使用
embed()

# 或者仅仅堵塞线程
# bot.join()




