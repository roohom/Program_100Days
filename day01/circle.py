#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 14:35
# @Author  : Roohom
# @Site    : 
# @File    : circle.py
# @Software: PyCharm

import math

radius = float(input("请输入圆的半径："))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print("此圆的周长是：%.2f " % perimeter)
print("此圆的面积是：%.2f " % area)

