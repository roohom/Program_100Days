#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 14:54
# @Author  : Roohom
# @Site    : 
# @File    : v23.py
# @Software: PyCharm

"""
findall的使用
"""


import re

pattern = re.compile(r'\d+')
s = pattern.findall('i am 18 years old and 180cm high')

print(s) # 返回列表

s = pattern.finditer('i am 18 years old and 180cm high')
print(type(s))

for i in s:
    print(i.group())




