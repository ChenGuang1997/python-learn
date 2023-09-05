# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/29 11:10
@Auth ： 陈不辣
@File ：demo9-object.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
object 类是所有类的父类，所有类都有object类的方法和属性
内置函数 dir() 查看指定对象的所有属性
__str__()  返回对于‘对象的描述’   输出实例的内存地址 例： <__main__.Student object at 0x000002701554BAC8>
'''
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return 'hello  world'
stu=Student('zs','20')
print(dir(stu))
#print(stu)
# 重写前：  <__main__.Student object at 0x000002701554BAC8>
# 重写__str()__ 方法后
print(stu)   #  str（）方法默认是输出实例的内存地址