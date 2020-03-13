#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 14:40
# @Author  : Roohom
# @Site    : 
# @File    : temperature.py
# @Software: PyCharm
"""
将华氏温度转化为摄氏温度
"""

F = float(input("请输入华氏温度:"))
C = (F - 32) / 1.8
print('%.2f华氏度 = %.1f摄氏度' % (F, C))