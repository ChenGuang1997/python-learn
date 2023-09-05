'''

sort  永久排序 排序后永久更改
'''
list1=['route','switch','netline','server','machine']
print(list1)
list1.sort()
print(list1)
# 逆向排序  reverse=True
list1.sort(reverse=True)
print(list1)
#  注意  print(list1.sort(reverse=True))  为空

'''
sorted  临时排序  也可以逆向排序 reserve
'''
print('------------------------')
list1=['route','switch','netline','server','machine']
print(sorted(list1))
#print(list1.soreted())
print(list1)

#  反转列表  reserve  对象调用，返回null,不返回值
list1.reverse()
print(list1)
print(list1.reverse())
# len 函数 获取列表长度
print(len(list1))