#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 21:39
# @Author  : Roohom
# @Site    : 
# @File    : for3.py
# @Software: PyCharm
"""
输入两个正整数计算其最大公约数和最小公倍数
"""

a = int(input('a='))
b = int(input('b='))
if a>b:
    (a,b)=(b,a)
for factor in range(a,0,-1):
    if a % factor == 0 and b % factor == 0:
        print("a和b的最大公约数是：%d" % factor)
        print("a和b的最小公倍数是：%d" % (a*b//factor))
        break