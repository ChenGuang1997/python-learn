# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/8 17:08
@Auth ： 陈不辣
@File ：demo1.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
在Python中，字典是一系列键—值对。每个键都与一个值相关联，你可以使用键来访问与之
相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将任何Python对
象用作字典中的值。 字典使用 {}  表示   访问则用 dict['key'] 访问该键对应的value

数据结构之一，是无序序列，可变序列 即 可以增删改查 
'''
person={'age':'26','sex':'male','height':'165cm','age':'28','age':'38'}
print('age is',person['age'],'sex is ',person['sex'])
# 多个键相同时，取最后那个键,且最后那个键覆盖前面的所有相同键

#使用内置函数 dict（）创建字典； key不需要加’‘，value是字符时需要加’‘
person2=dict(age=20,name='cg')
#items()  字典内置函数，获取字典的k-v并返回
for k,v in person2.items():
    print(k,v)
#  创建空字典  {}
person3={}
'''
字典k-v添加  
取值时使用['k'] 
'''
person['weight']='85kg'
person['job']='enginer'
print(person)
# '''  删除字典的元素
# 使用del 函数  del  dir['key']
del person['job']
print(person)
#  clear 内置函数  清空字典
person.clear()
print(person)


