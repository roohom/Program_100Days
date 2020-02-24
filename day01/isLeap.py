#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 14:26
# @Author  : Roohom
# @Site    : 
# @File    : isLeap.py
# @Software: PyCharm

"""
判断一年是不是闰年
"""

year = int(input("请输入你所要判断的年份： "))

isLeap = (year%4 == 0 and year%100!= 0 or year%400 ==0)
if(isLeap==True):
    print('{}'.format(year) + "年是闰年。")
else:
    print('{}'.format(year) + "年不是闰年。")
