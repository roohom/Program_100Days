#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 22:26
# @Author  : Roohom
# @Site    : 
# @File    : getLen.py
# @Software: PyCharm

"""
定义一个point类和一个Line类，使用getLen方法获取两点构成直线的长度
"""
import math


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Line(object):
    def __init__(self, p1, p2):
        self.x = p1.get_x() - p2.get_x()
        self.y = p1.get_y() - p2.get_y()

        self.len = math.sqrt(self.x * self.x + self.y * self.y)

    def getLen(self):
        return self.len


p1 = Point(2, 3)
p2 = Point(5, 7)
line = Line(p1, p2)
print(line.getLen())
