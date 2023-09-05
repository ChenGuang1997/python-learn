# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/22 16:36
@Auth ： 陈不辣
@File ：demo5-动态绑定属性和方法.py
@IDE ：PyCharm
@addres:kyfq
"""
class Ren():
      def __init__(self,name,age):
          self.name=name
          self.age=age

      def sleep(self):
          print(self.name+'要睡觉')


per1=Ren('张三','19')
per2=Ren('李四','26')

'''
动态属性绑定
'''
print('------------为per2绑定一个其他的属性---------------------')
print(per1.name,per1.age)
per2.gender='女' # 动态绑定属性
print(per2.name,per2.age,per2.gender)
'''
方法动态绑定
'''
per1.sleep()
per2.sleep()
print('-----------为per1绑定方法')
# 定义一个函数
def fly():
    print('我会飞')

per1.fly=fly
#ob.method=method()

per1.fly()
#per2.fly