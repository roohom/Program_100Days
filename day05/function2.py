#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 22:57
# @Author  : Roohom
# @Site    : 
# @File    : function2.py
# @Software: PyCharm

"""
函数的定义何使用- 计算最小公倍数和最大公约数
"""

def BGS(x, y):
    if x>y:
        (x,y) = (y,x)
    for factor in range(x,1,-1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1

def MIS(x,y):
    return x*y//BGS(x,y)


print(BGS(15,27))
print(MIS(15,27))