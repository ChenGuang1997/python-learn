'''

列表生成函数 list() 返回一个列表
界限函数 range() 返回一个范围区间的值 但不包含末位
'''
list3=list(range(1,9))
print(list3)
# rang (start,end,len)  开始 结束 递增长度 这个示例中，函数range()从1开始数，然后不断地加2，直到达到或超过终值（13）但不包含13
list4=list(range(1,13,2))
print(list4)
#  ** 表示 做幂运算 **2 平方 **3 立方 类推
list5=[]
for i in range(1,11,2):
    list5.append(i**2)
print(list5)
#  列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素
list6=[v**2 for v in range(1,11)]
print(list6)
'''
min max sum 列表操作函数
'''
print(min(list5))
print(max(list5))
print(sum(list5))
'''
sort()内置函数 会对源列表做出改变但不会自动还原  
 而stored函数则不会修改列表的原始顺序，会将源列表列表元素的值重新排序产生一个新的列表对象。原列表不会发生任何改变
'''
list3.sort(reverse=True)
print(list3,id(list3))
list7=sorted(list3)
print(list7,id(list7))
'''
列表生成式  列表解析   list=[i(元素表达式，可以不做任何操作) for i in rang(s,e)]
'''
list8=[i**2 for i in range(1,10)]
print(list8)