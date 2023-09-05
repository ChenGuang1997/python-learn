# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/16 11:43
@Auth ： 陈不辣
@File ：demo3-tracebak模块.py
@IDE ：PyCharm
@addres:kyfq


"""
import  traceback
try:
    print('--------------------->>>')
    num=1/0
except:
    traceback.print_exc()