# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/10 16:01
@Auth ： 陈不辣
@File ：demo3-集合间的关系.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
相等 子集 超集  两集合是否有交集
'''
'''
①判断集合相等  --  元素是否相等
'''
s1={1,2,3,5,7,9}
s2={1,2,3,5}
s3={1,2,3,5,7,8}
print(s1 == s2)
print(s3==s1)
print(s3!=s2)
'''
② 判断集合是否是另一个集合的子集 或者超集
子集  issubset()
超集  issuperset()
'''
print(s2.issubset(s3))
print(s2.issubset(s1))
print(s1.issuperset(s3))
print(s3.issuperset(s2))
#  ③  两集合是否没有交集  true 表示没有 false表示有
print(s3.isdisjoint(s1))
s4={100,200,300}
print(s3.isdisjoint(s4))