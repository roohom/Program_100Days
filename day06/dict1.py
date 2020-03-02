#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 20:47
# @Author  : Roohom
# @Site    : 
# @File    : dict1.py
# @Software: PyCharm
"""
定义和使用字典
"""

def main():
    scores = {'李白':85,'杜甫':89,'白居易':88}
    print(scores['杜甫'])
    print(scores['李白'])
    for elem in scores:
        print('%s\t---->\t%d' % (elem, scores[elem]))

    scores['白居易'] = 65
    scores['上官云晓'] = 77
    scores.update(冷面=67, 万户=99)
    print(scores)

    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    print(scores.get('武则天',60))
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('李白',77))
    scores.clear()
    print(scores)


if __name__ == '__main__':
    main()
