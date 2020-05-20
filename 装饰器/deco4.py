#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 20:32
# @Author  : Roohom
# @Site    : 
# @File    : deco4.py
# @Software: PyCharm
"""
装饰器的嵌套

1. 普通装饰器的定义

"""


def outer(func):
    def inner():
        print("-----------")
        func()
        print("+++++++++++")
    return inner

# 使用一个装饰器的
# @outer
# def love():
#     print("+>>>>>>>>>>+")
#


def kuozhan(f):
    def kzinner():
        print("扩展1")
        f()
        print("扩展2")
    return kzinner


@kuozhan
@outer
def love():
    print("+>>>>>>>>>>+")


love()


"""
1. 先使用离得近的outer函数，装饰love函数，返回了一个inner函数
2. 再使用上面的kuozhan装饰器，装饰上一次返回的inner函数，又返回了kzinner函数

最后调用love函数的时候执行顺序

love = kzinner()
        =====> 扩展1
        =====> inner()  
                =====> ----------
                =====> love()
                =====> ++++++++++
                
        =====> 扩展2
"""
