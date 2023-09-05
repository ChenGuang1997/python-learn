# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/7 11:01
@Auth ： 陈不辣
@File ：demo2.py
@IDE ：PyCharm
@addres:kyfq
"""
# if  else elif 多选择分支结构
score=int(input("输入成绩:"))
if score>=90:
    print("优秀")
elif score>=70and score<90:
    print("良好")
elif score>=60and score<70:
    print("合格")
elif score>=0and score<60:
    print("不合格")
else:
    print("成绩不合规")

