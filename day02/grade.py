#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 21:51
# @Author  : Roohom
# @Site    : 
# @File    : grade.py
# @Software: PyCharm
""""
百分制成绩转等级制成绩
90分以上，输出A
80分~89分，输出B
70分~79分，输出C
60分~69分，输出D
60分以下，输出E
"""

score = float(input("请输入你的成绩："))
if score > 90:
    grade = 'A'
elif 80 <= score <= 89:
    grade = 'B'
elif 70 <= score <= 79:
    grade = 'C'
elif 60 <= score <=69:
    grade = 'D'
else:
    grade = 'E'

print("你的成绩等次是：%c" % grade)
