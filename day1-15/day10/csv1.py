#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 19:43
# @Author  : Roohom
# @Site    : 
# @File    : csv1.py
# @Software: PyCharm

"""
读取csv文件
"""
import csv

filename = 'example.csv'

try:
    with open(filename) as f:
        reader = csv.reader(f)
        data = list(reader)
except FileNotFoundError:
    print('无法打开文件：', filename)
else:
    for item in data:
        print('%-30s%-20s%-10s' % (item[0], item[1], item[2]))
