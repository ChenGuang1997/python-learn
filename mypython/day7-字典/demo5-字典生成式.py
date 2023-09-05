# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/9 15:00
@Auth ： 陈不辣
@File ：demo5-字典生成式.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
列表生成式  list[values for vlaues in range(n,m)]

zip(ob1,ob2)函数  将可迭代的对象作为参数，将对象中的元素打包成元组，返回这些元组组成的列表

且会以最少数量元素为主。组成相应数量的元组
'''
name=['tom','jierui','jack','spark']
time=[5,6,8,10,11]

job={name1:time1 for name1,time1 in zip(name,time)}
print(job)
