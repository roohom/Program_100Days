#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 21:46
# @Author  : Roohom
# @Site    : 
# @File    : garbage_time.py
# @Software: PyCharm
a = [4, 8, 7, 15]
b = [7, 9, 17, 14]
c = [6, 9, 12, 8]
d = [6, 7, 14, 6]

import itertools

ls = list(itertools.permutations([1, 2, 3, 4], 4))

Ts = []
for mtd in ls:
    T = a[mtd[0]-1] + b[mtd[1]-1] + c[mtd[2]-1] + d[mtd[3]-1]
    print(mtd, "对应的时间：",T)
    Ts.append(T)

print(Ts)
print("最小的时间是:{}".format(min(Ts)))



















