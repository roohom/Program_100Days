#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 09:58
# @Author  : Roohom
# @Site    : 
# @File    : p02.py
# @Software: PyCharm


import p01
# 此句相当于把p01的代码全部粘贴到了这里，语句print("我是01模块,你现在导入我是想干嘛？")将会执行

stu = p01.Student("董咚", 22)
stu.say()
p01.sayHello()
