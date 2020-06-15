#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 23:35
# @Author  : Roohom
# @Site    : 
# @File    : wechat_vote.py
# @Software: PyCharm

from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
import time


bot = Bot()     #登录微信


def send_news():
    try:

        my_friend = bot.friends().search(u'宣金祥')[0]# 好友的微信号，可以在获取好友列表中找
        my_friend.send(u"Have a NICE day!")  #描述自己修改
        time.sleep(3)
        #my_friend = bot.mps().search(u"安徽共青团")[0]
        #my_friend.send(u"29282")
        time.sleep(3)
        # t = Timer(2, send_news) # 设置发送时间间隔
        # t.start()

    except:
        my_friend = bot.friends().search('roohom')[0]# 自己的微信号
        my_friend.send(u"今天消息发送失败了")    #描述自己修改


if __name__ == "__main__":
    n = 5
    for i in range(5):
        print("您开始的投票即将在{}秒之后开始....".format(n))
        n -= 1
        time.sleep(1)
    for i in range(5):
        send_news()
        time.sleep(2)

