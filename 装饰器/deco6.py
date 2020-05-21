#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 21:28
# @Author  : Roohom
# @Site    : 
# @File    : deco6.py
# @Software: PyCharm
"""
装饰带有多参数的函数
"""


def outer(func):
    def inner(who, name, *args, **kwargs):
        print("找到女知己，聊理想....")
        func(who, name, *args, **kwargs)
        print("约定一起学习.....")
    return inner


# 定义多参数的函数
@outer
def love(who, name, *args, **kwargs):
    print(f"{who}跟{name}一起学习...")
    print("一起探讨学习问题", args)
    print("读了几本书", kwargs)


love("xiaoai", "siri", "hotpot", "ice cream", "watermelon", "movie")

"""
love()  ===> inner()
        love(...)  ===> inner(...)
            inner(...)  ===> inner(...)
             
"""

























