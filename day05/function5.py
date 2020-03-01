#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 23:23
# @Author  : Roohom
# @Site    : 
# @File    : function5.py
# @Software: PyCharm
"""
作用域问题
"""

#局部作用域
def foo1():
    a = 5

foo1()

b = 10

def foo2():
    print(b)

foo2()

def foo3():
    b = 100 # 局部变量
    print(b)

foo3()
print(b)

def foo4():
    global b
    b = 200
    print(b)

foo4()
print(b)