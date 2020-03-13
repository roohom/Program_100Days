#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 23:11
# @Author  : Roohom
# @Site    : 
# @File    : function4.py
# @Software: PyCharm

"""
函数的参数
- 位置参数
- 可变参数
- 关键字参数
- 命名关键字参数
"""

#参数默认值
def f1(a, b=5,c=10):
    return a + b*2 + c*3


print(f1(1,2,3))
print("-----------")
print(f1(100,200))
print("-----------")
print(f1(100))
print("-----------")
print(f1(c=2,b=3,a=1))
print("-----------")


#可变参数
def f2(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(f2(1,2,3))
print("-----------")
print(f2(1,2,3,4))
print("-----------")
print(f2())
print("-----------")


#关键字参数
def f3(**kw):
    if 'name' in kw:
        print('欢迎你%s!' % kw['name'])
    elif 'tel' in kw:
        print('你的联系电话是：%s!' % kw['tel'])
    else:
        print("没有你的个人信息！")

param = {'name':'董如红','age':22}
f3(**param)
f3(name='董如红',age= 22, tel= 18256993000)
f3(user='董如红',age=22, tel=18256993000)
f3(user='董如红',age=22, mobile=18256993000)


