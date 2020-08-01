#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 21:37
# @Author  : Roohom
# @Site    : 上海
# @File    : TicketSystem.py
# @Software: PyCharm


class Ticket():
    def __init__(self, weekend=False, child=False):
        self.exp = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1

        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def cal_total(self, num):
            return self.exp * self.inc * self.discount * num


adult = Ticket()
child = Ticket(child=True)

print("两个成年人和一个小孩子平时的总价格是:{}".format(adult.cal_total(2)+child.cal_total(1)))