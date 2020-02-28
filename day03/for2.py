#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 21:29
# @Author  : Roohom
# @Site    : 
# @File    : for2.py
# @Software: PyCharm
"""
输入非负整数n，计算n！
"""

n = int(input('n= '))
result = 1
for x in range(1,n+1):
    result *= x

print(result)
