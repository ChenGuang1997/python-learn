# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/10 16:52
@Auth ： 陈不辣
@File ：demo4-集合的数学关系.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
交集 差集  并集 对冲集

'''
# ① 交集
s1={11,22,33,44,55,66,88}
s2={33,44,55,66,77}
print(s1.intersection(s2))
# 也可以使用 & 号表示交集函数 intersection
print(s1&s2)
#②  并集 合并两集合并去除重复元素  和  | 等价
print(s1.union(s2))
print(s1|s2)
print('--------------')
#③差集  difference()  等同于  - 号 原集合不会发生变化
print(s1.difference(s2))
print(s1-s2)
print(s2.difference(s1))
# ④对称差集  和交集相反 等同于 ^ 号
print(s1.symmetric_difference(s2))
print(s1^s2)
