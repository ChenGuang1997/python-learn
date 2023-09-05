# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/9 14:25
@Auth ： 陈不辣
@File ：demo4-特点.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
1 字典种的key不能重复，但是value是可以重复的
2  字典中的元素是无序的
3 key不可变，可以动态伸缩大小
4 浪费内存，空间交换时间
'''
dict1={'name':'ls','name':'zs'}
print(dict1)
#  value 是可以重复的
dict2={'name':14,'sex':14,}
print(dict2)

#key不可变  字典根据key使用hash计算位置
'''
一个可哈希的对象必须是不可变的，因为 如果 key 不可变，那么它的 hash 值就不会改变，从而不会出现重复的 key。 
如果 key 是可变的，那么在改变对象后它的 hash 值也会发生变化，这时该对象再作为 key 就不能被正确访问了。
 因此，将字典中的key换成可 hash 的不可变类型（例如字符串、数字、元组，但不能是列表或字典）即可避免该错误。

'''
list1=[1,2,3,4]
d={list1:100}
print(d)