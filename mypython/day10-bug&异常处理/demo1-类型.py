# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/15 14:25
@Auth ： 陈不辣
@File ：demo1-类型.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
1
print 打印输出   #  注释部分代码
'''
'''
被动掉坑
        try:
        代码块
        expect:
        异常处理语句

'''
'''
常见类型：
1  zeroDivisionError
2  indexError  索引
3 KeyError   键位异常
4 NameError  未初始化
5 SyntaxError 语法问题
6 ValueError  取值，传参错误
'''
try:
    a=int(input("请输入除数："))
    b=int(input("请输入被除数："))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("错误，被除数不能为0！")
except ValueError:
    print("请输入数字")
'''
当需要处理多个异常时
try:
{代码块
except: exception1
except: exception2
excrpt: exception3 
先从子类异常开始 继承父类异常  防止遗漏的异常 增加 BaseExceptieon 
except BaseExpection as e:
    print(e)
'''