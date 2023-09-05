# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/7 11:07
@Auth ： 陈不辣
@File ：demo3.py
@IDE ：PyCharm
@addres:kyfq
"""
# 嵌套选择分支
a=input("请问你是会员吗")
if a=="y":
    print("请问你是年会员还是月会员")
    b=input("请输入会员级别：")
    if   b=='n':
            print("你是年度会员")
    elif b=='y':
        print("你是月会员")
    else:
        print("输入有误")
else:
    print("您不是会员")

