#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 22:03
# @Author  : Roohom
# @Site    : 
# @File    : multiprocess1.py
# @Software: PyCharm

"""
使用process类创建多个进程
"""

from multiprocessing import Process,Queue
from time import sleep


def sub_task(string, q):
    number = q.get()
    while number:
        print('%d: %s' % (number, string))
        sleep(0.001)
        number = q.get()

def main():
    q = Queue(10)
    for number in range(1,11):
        q.put(number)
    Process(target=sub_task, args=('Ping', q)).start()
    Process(target=sub_task, args=('Pong', q)).start()


if __name__ == '__main__':
    main()


