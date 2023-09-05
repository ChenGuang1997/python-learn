'''
在Python中，用方括号（[]）来表示列表，并用逗号来分隔其中的元素。

存储多个对象的引用，不同类型
'''
server=['dell','Powerleader','huawei']
server2=['1','2','3']
print(server)
# 这样打印会直接将整个列表带格式打印出来
# 指定索引取出对应列表位置的元素
print(server[0])
print(server[0].upper())
print(server[1].lower())
print(server[2].strip())
# 最后一个元素  使用索引 -1 倒数第二 -2 类推
print(server[-1])
# 修改
server[-1]='lianxiang'
print(server)
# 添加  列表中，首元素前，尾元素后
# 追加  append 在列表的末尾添加一个元素 或者整个列表  extend 在列表末尾至少添加一个元素(把整个列表的数据依次加入
server.append('IBM')
server.append(server2)
print(server)
server.extend(server2)
print(server)
#在列表中插入元素  insert(index,item)
server.insert(1,'zuzhuang')
print(server)


# -------------  clear() 清空所有元素
# 删除函数  删除列表元素  del  list[index]
server4=['aaa','bbbb','ccc','sss']
print(server4)
server4.clear()
print(server4)
del server[-1] #删除最后一个元素
print(server)
print('-------------------<<<<<')
del server[3]
print(server)
#  pop  弹栈  利用元素后随后在将其删除，也可以删除指定索引位置的元素Pop(index)
pop_num=server.pop()
print(server)
print(pop_num)
# 删除 任意位置元素
pop_num=server.pop(-1)
print(pop_num)
print(server)

'''
pop  和 del  语句都时删除元素  区别是  del不能利用删除的元素  pop会获取删除元素的值，我们可以获取到
'''
print('--------------------------------------------------')
''''
根据值删除元素，当某些时候不知元素位置，但知道元素值的时候可以使用,但删除时不可以利用
只能删除第一个值，不能一次删除重复的所有的值，只能利用for循环删除
'''
server2=['dell','Powerleader','huawei','lianx','dell']
r_num=server2.remove('lianx')  #打印为none 空值
print(r_num)
print(server2)
#  不能删除重复的所有的值，只删除第一个重复的值，不能删除不存在的元素
server2.remove('dell')
server2.append('huawei')
print(server2)
print(id(server2[0]))
print(id(server2[1]))
print(type(server2[0]))
print('----------------------.>>>>>')
#  以切片的形式删除列表元素
server3=['111','2222','3333','4444','5555']
server3[1:3]=[]  # 就是使用空列表替代
print(server3)
#  返回列表元素的索引  有重复元素时，只会返回第一个相关元素的索引
print(server2.index('huawei'))
# print(server2.index('qiling'))  未存在的元素则会报错

print(server2.index('huawei',0,2))  # 从范围位置内查找元素的索引
print('-------------使用内置函数list()c创建列表')
server3=list(['1','2','3','4'])
print(server3)
print('\n')
print('***************')
del server3  # 删除列表对象
print(server3)
