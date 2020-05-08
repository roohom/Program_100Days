#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 14:48
# @Author  : Roohom
# @Site    : 
# @File    : v22.py
# @Software: PyCharm

"""
search的使用
"""


import re

s = r'\d+'
pattern = re.compile(s)

# 参数表明搜查的起始范围
m = pattern.search('one12two34three56', 10, 40)
print(m.group())


