# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/29 17:26
@Auth ： 陈不辣
@File ：demo2-特殊属性.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
特殊属性 ： __dict__  获取类对象的方法或者实例对象的所有属性，返回字典

__class__  获取类对象或者实例对象的所属类型

__bases__  获取类对象或者实例对象的父类  返回元组
'''

class A:
    pass
class B:
    pass
class C(A,B):
    def  __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print("abc")

c=C('zs','33')
print(c.__dict__)
print(C.__dict__)

print('--------------------------')
print(c.__class__)
print(C.__class__)
print('bases 返回类继承的所有父类  base 返回继承的第一个父类，基类','mro,返回类的层次机构，与其他类的关系')
'''
__subclasses__ 返回子类的列表
'''
print('---------',C.__bases__)
print('---------,',C.__base__)
print('----------,',C.__mro__)
print('------',A.__subclasses__())
'''
特殊方法

'''
a=100
b=99
c=a+b
d=a.__add__(b)
print(d)
print(c)
'''
__add__()特殊方法  重写
'''
class Student:
    def __init__(self,name):
        self.name=name

    def __add__(self, other):
        return  self.name+other.name
    def __len__(self):
        return len(self.name)

s1=Student('zys')
s2=Student("ls")
print(s1+s2)
print(s1.__add__(s2))
#实现两个对象的加法运算
print('------------------------------------------------')
# __len__()    len()
l1=[1,2,3,4]
print(len(l1))
print(l1.__len__())
print(len(s1))
print(s1.__len__())