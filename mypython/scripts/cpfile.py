# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/7 11:23
@Auth ： 陈不辣
@File ：cpfile.py
@IDE ：PyCharm
@addres:kyfq
"""
import sys
# sys 系统模块
def copy(src_fname, dst_fname):
    src_fobj = open(src_fname, 'rb')
    dst_fobj = open(dst_fname, 'wb')

    while True:
        data = src_fobj.read(4096)
        if not data:
            break
        dst_fobj.write(data)

    src_fobj.close()
    dst_fobj.close()

copy(sys.argv[1], sys.argv[2])
# 执行方式
# linux: cpfile.py /etc/hosts /tmp/b.hosts
# windows python.exe 'D:\....'  'E:\....'
