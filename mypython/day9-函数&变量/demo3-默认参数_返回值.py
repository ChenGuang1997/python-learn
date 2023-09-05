# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/11 14:26
@Auth ： 陈不辣
@File ：demo3-默认参数_返回值.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
函数有多个返回值时，返回值以元组的形式呈现.如果只有一个数据时，则返回原类型返回值。
'''
def jo(arg1):
    j=[]
    o=[]
    for i in arg1:
        if i%2:
            o.append(i)
        else:
            j.append(i)

    return j,o

list1=[1,2,3,4,5,6,7,8,9,10]

print(jo(list1))
'''
函数定义默认值参数时，只有与默认值不符合时才会改变默认值参数

'''
def fun2(arg2,arg3=2):

    print(arg2%arg3)

fun2(10)
fun2(10,3)