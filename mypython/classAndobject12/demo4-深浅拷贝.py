# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/31 11:12
@Auth ： 陈不辣
@File ：demo4-深浅拷贝.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
①变量的赋值-对象相互赋值时，实质是同一个对象，但是是不同的引用而已
②浅拷贝-只拷贝源对象本身，源对象的子对象内容不拷贝，源对象和拷贝对象内的属性都引用同一个对象

③深拷贝-使用copy deepcopy模块 递归拷贝拷贝对象中的子对象。源对象和拷贝对象的子对象不相同
'''
class Cpu:
    pass
class Grapghic:
    pass
class Computer():
    def __init__(self,cpu,graphic):
        self.cpu=cpu
        self.graphic=graphic


# 变量赋值 引用是相同的
cpu1=Cpu()
cpu2=cpu1
print(id(cpu1),id(cpu2))
# 类的浅拷贝
print('------------------')
grp1=Grapghic()
computer1=Computer(cpu1,grp1)

import  copy
computer2=copy.copy(computer1)

# ②浅拷贝-只拷贝源对象本身，源对象的子对象内容不拷贝，源对象和拷贝对象内的属性都引用同一个对象
# comp2与comp1属于不同对象，但内部的属性仍然指向同一个对象 如cpu和graphic都指向同一个对象，但是comp1和comp2不是同一个对象

print(computer1,computer1.cpu,computer1.graphic)
print(computer2,computer2.cpu,computer2.graphic)

# 深拷贝-使用copy deepcopy模块 递归拷贝拷贝对象中的子对象。源对象和拷贝对象的子对象不相同
# 类似于 Linux软连接 硬链接  或者 副本和快捷方式的区别
print('-------------深拷贝')
computer3=copy.deepcopy(computer1)
print(computer1,computer1.cpu,computer1.graphic)
print(computer3,computer3.cpu,computer3.graphic)