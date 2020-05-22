#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 21:54
# @Author  : Roohom
# @Site    : 
# @File    : deco10.py
# @Software: PyCharm
"""
类装饰器
使用函数去装饰类

@装饰器
class Demo():
    pass

装饰器给函数进行装饰，目的是不改变函数调用和代码的情况下给原函数增加了新的功能
装饰器给类进行装饰，目的是不改变类的定义和调用的情况下给类增加新的成员(属性或方法)
"""


# 定义函数，接收一个类，返回给修改后的类
def kuozhan(cls):
    def func2():
        print("我是在装饰器中定义的新方法func2")
    cls.func2 = func2     # 把刚才定义的方法赋值给类
    cls.name = "我是在装饰器中追加的新属性 name"

    # 返回时，把追加的类新成员的 类 返回
    return cls


# 通过一个函数装饰器，给类进行装饰，增加新的属性或者方法
@kuozhan     # kuozhan(Demo) ==> cls ==> Demo
class Demo():
    def func():
        print("我是demo中定义的func方法")


Demo.func()  # 此时再调用的Demo类是通过装饰器更新过的Demo类
Demo.func2()
print(Demo.name)












