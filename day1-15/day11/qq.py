#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 21:14
# @Author  : Roohom
# @Site    : 
# @File    : qq.py
# @Software: PyCharm
"""
验证输入用户名和qq号是否有效并给出对应的提示信息
"""

import re

def main():
    username = input("请输入你的用户名：")
    qq = input('请输入QQ号：')
    # match函数的第一个参数是正则表达式字符串或正则表达式对象
    # 第二个函数要跟正则表达式做匹配的字符串对象
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)  # 匹配以字符串开始，是数字0-9或小写字母a-z或大写字母A-Z或_的任意字符，并是以字符串结尾的长度为6-20位的字符串
    if not m1:
        print("请输入有效的用户名。")

    m2 = re.match(r'^[1-9]\d{4,11}$',qq)              # 匹配以数字1-9以内任意数字的长度为4-11为的任意字符串
    if not m2:
        print("请输入有效的QQ号！")
    if m1 and m2:
        print("你输入的信息是有效的！")


if __name__ == '__main__':
    main()


