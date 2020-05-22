#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 21:18
# @Author  : Roohom
# @Site    : 
# @File    : deco8.py
# @Software: PyCharm
"""
类装饰器装饰函数
"""


class Outer():
    # 魔术方法：当把该类的对象当作函数调用时，自动触发obj()
    def __call__(self, func):
        self.func = func      # 把传进来的函数作为对象的成员方法
        return self.inner   # 返回一个函数

    # 在定义的需要返回的新方法中，进行装饰和处理
    def inner(self, who):
        print("拿到联系方式....")
        self.func(who)
        print("开始一起学习....")


@Outer()            # Outer() ==> obj   @obj ==> obj(love) ===>  __call__(love) ==> inner()
def love(who):
    print(f"{who}和红颜一起学习")


love('我')










