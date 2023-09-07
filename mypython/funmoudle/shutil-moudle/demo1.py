# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/7 14:03
@Auth ： 陈不辣
@File ：demo1.py
@IDE ：PyCharm
@addres:kyfq
"""
import  shutil
#shutil.copy('C:\\Users\\CG\\Desktop\\新建文件夹\\flannel.tar','C:\\Users\\CG\\Desktop') # cp /etc/a.txt /tmp/
#shutil.copy2('C:\\Users\\CG\\Desktop\\新建文件夹\\flannel.tar','C:\\Users\\CG\\Desktop') # 尽量保留所有元数据，文件属组属主，inode等
#shutil.rmtree('C:\\Users\\CG\\Desktop\\新建文件夹\\test2')
#shutil.rmtree('C:\\Users\\CG\\Desktop\\新建文件夹\\GXTC23023392.sdpc') # 不能删除文件
#shutil.make_archive('C:\\Users\\CG\\Desktop\\mypython','gztar','C:\\Users\\CG\\PycharmProjects\\mypython')

with open('b.txt', 'rb') as sfobj:
    with open('copyb.txt', 'wb') as dfobj:
        shutil.copyfileobj(sfobj, dfobj) # 拷贝文件对象
