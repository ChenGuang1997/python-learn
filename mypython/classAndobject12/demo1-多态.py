# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/29 15:41
@Auth ： 陈不辣
@File ：demo1-多态.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
多态 --在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法--一个父类-多个子类

静态语言多态的三个必要条件：
继承，
父类引用指向子类对象
方法必须重写

'''
class  Traffic(object):
    def __init__(self):
        pass
    def fuel(self):
        print("交通工具都要消耗能量")

class Bus(Traffic):
    pass
   # def  fuel(self):
    #    print("公交车用电")

class Car(Traffic):
    def fuel(self):
        print("汽车用汽油")

class Air(Traffic):
    def fuel(self):
        print("飞机用航空燃油")

class Person(object):
    def fuel(self):
        print("人消耗其他能量")

def fun(obj):
    obj.fuel()

fun(Car())
fun(Air())
fun(Bus())  # ，继承父类的方法 但未重写父类方法
fun(Person())

