# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/9 16:14
@Auth ： 陈不辣
@File ：demo6-嵌套.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
列表嵌套字典，字典嵌套列表，字典嵌套字典


'''
dict1={'name':14,'name2':15,'name3':16}
list1=[1,2,4,6,7,dict1]
print(list1)
print('---------------------->>')
list2=[11,22,33,44,55]
dict2={'item1':list1,'item2':list2,'item3':2023}
print(dict2.get('item1'))

print('--------------------<<<')
dict3={'item1':dict1,'item2':dict2}
print(dict3)
