# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/7 14:15
@Auth ： 陈不辣
@File ：demo7.py
@IDE ：PyCharm
@addres:kyfq
"""
# 打印直角三角型
for i in range(1,11):
    for j in range(1,i+1):
        print("*",end='')
    print()


for n in  range(1,10):
    for  m in range(1,n+1):
        print(n,"*",m,'=',n*m,end="\t")

    print()
