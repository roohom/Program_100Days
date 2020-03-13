#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 22:41
# @Author  : Roohom
# @Site    : 
# @File    : file2.py
# @Software: PyCharm
"""
读取圆周率文件判断其中是否包含自己的生日
"""

birth = input('请输入你的生日：')
with open('pi_million_digits.txt') as f:
    lines = f.readlines()
    pi_strong = ''
    for line in lines:
        pi_strong += line.strip()
    if birth in pi_strong:
        print('BINGO!')