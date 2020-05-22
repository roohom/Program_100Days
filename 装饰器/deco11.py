#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 22:19
# @Author  : Roohom
# @Site    : 
# @File    : deco11.py
# @Software: PyCharm
"""
使用类装饰器去装饰类
"""


class kuozhan():
    def __call__(self, cls):
        # 把接收的类赋值给当前对象作为一个属性
        self.cls = cls
        # 返回一个函数
        return self.newfunc     # 不加括号

    def newfunc(self):
        self.cls.name = "我是在类装饰器中追加的新属性 name"
        self.cls.func2 = self.func2
        # 返回传递进来的类的实例化结果
        return self.cls()         # 加括号,返回的是实例

    def func2(self):
        print("我是在类装饰器中追加的新方法 func2")


@kuozhan()   #kuozhan ==> obj ==> @obj(Demo) ==> __call__() ==> obj ==> newfunc()
class Demo():
    def func(self):
        print("我是Demo类中定义的func方法")


obj = Demo()  # Demo() ==> newfunc() ==> obj
obj.func()
obj.func2()
print(obj.name)
print(obj)      # <__main__.Demo object at 0x0FB2B6D0>




















