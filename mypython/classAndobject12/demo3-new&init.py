# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/30 15:11
@Auth ： 陈不辣
@File ：demo3-new&init.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
__new__() 用于创建对象
__init()__ 对创建的对象初始化
*args,**kwargs代表所有单字符串和列表对象. 也就是说新对象的取名没限制

'''
class Person(object):

    def __new__(cls, *args, **kwargs):
        print("①__new__()被调用了，cls的id值为{0}".format(id(cls)))
        obj=super().__new__(cls)
        print("②obj创建的对象的id为：{0}".format(id(obj)))
        return obj

    def __init__(self,name,age):
        print('⑥__init__被调用了,初始化了，id为{0}'.format(id(self)))
        self.name=name
        self.age=age

print('③object这个类对象的id为{0}.'.format(id(object)))
print('④person这个类对象的id为{0}.'.format(id(Person)))

# 创建person的实例对象
p1=Person("福贵",'60')
print('⑤p1这个Person类的实例对象的id：{0}'.format(id(p1)))
print('assssssss'+str(id(p1)))

