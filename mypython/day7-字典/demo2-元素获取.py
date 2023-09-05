# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/9 11:01
@Auth ： 陈不辣
@File ：demo2-元素获取.py
@IDE ：PyCharm
@addres:kyfq
"""
##  [] 取值  通过字典中存在的key获取对应的value 如果没有 对应的key则抛出keyERR异常

# get() 方法取值，不存在对应的key，则返回空 none
#  第一种 []
scores={'张三':100,'李四':99,'王五':80}
print(scores)
print(scores['李四'])
#print(scores['钱六'])
#  第二种 内置方法 get()
print(scores.get('张三'))
print(scores.get('钱六'))
# 可以指定返回的值
print(scores.get('钱六','不存在'))