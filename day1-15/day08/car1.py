#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 21:35
# @Author  : Roohom
# @Site    : 
# @File    : car1.py
# @Software: PyCharm
"""
属性的使用
    -访问器/修改器/删除器
    -使用__slots__对属性加以限制
"""


class Car(object):
    # 对brand 和 max_speed加以限制
    __slots__ = ('_brand', '_max_speed')

    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def max_speed(self):
        return self._max_speed

    @max_speed.setter
    def max_speed(self, max_speed):
        if max_speed < 0:
            raise ValueError('Invalid max speed for car')
        self._max_speed = max_speed

    def __str__(self):
        return 'Car:[品牌=%s, 最高时速=%d]' % (self._brand, self._max_speed)


car = Car('SUBARU', 300)
print(car)

#car.max_speed = -100

car.max_speed = 320
car.brand = "Benz"
print(car)

#属性的实现
print(Car.brand)
print(Car.brand.fget)
print(Car.brand.fset)
print(Car.brand.fdel)









