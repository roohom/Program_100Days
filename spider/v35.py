#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/10 22:19
# @Author  : Roohom
# @Site    : 
# @File    : v35.py
# @Software: PyCharm
"""
Python中正则模块re
使用步骤:
1. compile函数将正则表达式的字符串编译为一个pattern对象
2. 通过pattern对象的一些方法对文本进行匹配，匹配结果是一个match对象
3. 用match对象的方法，对结果进行操作



"""

import re
# \d表示数字
# +表示这个数字可以出现一次货多次

s = r"\d+"
# 返回pattern对象
pattern = re.compile(s)
# 返回一个match对象
m = pattern.match("one12twothree3")

print(type(m))
# 默认匹配从头开始，所以此次结果为none
print(m)  # None

m = pattern.match("one12twothree3", 3, 10) # 带位置参数，从3开始找到10

print(type(m))
# 默认匹配从头开始，所以此次结果为none
print(m)  # None
print(m.group()) # 把匹配到的打印出来

print(m.start(0)) # 从哪个位置开始

print(m.end(0)) # 从哪个位置结束
print(m.span(0)) # 范围是多少

