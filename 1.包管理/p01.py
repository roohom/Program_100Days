#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 09:53
# @Author  : Roohom
# @Site    : 
# @File    : p01.py
# @Software: PyCharm


class Student():
    def __init__(self, name="NoName", age=18):
        self.name= name
        self.age = age

    def say(self):
        print("My name is {}".format(self.name))


def sayHello():
    print("Hi, 你好我现在悔过自新重学Python！")


print("我是01模块,你现在导入我是想干嘛？")