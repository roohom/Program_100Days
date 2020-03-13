#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 21:56
# @Author  : Roohom
# @Site    : 
# @File    : car2.py
# @Software: PyCharm


class Car(object):

    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed

    def get_brand(self):
        return self._brand


    def set_brand(self, brand):
        self._brand = brand


    def get_max_speed(self):
        return self._max_speed


    def set_max_speed(self, max_speed):
        if max_speed < 0:
            raise ValueError('Invalid max speed for car')
        self._max_speed = max_speed

    def __str__(self):
        return 'Car:[品牌=%s, 最高时速=%d]' % (self._brand, self._max_speed)

    #用已有的修改器和访问器定义属性
    brand = property(get_brand, set_brand)
    max_speed = property(get_max_speed, set_max_speed)


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
