#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 20:56
# @Author  : Roohom
# @Site    : 
# @File    : deco7.py
# @Software: PyCharm
"""
带有参数的装饰器
"""


# 如果装饰器需要有参数，要给当前的装饰器套一个壳，用于接收装饰器的参数
def kuozhan(var):
    def outer(func):
        def inner1():
            print("红颜给了联系方式....")
            func()

        def inner2():
            print("介绍另一个红颜")
            func()
        # 装饰器壳的参数，可以用于在函数内做流程控制
        if var=="我":
            return inner1
        else:
            return inner2
    return outer


@kuozhan("你")
def love():
    print("找个红颜，一起学习")


love()





















