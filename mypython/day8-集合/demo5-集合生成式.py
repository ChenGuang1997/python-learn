# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/11 10:40
@Auth ： 陈不辣
@File ：demo5-集合生成式.py
@IDE ：PyCharm
@addres:kyfq
"""
#列表
list1=[i**3 for i in range(1,9)]
print(list1)

s1={i**2  for i in range(2,8) }
print(s1)
'''
总结：
可变，可重复，有序--列表[]   list
不可变，重复，有序---元组（）  tupple
无序，不可重复-----集合{}，set() 元素不可重复；字典{key:value},key不可重复(实际是set)  dict()


'''