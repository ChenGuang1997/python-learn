# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/7 14:08
@Auth ： 陈不辣
@File ：demo6.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
for else   while else   
'''
for i in range(1,4):
    passwd=int(input("请输入密码："))
    if passwd==8888:
        print("密码正确")
        break
    else:
        print("密码错误")
        continue
else:
    print("密码输入错误三次")
#  while  else
a=0
while   a<4:
    print(a)
    a+=1
else:
    print("结束")
