#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 22:29
# @Author  : Roohom
# @Site    : 
# @File    : student.py
# @Software: PyCharm

"""
定义和使用学生类
"""

def foo():
    print('test')


class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s:' % (self.name, course_name))

    def watch_movie(self):
        if self.age<18:
            print('%s只能看《喜羊羊与灰太狼》' % self.name)
        else:
            print('%s正在看\"你懂的\"' % self.name)

def main():
    stu1 = Student('drh', 22)
    stu1.study('《python编程从小白到放弃》')
    stu1.watch_movie()
    stu2 = Student('小王', 12)
    stu2.study('《数学》')
    stu2.watch_movie()


if __name__ == '__main__':
    main()






