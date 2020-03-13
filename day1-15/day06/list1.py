#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 21:15
# @Author  : Roohom
# @Site    : 
# @File    : list1.py
# @Software: PyCharm
"""
定义和使用列表
    - 用下标访问元素
    - 添加元素
    - 删除元素
"""

def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    print(fruits)

    print(fruits[0])
    print(fruits[1])
    print(fruits[-1])
    print(fruits[-2])
    fruits[1] = 'apple'
    print(fruits)
    fruits.append('pitaya')
    fruits.insert(0, 'banana')
    print(fruits)
    del fruits[1]
    fruits.pop()
    fruits.pop(0)

    fruits.remove('apple')
    print(fruits)


if __name__ == '__main__':
    main()



