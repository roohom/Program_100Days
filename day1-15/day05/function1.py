#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 22:53
# @Author  : Roohom
# @Site    : 
# @File    : function1.py
# @Software: PyCharm
"""
函数的定义和使用-计算组合数C(7,3)
"""

def factorial(n):
    result = 1
    for num in range(1, n+1):
        result *= num

    return result

print(factorial(7//factorial(3)//factorial(4)))

