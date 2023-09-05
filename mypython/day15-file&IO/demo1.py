# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/4 10:51
@Auth ： 陈不辣
@File ：demo1.py
@IDE ：PyCharm
@addres:kyfq
"""
file=open('note','r')
#print(file.readlines())
file.close()

file2=open('a.txt','r')
#file2.write('hello world')
file2.seek(5)
print(file2.read())
print(file2.tell())
file2.close()

file3=open('note2','a')
#file3.write('Python')
file3.close()

# 二进制读取文件  一般是非文本文件
src_file=open('桌面图标.ico','rb')
des_file=open('桌面图标2.ico','wb')
des_file.write(src_file.read())
src_file.close()
des_file.close()

