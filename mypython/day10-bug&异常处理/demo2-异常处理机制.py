# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/15 17:54
@Auth ： 陈不辣
@File ：demo2-异常处理机制.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
1 异常处理机制
try  except  else 机制
没有抛出异常则执行 else 内的代码块
否则执行 except

'''
try:
    a=int(input("请输入除数："))
    b=int(input("请输入被除数："))
    c=a/b
except ZeroDivisionError:
    print("错误，被除数不能为0！")
except ValueError:
    print("请输入数字")
else:
    print('结果是：',c)

'''
2  try  except  else finally 
无论发生什么异常 ，finally最后都会执行  释放try中的资源

'''