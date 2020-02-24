#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 11:03
# @Author  : Roohom
# @Site    : 
# @File    : string.py
# @Software: PyCharm

"""
字符串常用操作
"""

str1 = 'hello, world！'
print('字符串的长度是：', len(str1))
print('单词首字母大写是：',str1.title())
print('字符串变大写：', str1.upper())
print('字符串是不是大写：',str1.isupper())
print('字符串是不是以hello开头：',str1.startswith('hello'))
print('字符串是不是以hello结尾:', str1.endswith('hello'))
print('字符串是不是以感叹号开头:', str1.startswith('!'))
print('字符串是不是以感叹号结尾:', str1.endswith('!'))

str2 = '- drh'
str3 = str1.title() + ' ' + str2.lower()
print(str3)


