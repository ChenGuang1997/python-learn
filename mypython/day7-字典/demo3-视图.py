# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/9 11:39
@Auth ： 陈不辣
@File ：demo3-视图.py
@IDE ：PyCharm
@addres:kyfq
"""
#  内置函数 keys()  获取字典的所有keys,返回的是一个列表
salary={'xs':10000,'qd':20000,'hd':30000,'operation':15000,}
mykey=salary.keys()
print(type(mykey))
print(mykey)
# 遍历字典时，会默认遍历所有的键
for i in salary:
    print(i,salary[i],salary.get(i))
#  内置函数  values()  获取所有values 返回的是一个列表
myvalues=salary.values()
print(type(myvalues))
print(myvalues)

#  内置函数  items()  获取字典所有的k-v 返回元组类型数据
myitems=salary.items()
print(myitems)
print(list(myitems))
