# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/5 10:26
@Auth ： 陈不辣
@File ：demo5.py
@IDE ：PyCharm
@addres:kyfq
"""
import  os.path
print(os.path.abspath('demo5.py'))
print(os.path.exists('demo5.py'),os.path.exists('demo8.py'))
print(os.path.join('C:\\Users\\CG\\Desktop','demo5.py'))
print(os.path.split("C:\\Users\\CG\\Desktop\\demo5.py")) # 将路径与文件名分开
print(os.path.splitext("demo5.py")) # 将文件名与扩展名分开
print(os.path.basename('C:\\Users\\CG\\Desktop\\demo5.py'))# 提取绝对路径下的文件名，截取文件名
print(os.path.dirname('C:\\Users\\CG\\Desktop\\demo5.py')) # 和basename相反，提取路径但不包括文件名
print(os.path.isdir('C:\\Users\\CG\\Desktop\\demo5.py')) #  判断路径是否存在
