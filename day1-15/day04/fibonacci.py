#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 21:59
# @Author  : Roohom
# @Site    : 
# @File    : fibonacci.py
# @Software: PyCharm
"""
输出斐波那契数列的前20个数
"""


a = 0
b = 1
for i in range(20):
    a, b = b, a+b
    print(a)
