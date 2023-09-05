# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/31 17:36
@Auth ： 陈不辣
@File ：demo2-main.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
以主程序运行
在模块（py文件）种，每个模块都定义了一个记录模块名称的变量 __name__ ,程序检查这个变量，以确定他们在哪个模块运行
如果一个模块不是被导入在其他模块运行，那么它可能在解释器的顶级模块中执行 顶级模块的 __name__变量的值威__main__
'''
from funmoudle import demo1
print(demo1.fblq(8))  # 里面会出现运行demo1产生的所有结果  但是 加入 __name__=='__main__'  表示只在主程序中运行

