# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/7 13:47
@Auth ： 陈不辣
@File ：demo5.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
水仙花数  100-999
'''
for i in  range(100,999):
    g=i%10
    s=i//10%10
    b=i//100
    #print(g,s,b)
    sxh=g**3+s**3+b**3
    if i==sxh:
        print(i,"is 水仙花数字")
