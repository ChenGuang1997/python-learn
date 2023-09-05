# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/18 17:47
@Auth ： 陈不辣
@File ：demo4-类和静态方法-属性.py
@IDE ：PyCharm
@addres:kyfq
"""
''''
类方法 类属性 静态方法
类属性-定义在类中，方法之外的变量-被该类所有实例共享属性  
静态方法-类名直接调用的方法  @staticmethmod
类方法-类名直接调用  @classmethmod
'''


class Student():
    senor = '大学生'  # 类属性 所有对象共享

    def __init__(self, name, age, sex):  # self.xxx 为实体属性，将局部变量的值赋值给实体属性 self.xxx 任意命名，不必和局部变量一致，但为了区分
        self.name = name
        self.age = age
        self.sex = sex

    # 实例方法  传递实例的引用
    def read(self):
        print('读书')

    # 静态方法  不传参数
    @staticmethod  #  也是类名直接访问，无默认参数
    def sm():
        print('sm')

    # 类方法 必带cls形参  使用类名直接访问
    @classmethod
    def clsm(cls):
        print("cls方法")


stu1=Student('zs','18','male')
stu2=Student('ls','26','female')
print(stu1.senor)
print(stu2.senor)
#stu1.senor='打工仔'  ##  类属性由实例修改时，只对当前实例对象起作用
#print(stu2.senor)
#print(stu1.senor)
Student.senor='社会人'
## 类属性修改时，对所有实例共享
stu1.senor='boss'
print(stu1.senor)
print(stu2.senor)
print('-----------类方法')

Student.clsm()
print('-------===静态方法')
Student.sm()

