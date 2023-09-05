# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/15 13:45
@Auth ： 陈不辣
@File ：demo5-变量-递归函数.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
1  局部变量   只在函数内部生效的变量

'''
def fab (a,b,d):
    c=a+b+d  ## c  只在该函数体内生效
    return c
# print(c)  NameError: name 'c' is not defined
'''
2 全局变量  函数内外都能使用 函数使用后不改变变量
'''
age=26
def fun1(age):
    print('age is :',age)
    age+=1
fun1(age)
print(age)
'''
3  可以在函数内部定义全局变量  关键字  global
'''
def fun2():
    global name
    name='cg'
    print(name)
fun2()
print(name)

'''
递归 函数体调用自身+终止条件
缺点 占用内存，效率低  但代码简单
'''
#  经典汉诺塔
def hnt(n):
    if n==1:
        return n
    else:
        return hnt(n-1)*2+1
print(hnt(64))
#  阶乘
def jc(n):
    if n==1:
        return n
    else:
        return n*jc(n-1)
print(jc(6))
# 斐波拉契数列   1 1 2 3 5 8 13 21 ......n 求n时的和
def fblq(n):
    if n==1 or n==2:
        return 1
    else:
        return fblq(n-1)+fblq(n-2)
print(fblq(7))
