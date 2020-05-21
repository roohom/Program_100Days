#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 21:10
# @Author  : Roohom
# @Site    : 
# @File    : deco5.py
# @Software: PyCharm

"""
对带有参数的函数进行装饰
"""


def outer(func):
    # 如果装饰带有参数的函数，需要在内函数中定义形参，并传递给调用的函数，因为调用原函数等于调用了内函数
    def inner(var):
        print("-------------")
        func(var)
        print("+++++++++++++")

    return inner


# 有参数的函数
@outer
def love(name):
    print("+>>>>{}>>>>>+".format(name))


love("nice") # love() ===> inner()   love("nice") ===> inner("nice")








