# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/16 14:13
@Auth ： 陈不辣
@File ：demo1-斐波拉契.py
@IDE ：PyCharm
@addres:kyfq
"""
def fblq(n):
    if n==1 or n==2:
        return  1
    else:
        return fblq(n-1)+fblq(n-2)

#print(fblq(4))
def  hnt(n):
    if n==1:
        return  1
    else:
        return 2*hnt(n-1)+1



if __name__ == '__main__':
    print(fblq(20))   # 这表示 该语句只在当前模块中运行 即在这个主程序中运行
    print(hnt(6))