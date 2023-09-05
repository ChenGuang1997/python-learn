'''

切片  [start:end:step]  和rang类似 输出指定位置的元素
[0:3] 指从第一个到第三个位置的元素  步长默认为1
【start:end】 start->end-1    取出的为切片为新的列表对象

'''
list7=['zs','ls','ww','ql','zq']
print(list7[0:3])
print(list7[1:3])
# 没有指定 起始索引或者末尾索引 则自动填补第一位 （0）或者最后一位 （-1）
print(list7[:3])   # 同 [0:3]
print(list7[1:])  #同 [1:-1]
print(list7[:])  # 打印所有
print(list7[-2:])  #打印最后几位  [-n:]
print(list7[:3:2])
print('-----------')
print(list7[::-1])   # 逆转列表  step 为负数时 从尾部开始，相反的，正数时则是从首开始
print(list7[3::-1]) # 从尾部开始，正序索引为3的元素开始到首部
#  遍历切片
for item in list7[:3]:
    print(item)
#  复制列表
my_car=['bench','rus','lxus','audi']
his_cars=my_car[:]
print(his_cars,id(his_cars))
print(my_car,id(my_car))
you_cars=my_car[:3]
print(you_cars)
# 注意     his_cars=my_car，没有切片时  ×xxxxx    这表示为相同的两个列表对象，
his_cars2=my_car
print(my_car,id(my_car))
print(his_cars,id(his_cars2))
#  内存地址一样
my_car.append('byd') #两个列表是同一个对象，只是不同引用
print(his_cars2)
