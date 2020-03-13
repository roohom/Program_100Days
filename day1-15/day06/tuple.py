#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 21:59
# @Author  : Roohom
# @Site    : 
# @File    : tuple.py
# @Software: PyCharm
"""
元组的定义和使用
"""

def main():
    t = ('drh', 38, True, '安徽滁州')
    print(t)
    print(t[0])
    print(t[1])
    print(t[2])
    print(t[3])

    for member in t:
        print(member)

    t = ('王大锤', 20, True, '云南昆明')
    print(t)

    person = list(t)
    print(person)

    person[0] = '李小龙'
    person[1] = 25
    print(person)

    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)

    print(fruits_list)
    print(fruits_tuple[1])


if __name__ == '__main__':
    main()