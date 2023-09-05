# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/7 11:29
@Auth ： 陈不辣
@File ：demo4.py
@IDE ：PyCharm
@addres:kyfq
"""
# 循环分为  while for
# 求1-100奇数和
a=1
sum=0
while a<101:
    if a%2==0:
        sum+=a

    a+=1
print(sum)

sum2=0
for i in range(1,101):
    if  i%2 !=0:
       sum2+=i
print(sum2)
