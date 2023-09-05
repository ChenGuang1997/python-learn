# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/25 15:29
@Auth ： 陈不辣
@File ：demo8-重写.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
子类可以重写父类中某个属性或者方法
子类重写后，可以在子类重写的方法中通过 super().xxx()调用父类中被重写的方法,但传入的实例是子类的实例
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
    def info(self):
        super().info()
        print("hello everyone")

#  super().info()
class Boss(Person):
    def __init__(self,name,age,car):
        super().__init__(name,age)
        self.car=car

employee1=employee('cg',26,'男')
boss1=Boss('sb','40','audi')
# 从父类继承
employee1.info()
per1=Person('ww','88')
per1.info()
