# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/5 11:55
@Auth ： 陈不辣
@File ：demo6.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
获取当前目录下的所有 后缀 .py文件

'''
import  os
path=os.getcwd()
list=os.listdir(path)
print(list)
for name in list:
    if name.endswith(".py"):
        print(name)

listfile=os.walk(path) # generator object
print(listfile)
for dirpath,dirname,filename in listfile:
    print(dirpath)
    print(dirname)
    print(filename)
    print('-------->>>')