# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/1 15:44
@Auth ： 陈不辣
@File ：demo2.py
@IDE ：PyCharm
@addres:kyfq
"""
import  sys
import time
import urllib.request as  re
print(sys.getsizeof(22))
print(sys.getsizeof(99))
print(sys.getsizeof(True))
print(sys.getsizeof(False))
print(sys.getsizeof('张三'))

print('---------------')
#  时间相关
print(time.time())
print(time.localtime())

#  服务器请求
print(re.urlopen('https://fqmark.ai.pathologycn.com:6004/#/login').read())