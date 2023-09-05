# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/10 11:37
@Auth ： 陈不辣
@File ：demo2-空数据结构.py
@IDE ：PyCharm
@addres:kyfq
"""

l1=[]
l2=list()
t=()
t2=tuple()
d1={}
d2=dict()
print(type(l1),l2)
print(type(t),t2)
print(type(d1),d2)
'''
为什么要将元组设置不可变序列


1 同时操作对象时不加锁
2 元组中存储的时对象的引用，
  2.1 元组中对象本身是不可变对象（如元组，字符串），则不能在引用其他对象
  2.2 元组中的对象是可变对象，则可变对象的引用不可改变，但其数据可以改变
   2.2如下例子
'''
t3=(10,[20,30],40)
# 这个元组包含了整数和列表对象 列表是可变对象
print(id(t3),type(t3),t3)
# 改变可变对象（list）的数据
t3[1].append(50)
print(id(t3),type(t3),t3) # 列表的内存地址不变
# 修改元组内的元素
t3[1]=100
print(t3)
''' TypeError: 'tuple' object does not support item assignment   元组元素引用不可变，但元素的数据可以变。如上 不能将t3[1]位置的列表
修改为其他对象，但是可以改变列表内的数据
'''