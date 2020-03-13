#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 23:02
# @Author  : Roohom
# @Site    : 
# @File    : guess.py
# @Software: PyCharm
"""
面向对象版的猜数字游戏
"""

from random import randint

class GuessMachine(object):

    def __init__(self):
        self._answer = None
        self._counter = None
        self._hint = None

    def reset(self):
        self._answer = randint(1, 100)
        self._counter = 0
        self._hint = None

    def guess(self, your_answer):
        self._counter += 1
        if your_answer > self._answer:
            self._hint = '小一点'
        elif your_answer < self._answer:
            self._hint = '大一点'
        elif your_answer == self._answer:
            self._hint = '恭喜你猜对了！'
            return True
        return False

    @property
    def counter(self):
        return self._counter

    @property
    def hint(self):
        return self._hint


if __name__ == '__main__':
    game = GuessMachine()
    play_again = True
    while play_again:
        game_over = False
        game.reset()
        while not game_over:
            your_answer = int(input("请输入你的答案："))
            game_over = game.guess(your_answer)
            print(game.hint)
        if game.counter > 7:
            print("请充值智商！")
        play_again = input("再玩一次？(yes|no)") == 'yes'