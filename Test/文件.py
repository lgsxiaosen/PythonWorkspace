#!usr/bin/python
# -*- coding:utf-8 -*-

# 读取键盘输入
"""str = raw_input("请输入：")
print "你输入的是：", str """

# input函数

"""str = input("请输入：")  # [x*5 for x in range(2,10,2)],range(2,10,2)代表从2到10，间隔为2，不包括10
print "你输入的是：",str  """


# 打开文件
"""fo = open("foo.txt","wb")
fo.write("Python is a great language.\nYeah its great!!\n")
print "文件名：", fo.name
fo.close()
print "文件是否已关闭：", fo.closed
print "访问模式：", fo.mode
print "末尾是否强制加空格：", fo.softspace """


# 读取文件
"""fo = open("foo.txt", "r+")
str = fo.read(10)
print "读到的文件：", str
fo.close() """


# 删除文件
"""import os
os.remove("foo.txt") """

# 创建目录
import os
# os.mkdir("test")
# 删除目录
os.rmdir("test")













