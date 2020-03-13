#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 21:58
# @Author  : Roohom
# @Site    : 
# @File    : piecewise.py
# @Software: PyCharm
"""
分段函数求值
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""

x = int(input("请输入你所想要计算的数值x："))
if x > 1:
    value = x*3-5
elif -1<= x <=1:
    value = x+2
elif x < -1:
    value = x*5+3

print(value)
