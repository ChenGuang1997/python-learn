# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/10 15:23
@Auth ： 陈不辣
@File ：demo2-集合操作.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
判断操作  in  not in 

'''
s1={111,222,333,444,555,666}
print(234 in s1)
print(999 not in s1)
print(111 in s1)
'''
add()  一次添加加一个元素  update()添加多个元素 可以添加列表 集合，元组,但不能添加字典，字典是不可哈希对象
'''
d1={'item1':11,'item2':'cg'}
s1.add(999)
print(s1)
#s1.add(d1)
#print(s1)
s1.update({555,777,888})
print(s1)
s1.update(['python','java','golang'],'golang')
print(s1)
s1.update((1,2,3))
print(s1)
'''
集合的删除操作
remove（）函数  discard()  pop()  clear()
'''
s1.remove(555)
print(s1)
# s1.remove(9999)   不存在的元素删除时 抛出keyerr
print(s1)
# discard()  一次删除一个元素，元素不存在时不抛出err 和 字典的get(key)类似
s1.discard('java')
s1.discard('c#')
print(s1)

# pop()  无参函数  一次删除任意一个集合元素 任意
s1.pop()
print(s1)
# s1.pop(10000)  TypeError: pop() takes no arguments (1 given)
# print(s1)

# clear（）  清除集合所有元素
s2={9,8,7,6,5,4,3}
print(s2,type(s2))
s2.clear()
print(s2)