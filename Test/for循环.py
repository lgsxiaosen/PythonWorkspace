#!/usr/bin/python
# encoding=utf-8

# for循环，例
"""for letter in 'python': #第一个实例
    print '当前字母：',letter

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print '当前字母 :', fruit

print "Good bye!" """

# 通过序列索引迭代
# 函数 len() 返回列表的长度，即元素的个数。 range返回一个序列的数。
'''fruits = ['banana', 'apple',  'mango']
print len(fruits)
print range(len(fruits))
for index in range(len(fruits)):
    print index
    print '当前水果 :', fruits[index] '''

# 循环中使用else语句
for num in range(10, 20):  # 迭代 10 到 20 之间的数字
   for i in range(2, num): # 根据因子迭代
      if num % i == 0:      # 确定第一个因子
         j = num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num, i, j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'




