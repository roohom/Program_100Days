#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 22:04
# @Author  : Roohom
# @Site    : 
# @File    : palindrome.py
# @Software: PyCharm
"""
判断一个数是不是回文数
"""

num = int(input("请输入你的数："))
temp = num
num2 = 0
num3 = 0

while temp>9:
    num2 = temp % 10      # 用来保存输入的数得最后一位
    num2 *= 10            #将最后一位换成最高位
    num3 *= 10            #保存到最后一位和下一位相加，再上一位准备和后面得到的低位相加
    temp = temp//10       #保存原数经<取最低为>后剩下的其余位
    num3 = num2 + num3    #将数转换

num3 = temp+num3          #得到的数是原数的十倍，故除以十

if(num3 == num):
    print("是回文数！")
else:
    print("不是回文数!")

