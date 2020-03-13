#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 21:20
# @Author  : Roohom
# @Site    : 
# @File    : person2.py
# @Software: PyCharm


"""__slots__魔法"""

class Person(object):

    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 getter（）方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age < 19:
            print('%s正在玩球.' % self._name)
        else:
            print("%s正在玩球-.-" % self._name)


def main():
    person = Person('王大锤', 14)
    person.play()
    person._gender= '男'


if __name__ == '__main__':
    main()


