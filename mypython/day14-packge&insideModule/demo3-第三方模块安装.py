# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/1 16:09
@Auth ： 陈不辣
@File ：demo3-第三方模块安装.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
pip3 
pip3 install  moduelname
pip3 installl  module==version 
pip3 install module  -i  https://xxx.xxx.com  加速源

'''
import schedule as shd
import time
def joba():
    print('定时备份')

shd.every(3).seconds.do(joba)
i=5
while True:
    shd.run_pending()
    time.sleep(1)