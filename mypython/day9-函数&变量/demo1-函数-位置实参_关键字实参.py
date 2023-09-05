# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/11 11:00
@Auth ： 陈不辣
@File ：demo1-基本函数.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
1 代码复用
2 隐藏细节
3提高维护性
4 可读性方便
def fun_name (arg):
    函数体
    return 
'''
'''  一  位置实参'''
#  a  b  为形式参数
def fab (a,b,d):
    c=a+b+d
    return c
##  1  99  为实参 ，实际参数的值
result=fab(1,99,999)
print(result)
print('--------------##################')
'''   二  关键字实参   根据形参名称进行实际参数传递,但是位置形参需要在原指定位置且必须在关键字实参前面'''
result2=fab(99,b=10,d=999)
print(result2)
