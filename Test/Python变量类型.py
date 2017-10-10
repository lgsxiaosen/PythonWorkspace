# coding=utf-8
# !/usr/bin/python

#列表
'''list=['abc',57687,2.33,'sfs2','^%&*(']
tinylist=[123,'abc']
print list # 输出完整列表
print list[0] # 输出列表的第一个元素
print list[1:3] # 输出第二个至第三个的元素
print list[2:] # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2 # 输出列表两次
print list + tinylist # 打印组合的列表 '''

#Python元组
'''tuple=('abc',57687,2.33,'sfs2','^%&*(')
tinytuple=(123,'abc')
print tuple # 输出完整元组
print tuple[0] # 输出元组的第一个元素
print tuple[1:3] # 输出第二个至第三个的元素
print tuple[2:] # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2 # 输出元组两次
print tuple + tinytuple # 打印组合的元组'''

#元组不能更新
'''tuple=(24,'242fds',444)
list=[24,'242fds',444]
#tuple[2] = 1000 # 元组中是非法应用
list[2] = 1000 # 列表中是合法应用
print tuple
print list '''

#Python元字典
'''dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print dict['one']  # 输出键为'one' 的值
print dict[2]  # 输出键为 2 的值
print tinydict  # 输出完整的字典
print tinydict.keys()  # 输出所有键
print tinydict.values()  # 输出所有值
print dict '''