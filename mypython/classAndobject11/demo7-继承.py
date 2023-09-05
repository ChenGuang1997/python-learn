# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/25 15:03
@Auth ： 陈不辣
@File ：demo7-继承.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
继承-提高代码复用 
没有父类-则默认继承object类
支持多继承
定义子类的时候，必须在构造函数中调用父类构造函数  super().__init__(x,y)
'''
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class employee(Person):
    def __init__(self,name,age,sex):
        super().__init__(name,age)
        self.sex=sex

class Boss(Person):
    def __init__(self,name,age,car):
        super().__init__(name,age)
        self.car=car

employee1=employee('cg',26,'男')
boss1=Boss('sb','40','audi')
# 从父类继承
employee1.info()
boss1.info()

#  多继承 一个类可以继承多个父类
class other(Person,Boss):
    pass