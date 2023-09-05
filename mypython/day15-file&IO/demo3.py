# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/4 15:29
@Auth ： 陈不辣
@File ：demo3.py
@IDE ：PyCharm
@addres:kyfq
"""
'''
  open(file,r) as file:  表示一个上下文对象  实现了 enter 和 exit方法
'''
'''
__enter__ 方法是一个在类中定义的特殊方法，用于在进入上下文管理器时执行一些操作。
它通常与 with 语句一起使用，用于初始化资源或执行其他必要的操作
在上面的示例中，我们定义了一个名为 MyResource 的类，并在其中实现了 __enter__ 和 __exit__ 两个特殊方法。

在 __enter__ 方法中，我们定义了进入上下文管理器时要执行的操作，这里只是简单地打印一条消息。

在 __exit__ 方法中，我们定义了离开上下文管理器时要执行的操作，这里也只是简单地打印一条消息。

然后，我们使用 with 语句创建了一个上下文管理器，并将其赋值给 file 变量。
在 with 语句块中，我们可以执行一些操作，这些操作将在进入和离开上下文管理器时执行相应的操作

'''
#  重写 上下文切换方法
class Mangenttxt(object):

    def __enter__(self):
        print("执行enter操作")
        return self
       #  注意 此处需要返回当前实例，若没有返回实例对象，则不能调用上下文切换时的其他函数
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("执行exit操作")

    def fun1(self):
        print('show 方法')


with Mangenttxt() as file: # --->>>  mt=Mangenttxt()
      file.fun1()
      #  无论是否产生异常，都会调用 exit()方法退出上下文管理器，释放资源   不需要手动的去关闭

with open('桌面图标.ico','rb') as src_file:
    with open('桌面图标.ico3','wb') as des_file:
        des_file.write(src_file.read())