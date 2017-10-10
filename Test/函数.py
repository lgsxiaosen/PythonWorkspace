#!/usr/bin/python
# encoding=utf-8


"""def change_me(my_list):
    my_list.append([1, 2, 3, 4])
    print "函数内取值：" , my_list
    return

my_list = [10, 20, 30]
change_me(my_list)
print "函数外取值：" , my_list """


'''def printme(str,str1):
    print str
    return

printme(str=12,str1=3) '''



# 不定长参数
"""def printinfo(str,*str1):
    print '输出：',str
    for var in str1:
        print var
    return

printinfo(10)
printinfo(32,53,54,21) """

# 局部变量和全局变量
"""total = 3
def sum(str1,str2):
    total=str1+str2
    print total
    return total

sum(12,20)
print total """


# 命名空间和作用域
money = 200
def addmoney():
    global money
    money = money + 1

print money
addmoney()
print money
























