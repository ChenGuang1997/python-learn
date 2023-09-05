# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/7 10:08
@Auth ： 陈不辣
@File ：demo1.py
@IDE ：PyCharm
@addres:kyfq
"""
#单分支
money=1000
s=int(input("取款数："))
if money>=1000:
    money-=s
    print("取款成功","余额为：",money)

# 双分支  补充对象的布尔值   null 0  none  空列表，元组，字典，字符串 都表示false ,其他则为true
a=int(input("请输入："))
if a%2:
    print(a,"是奇数")
else:
    print(a,"是偶数")
