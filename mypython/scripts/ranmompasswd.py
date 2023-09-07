# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/7 11:41
@Auth ： 陈不辣
@File ：ranmompasswd.py
@IDE ：PyCharm
@addres:kyfq
"""
from random import  choice
import  string
string_choice=string.digits+string.ascii_letters

def getpasswd(n=10):
    passwd=''
    for i in range(n):
        ch_ar=choice(string_choice)
        passwd+=ch_ar

    return passwd

if '__name__'=='__main__':
    print(string_choice)
    print(getpasswd(9))
    print(getpasswd(11))
    print(getpasswd())