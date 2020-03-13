#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 19:52
# @Author  : Roohom
# @Site    : 
# @File    : csv2.py
# @Software: PyCharm
"""
写入csv文件
"""
import csv


class Teacher(object):
    def __init__(self, name, age, title):
        self.__name = name
        self.__age = age
        self.__title = title
        self.__index = -1

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def title(self):
        return self.__title


filename = 'teacher.csv'
teachers = [Teacher('drh', 22, '学生'), Teacher('李白', 24, '刺客')]

try:
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for teacher in teachers:
            writer.writenow([teacher.name, teacher.age, teacher.title])
except BaseException as e:
    print("无法写入文件：", filename)
else:
    print('保存数据完成！')