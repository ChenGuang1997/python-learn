# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/24 16:34
@Auth ： 陈不辣
@File ：demo6-封装.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
面向对象三大属性--封装  安全性 python中没有修饰属性私有的关键字  可以使用 __属性  表示该属性仅在类内部能访问
'''
class Staff:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    def info(self):
        print(self.name,self.__salary)

sta1=Staff('zs','1000')
sta1.info()

# print(sta1.__salary)
# print(sta1.salary)
print(dir(sta1))
print(sta1._Staff__salary)  # 在类的外部可以通过  _classname__属性 调用