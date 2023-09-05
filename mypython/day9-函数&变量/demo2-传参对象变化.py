# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/11 11:34
@Auth ： 陈不辣
@File ：demo2-传参对象变化.py
@IDE ：PyCharm
@addres:kyfq
"""
def fun(arg1,arg2):
    print('arg1:',arg1)
    print('arg2:',arg2)
    arg1=1000
    arg2.append(int(999))
    print('arg1:', arg1)
    print('arg2:', arg2)

n1=99
n2=[22,33,44,55]
print(n1)
print(n2)
print('#####')
fun(n1,n2)
print(n1,n2)
'''
在函数调用中，如果是不可变对象，在函数体执行完后，不会影响实参的值，如n1
如果是可变对象，函数执行完后会影响原来的实参，如n2 列表是可变对象

'''