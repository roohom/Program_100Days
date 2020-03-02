#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 21:34
# @Author  : Roohom
# @Site    : 
# @File    : list3.py
# @Software: PyCharm

"""
生成列表
    - 用range创建数字列表
    - 生成表达式
    - 生成器
"""

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = a, a+b
        yield a

def main():
    lsit1 = list(range(1,11))
    print(lsit1)

    list2 = [x*x for x in range(1,11)]
    print(list2)

    list3 = [m + n for m in 'ABCDEFG' for n in '12345']
    print(list3)
    print(len(list3))

    #生成器（节省空间，但生成下一个元素需要花费时间）
    gen = (m + n for m in 'ABCDEFG' for n in '12345')
    print(gen)

    for elem in gen:
        print(elem, end=' ')
    print()

    gen = fib(20)
    print(gen)
    for elem in gen:
        print(elem, end=' ')

    print()


if __name__ == '__main__':
    main()





