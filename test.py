#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 23:35
# @Author  : Roohom
# @Site    : 
# @File    : test.py
# @Software: PyCharm


import random

secert = random.randint(1,100)  #计算机随机生成一个数

##times = 3  #初始化用户的次数是三次
flag = 1
while flag:
    #a = int(input("输入数字"))
    times = 3
    while times:
        num = input("请输入一个数字：")
        if num.isdigit():
            tmp = int(num)
            if tmp == secert:
                print("你猜对啦！")
                break
            elif tmp > secert:
                print("你的数字太大啦！")
                times = times - 1
            else:
                print("你的数字太小啦！")
                times = times - 1

        else:
            print("叫你输入一个数字！！")
    if times==0:
        print("你的机会用完了!")
    else:
        pass
    game = input("你是否想要继续游戏？Y/N：")
    if game == "Y":
        flag = 1
    else:
        flag = 0
