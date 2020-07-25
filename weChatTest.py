#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 09:58
# @Author  : Roohom
# @Site    : 
# @File    : weChatTest.py
# @Software: PyCharm


# -*- coding: utf-8 -*-
import itchat
import pygame

'''
微信红包提醒
1.提醒 音乐提醒
2.个人红包
3.群里红包
'''
# 设置微信为自动登录
itchat.auto_login(hotReload=True)


# 提醒
def alarm():
    # # 初始化模块
    # pygame.mixer.init()
    # # 加载一个音乐
    # pygame.mixer.music.load('alarm.mp3')
    # # 播放音乐
    # pygame.mixer.music.play()
    print("收到红包了！")


# 个人红包 @装饰器 给函数增加新功能的
# 监控是否有个人给我发通知类型的信息
@itchat.msg_register('Note', isGroupChat=False)
def getNote(msg):
    if '收到红包' in msg['Text']:
        print(msg['Text'])
        alarm()  # 调用提醒声音函数


# 群里红包
@itchat.msg_register('Note', isGroupChat=True)
def getGroupNote(msg):
    if '收到红包' in msg['Text']:
        print(msg['Text'])
        alarm()


# 让监控跑起来
itchat.run()