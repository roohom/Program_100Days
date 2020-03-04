#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 22:25
# @Author  : Roohom
# @Site    : 
# @File    : dependency.py
# @Software: PyCharm

"""
对象之间得依赖关系和运算符重载
"""


class Car(object):

    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed
        self._current_speed = 0

    @property
    def brand(self):
        return self._brand

    def accelerate(self, delta):
        self._current_speed += delta
        if self._current_speed > self._max_speed:
            self._current_speed = self._max_speed

    def brake(self):
        self._current_speed = 0

    def __str__(self):
        return '%s当前时速%d' % (self._brand, self._current_speed)


class Student(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    # 学生和车之间存在依赖关系 - 学生使用了汽车
    def drive(self, car):
        print("%s驾驶者%s欢快地在去学校的路上" % (self._name, car._brand))
        car.acclerate(30)
        print(car)
        car.acclerate(50)
        print(car)
        car.acclerate(50)
        print(car)

    def study(self, course_name):
        print('%正在学习%s.' % (self._name, course_name))

    def watch_dy(self):
        if self._age < 18:
            print('%s只能看喜羊羊' % self._name)
        else:
            print('%s正在上网课。' % self._name)

    # 重载小于（<）运算符
    def __gt__(self, other):
        return self.age < other._age


if __name__ == '__main__':
    stu1 = Student('drh', 22)
    stu1.study('Python编程从入门到放弃')
    stu1.watch_dy()
    stu2 = Student('大锤', 12)
    stu2.study('数学')
    stu2.watch_dy()

    car = Car('SUBARU', 300)
    stu2.drive(car)
    print(stu1 > stu2)
    print(stu1 < stu2)