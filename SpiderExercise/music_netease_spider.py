#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 11:36
# @Author  : Roohom
# @Site    : 
# @File    : music_netease_spider.py
# @Software: PyCharm

from tkinter import *
import requests
from urllib import request
from bs4 import BeautifulSoup
import os

"""
音乐下载外链:
http://music.163.com/song/media/outer/url?id=

1. 获取页面源码 https://music.163.com/#/playlist?id=3214189237
2. 获取歌曲id以及歌曲名称
3. 下载音乐
"""


def music_spider():
    # 获取用户输入的url
    # url = entry.get()
    # 歌单地址
    url = "https://music.163.com/playlist?id=3214189237"
    headers = {
        "Host": "music.163.com",
        "Referer": "https: // music.163.com /",
        "Sec - Fetch - Dest": "iframe",
        "Sec - Fetch - Mode": "navigate",
        "Sec - Fetch - Site": "same - origin",
        "Upgrade - Insecure - Requests": "1",
        "User - Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }

    # 请求页面详情
    rsp = requests.get(url, headers=headers).text
    # ul class="f-hide"><li><a href="/song?id=571338279"

    # 获取id
    # 创建soup对象
    soup = BeautifulSoup(rsp, 'lxml')

    # 获取歌曲id与歌曲名称
    items = soup.find('ul', {'class':"f-hide"}).find_all('a')
    # print(items)

    music_dicts = {}
    for item in items:
        song_id = item.get('href').strip('/song?id=')
        song_name = item.text
        # print(music_name, music_id)
        music_dicts[song_id]=song_name

    for song_id in  music_dicts:
        # 拼接歌曲下载的url地址
        song_url = "http://music.163.com/song/media/outer/url?id={}.mp3".format(song_id)
        print(song_url)

        # 设置下载路径
        path = r"E:\Pycharm Projects\Program_100Days\SpiderExercise\music_163_down"
        if not os.path.exists(path):
            os.makedirs(path)

        # 添加数据到控件中
        text.insert(END, "Downloading:{}".format(music_dicts[song_id]))

        # 文本框向下滚动
        text.see(END)
        # 更新
        text.update()

        res = requests.get(url=song_url, headers=headers, allow_redirects=False)
        # print(res.status_code)
        # print(res.headers)
        real_url = res.headers['Location']
        request.urlretrieve(song_url, path+'\\'+music_dicts[song_id]+".mp3")


# 创建窗口
root = Tk()

# 设置窗口标题
root.title("网易云音乐下载器")

# 设置窗口大小
root.geometry("750x550")

# 设置窗口位置
root.geometry("+350+150")

# 设置下载标签，键入下载的地址
lable = Label(root, text="请输入您想下载的歌曲地址:", font=('Droid Sans', 12))
lable.grid()

# 输入框
entry = Entry(root, font=('微软雅黑', 12), width=55)
entry.grid(row=0, column=1)

# 设置列表框
text = Listbox(root, font=('Droid Sans', 12), width=92, height=20)
text.grid(row=1, columnspan=2)

# 设置按钮   N S W E
button = Button(root, text='Start', font=('微软雅黑', 12), command=music_spider())
button.grid(row=2, column=0, sticky='e')

# 退出按钮
button2 = Button(root, text='Quit', font=('微软雅黑', 12), command=root.quit)
button2.grid(row=2, column=1, sticky='n')

# 显示窗口，设置消息回环
root.mainloop()














