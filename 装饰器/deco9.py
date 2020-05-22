#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 21:33
# @Author  : Roohom
# @Site    : 
# @File    : deco9.py
# @Software: PyCharm
"""
用类方法去装饰函数
"""


class Outer():
    def newinner(func):
        Outer.func = func       # 把传递进来的函数定义为类方法
        return Outer.inner      # 同时返回一个新的类方法

    def inner():
        print("拿到联系方式...")
        Outer.func()
        print("渐渐熟悉起来...")


@Outer.newinner     # Outer.newinner(love) ==>  Outer.inner
def love():
    print("一起学习...")


love()   # love() ==> Outer.inner

















