#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 20:58
# @Author  : Roohom
# @Site    : 
# @File    : dict2.py
# @Software: PyCharm

"""
字典的常用操作
"""
def main():
    stu = {'name':'drh', 'age':22,'gender':'male'}
    print(stu)
    print(stu.keys())
    print(stu.values())
    print(stu.items())
    for elem in stu.items():
        print(elem)
        print(elem[0],elem[1])
    if 'age' in stu:
        stu['age']=20
    print(stu)
    print('-------------------',end='\n')
    stu.setdefault('score', 60)
    print(stu)
    print('-------------------',end='\n')
    stu.setdefault('score', 100)
    print(stu)
    print('-------------------',end='\n')
    stu['score'] = 100
    print(stu)


if __name__ == '__main__':
    main()

