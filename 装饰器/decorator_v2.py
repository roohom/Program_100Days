#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 13:24
# @Author  : Roohom
# @Site    : 
# @File    : decorator_v2.py
# @Software: PyCharm
"""
decorator版本的decorator.py
"""


def outer(f):
    def inner():
        print("我是外函数的内函数1")
        f()
        print("我是外函数的内函数2")
    return inner


@outer                       # 此处使用的@outer的语法就是把outer作为了装饰器，等同于old = outer(old)
def old():
    print("我是一个普通函数")


old()








