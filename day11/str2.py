#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 22:09
# @Author  : Roohom
# @Site    : 
# @File    : str2.py
# @Software: PyCharm

"""
字符串的常用操作 - 实现字符串的倒转
"""

from io import StringIO


def reverse_str1(str):
    return str[::-1]


def reverse_str2(str):
    if len(str) <= 1:
        return str
    return reverse_str2(str[1:]) + str[0:1]


def reverse_str3(str):
    rstr = StringIO()
    str_len = len(str)
    for index in range(str_len-1, -1, -1):
        rstr.write(str[index])
    return rstr.getvalue()


def reverse_str4(str):
    return ''.join(str[index] for index in range(len(str)-1, -1, -1))


def reverse_str5(str):
    str_list = list(str)
    str_len = len(str)

    for i,j in zip(range(str_len //2), range(str_len-1, str_len//2, -1)):
        return ''.join(str_list)


if __name__ == '__main__':
    str = 'I love Python'
    print(reverse_str1(str))
    print(str)
    print(reverse_str2(str))
    print(str)
    print(reverse_str3(str))
    print(str)
    print(reverse_str4(str))
    print(str)
    print(reverse_str5(str))
    print(str)



