# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/16 16:27
@Auth ： 陈不辣
@File ：demo3createobject.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
创建对象-对象的创建即是类的实例化-  张三=人类（）

'''


class Student():
    senor = '大学生'  # 类属性

    def __init__(self, name, age, sex):  # self.xxx 为实体属性，将局部变量的值赋值给实体属性 self.xxx 任意命名，不必和局部变量一致，但为了区分
        self.name = name
        self.age = age
        self.sex = sex

    def read(self):
        print('读书')


stu=Student('cg','26','male')
print(id(stu))
print(type(stu))
print(stu) # 实际输出对象的内存地址 16进制
#print(stu.name)
#print(stu.age)
stu.read()
Student.read(stu)
print(id(Student))
print(type(Student))
print(Student)
'''
实例方法的调用  
  1  ob.methmod()
  2  Classname.methmod(ob)
 
 例如  
 stu.read()   也可以这样表示  Student.read(stu)
'''