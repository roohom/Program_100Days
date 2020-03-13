#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 22:06
# @Author  : Roohom
# @Site    : 
# @File    : tax.py
# @Software: PyCharm
"""
输入月收入和五险一金计算个人所得税
新个人所得税计算方式颁布前的计算方式
"""

salary = float(input("请输入你的本月收入："))
insurance = float(input("五险一金："))
diff = salary - insurance -3500
if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 1500:
    rate = 0.03
    deduction = 0
elif diff < 4500 :
    rate = 0.1
    deduction = 105
elif diff < 9000 :
    rate = 0.2
    deduction = 555
elif diff < 35000 :
    rate = 0.25
    deduction = 1005
elif diff < 55000 :
    rate = 0.3
    deduction = 2755
elif diff < 80000 :
    rate = 0.35
    deduction = 5505
else:
    rate = 0.45
    deduction = 13505

tax = abs(diff*rate - deduction)
print("个人所得税是：￥%.2f元" % tax)
print("实际到手工资是：￥%.2f元" % (diff + 3500 -tax))
