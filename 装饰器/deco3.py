#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 13:35
# @Author  : Roohom
# @Site    : 
# @File    : deco3.py
# @Software: PyCharm

"""
利用装饰器
统计一个函数逇执行时间
"""
import time


# 定义一个统计函数执行时间的装饰器
# 注意return的不能加括号，加了就是调用了
def run_time(f):
    def inner():
        start = time.perf_counter()
        f()
        end = time.perf_counter() - start
        print("函数的调用执行时间为:{}".format(end))
    return inner


# 定义一个函数
@run_time
def func():
    for i in range(10):
        print(i, end=" ")
        time.sleep(1)


func()











