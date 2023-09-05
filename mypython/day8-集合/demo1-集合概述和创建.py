# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/10 14:21
@Auth ： 陈不辣
@File ：demo1-集合特点.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
集合和 列表 字典一样都属于可变序列
集合是没有value的字典  哈希表,不能有重复元素且无序 无序
'''
'''
创建方式 1  直接创建
'''
s1={'python','golang','c++','java'}
print(s1,type(s1))
'''
方式2  使用内置函数 set()  参数可以是 字符串，整型 列表 元组 range() 其他集合，或者空
'''
s2=set(range(1,8))
s3=set([1,3,5,7,9,9]) # 重复元素会去除
s4=set((2,4,6,8,10))
s5=set('学python')
s6=set(s1)
s7={}
print(s2,s3,s4,s5,s6,s7)
