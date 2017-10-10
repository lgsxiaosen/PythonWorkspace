#!/usr/bin/python
#encoding=utf-8

#while 循环语句
'''count = 0
while (count < 9):    print 'The count is:', count;    count = count + 1;  print "Good bye!" '''

# continue 和 break 用法
'''i = 1
while i < 10:
    i += 1;
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print i         # 输出双数2、4、6、8、10

i = 1
while 1:            # 循环条件为1必定成立
    print i         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break '''

#无限循环
"""var = 1
while var == 1 :  # 该条件永远为true，循环将无限执行下去
   num = raw_input("Enter a number  :")
   print "You entered: ", num

print "Good bye!" """


#循环中使用else语句
'''count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5" '''

#返回通过指定字符连接序列中元素后生成的新字符串
'''str = "";
seq = ("a", "b", "c"); # 字符串序列
print str.join( seq ); '''


str = "http://www.w3cschool.cn/"

print str.partition("://s")



