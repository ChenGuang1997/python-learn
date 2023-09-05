# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/4 15:18
@Auth ： 陈不辣
@File ：demo2.py
@IDE ：PyCharm
@addres:kyfq
"""
fil3=open('a.txt','w')
fil3.write('kyfq')
fil3.flush()
fil3.close()
fil3.write('666')
fil3.flush()
# ValueError: I/O operation on closed file. 管道已经关闭

