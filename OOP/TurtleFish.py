#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 21:53
# @Author  : Roohom
# @Site    : shanghai
# @File    : TurtleFish.py
# @Software: PyCharm
import random as rd


class Turtle(object):
    def __init__(self):
        self.power = 100
        # 初始化乌龟的位置
        self.x = rd.randint(0, 10)
        self.y = rd.randint(0, 10)

    def move(self):
        new_x = rd.choice([-2, -1, 1, 2]) + self.x
        new_y = rd.choice([-2, -1, 1, 2]) + self.y

        # 　如果越出边界
        if new_x < 0:
            self.x = 0 - (new_x - 0)
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0 - (new_y - 0)
        elif new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y

        self.power -= 1
        return (self.x, self.y)

    def eat(self):
        self.power += 20
        if self.power >= 100:
            self.power = 100


class Fish(object):
    def __init__(self):
        self.x = rd.randint(0, 10)
        self.y = rd.randint(0, 10)

    def move(self):
        new_x = rd.choice([-1, 1]) + self.x
        new_y = rd.choice([-1, 1]) + self.y

        # 　如果越出边界
        if new_x < 0:
            self.x = 0 - (new_x - 0)
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0 - (new_y - 0)
        elif new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y

        return (self.x, self.y)


turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print("鱼被吃完了，游戏结束")
        break
    if not turtle.power:
        print("乌龟体力耗尽，游戏结束")
        break
    pos = turtle.move()
    # 迭代器中删除元素非常危险，经常出现意想不到的结果，因为迭代器是直接引用列表元素进行操作的
    # 这里只是使用列表的切片，一个浅拷贝来进行操作
    i = 0
    for each_fish in fish[:]:
        if each_fish.move() == pos:
            turtle.eat()
            fish.remove(each_fish)
            print("有一条鱼被吃了！")
