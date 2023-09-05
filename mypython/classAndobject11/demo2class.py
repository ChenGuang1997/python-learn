# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/16 16:01
@Auth ： 陈不辣
@File ：demo2class.py
@IDE ：PyCharm
@addres:kyfq
"""
class Student():
      senor='大学生' #类属性
      def __init__(self,name,age,sex): # self.xxx 为实体属性，将局部变量的值赋值给实体属性 self.xxx 任意命名，不必和局部变量一致，但为了区分
          self.name=name
          self.age=age
          self.sex=sex


#实例方法  传递实例的引用
      def read(self):
        print('读书')


# 静态方法  不传参数
      @staticmethod
      def sm():
       print('sm')
# 类方法 必带cls形参
      @classmethod
      def clsm(cls):
          print("cls方法")

'''  在类之外定义的称为函数  ，在类之内定义的称为方法'''


def play():
    print("打游戏")