#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 21:52
# @Author  : Roohom
# @Site    : 
# @File    : while1.py
# @Software: PyCharm
"""
while循环实现1-100的求和
"""

sum = 0
num = 1

while(num<101):
    sum += num
    num += 1

print(sum)