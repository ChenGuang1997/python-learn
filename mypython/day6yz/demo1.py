# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/7 14:50
@Auth ： 陈不辣
@File ：demo1.py
@IDE ：PyCharm
@addres:kyfq
"""
#  元组与列表类似，不同点是 元组种的元素确定后不能修改 且使用（）圆括号表示但表示元素时是一样

##  字符串和元组都是不可变序列 -- 没用增删改操作  可变序列增删改，对象地址不会改变
s='hello'
print(id(s))
print(s)
s=s+' world'
print(s)
print(id(s))



print('-=----------------')
cft=(3,5,4) #长方体长宽高
print(id(cft))
print('-------------')
print(cft)
print(cft[0])
print("长方体的体积是：",cft[0]*cft[1]*cft[2])
# 不能使用索引来改变元组的元素
#cft[0]=6
# print(cft)
# 只能重新赋值
cft=(6,10,8)
print(id((cft)))
print(cft)
print(type(cft))
##  第二种创建方式  tuple函数
t=tuple((11,22,33))
print(type(t))
print(t)
#  省略小括号
t2=19,22,33
print(type(t2))
print(t2)

'''
只包含一个元素的元组创建时，需要使用（）和 ，号  否则则会认为是数据本身的数据类型


'''
print('------------------<<<<')
t3=('Python')
#t3 仍然是字符串
print(t3)
print(type(t3))
t4=('Python2',)
print(type(t4))
print(t4)
