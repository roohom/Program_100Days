#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 13:17
# @Author  : Roohom
# @Site    : 
# @File    : decorator.py
# @Software: PyCharm
"""
装饰器的原理
"""


# 利用闭包，把函数当做参数传递，并且在函数内去调用传递近来的函数，并返回一个函数
# 定义外函数，接收一个函数作为参数
def outer(f):
    def inner():
        print("我是外函数的内函数1")
        f()
        print("我是外函数的内函数2")
    return inner


# 定义普通函数
def old():
    print("我是一个普通函数")


# old()作为普通函数直接调用

old = outer(old)  # outer返回inner函数，赋值给了old
old() # 此处调用old函数等同于调用了inner函数





