# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/7 15:10
@Auth ： 陈不辣
@File ：getfile.py
@IDE ：PyCharm
@addres:kyfq
"""
import  os

def getfname():
    while True:
        fname=str(input('filename:'))
        if  os.path.exists(fname) is False:
            break
        print('%s 已经存在，请重试'% fname)

    return  fname

def getcontent():
    content=[]
    print('请输入内容，输入end表示结束')
    while True:
        line=str(input(">"))
        if line =='end':
            break
        content.append(line)
    return  content

def wfile(filename,content):
    with open(filename,'w') as fn:
        fn.writelines(content)


if __name__=='__main__':
    fname=getfname()
    content=getcontent()
    print(content)
    content1 = ['%s\n' % line for line in content]
    print(content1)
    wfile(fname,content1)





