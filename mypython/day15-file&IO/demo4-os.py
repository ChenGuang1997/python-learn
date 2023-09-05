# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/4 16:42
@Auth ： 陈不辣
@File ：demo4.py
@IDE ：PyCharm
@addres:kyfq
"""
import  os
#os.system('python')  system 调用系统命令

#os.startfile('C:\\Users\\CG\\Desktop\\viewImg.jpg') # 打开系统文件，需要绝对路径
#
print(os.getcwd())
list=os.listdir('../day15-file&IO')
print(list)
#os.mkdir('newdir')  # 创建目录
#os.makedirs('a/b/c')创建多级目录
#os.rmdir('a') # 删除目录
#os.removedirs('a/b/c')  #  删除多级目录
os.chdir('C:\\Users\\CG\\Desktop')
path1=os.getcwd()
path2=os.listdir(path1)