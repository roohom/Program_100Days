#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 21:09
# @Author  : Roohom
# @Site    : 
# @File    : findmax.py
# @Software: PyCharm
"""
找到列表中最大的数
"""

def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya']
    max_value = min_value = fruits[0]
    for index in  range(1, len(fruits)):
        if fruits[index] > max_value:
            max_value = fruits[index]
        elif fruits[index] < min_value:
            min_value = fruits[index]

    print('MAX:', max_value)
    print('MIN:', min_value)

if __name__ == '__main__':
    main()
