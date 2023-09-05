'''

打印整个列表  for循环  python代码缩进问题
'''
list2=['tct','jzx','xfs','myzh','zqg']
for algo in list2:
    print(algo)
    print(algo+' is good ')
print("总共5种算法")
# 缩进 导致的逻辑错误
print('--------------------')
for algo in list2:
    print(algo)
print(algo+' is good ')
print("总共5种算法")
'''
------  不必要的缩进
'''
'''
message="AAAAAAA"
  print(message)  报错   IndentationError: unexpected indent
'''
