# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/16 14:15
@Auth ： 陈不辣
@File ：demo2-导入模块.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
1  导入整个模块 导入模块的所有功能
给模块起名的时候尽量不与python自带的模块同名
import modename
from modulename import xxx

'''
# from  funmoudle import  demo1


# print(demo1.fblq(5))
'''
2 导入模块的某一个功能
from modulename import fun1,fun2
'''
# from  funmoudle.demo1 import  hnt


# print(hnt(4))

'''
3 指定别名  as   
import moudelename as  mn
from  moudel import xxx  as   yyy
'''
from funmoudle import demo1 as d1

print(d1.hnt(5))

'''
4  导入所有模块内容  * 
但一般最好不使用这种做法，有可能会造成函数名称冲突，还有会覆盖同名函数或者变量
要么使用导入整个模块，使用模块.函数调用 ，要么 使用别名
import abc * 
from abc import *


总结：
import module_name
import module_name as mn
from module_name import function_name
from module_name import function_name as fn
from module_name import *
'''
import math as mh

print(id(mh))
print(type(mh))
print(mh)
print(dir(mh))
print(mh.log10(1))
from math import pi

print(pi)
#  导入模块种某个具体的属性或者方法or函数
from  funmoudle.demo1 import  fblq
print(fblq(10))
