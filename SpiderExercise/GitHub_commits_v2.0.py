#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 10:17
# @Author  : Roohom
# @Site    : 
# @File    : GitHub_commits_v2.0.py
# @Software: PyCharm

"""
模拟登陆GitHub获取个人的commits数量
version=2.0

思路:
1. 用requests请求页面，使用BeautifulSoup在页面找到登录所需要的token
2. 同时把请求得到的cookie也保存
3. 再次用cookie去获取登录后的页面，在页面中查找commits元素，以获得commits数量

思路来源:https://www.cnblogs.com/littlesky1124/p/9315617.html

"""

import requests
from bs4 import BeautifulSoup

login_url = "https://github.com/login"
session_url = "https://github.com/session"
profile_url = "https://github.com/roohom"


def github_login(name, password):
    url = login_url

    rsp = requests.get(url)
    soup = BeautifulSoup(rsp.text, "lxml")

    # 获取登录所需要的的token
    token = soup.find(name='input', attrs={'name': 'authenticity_token'}).get('value')
    # print(token)

    # 获取登录所需要的cookie
    cookie = rsp.cookies.get_dict()
    # print(cookie)

    data = {
        "commit": "Sign in",
        "login": name,               # 用户名
        "password": password,       # 密码
        "webauthn - support": "supported",
        "webauthn - iuvpaa - support": "supported",
        "return_to": "",
        "required_field_7889":"",
        "authenticity_token": token
    }

    # headers = {
    #     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    #     "Accept - Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    #     "Cache - Control": "max - age = 0",
    #     "Connection": "keep - alive",
    #     "Content - Length": len(data),
    #     "Content - Type": "application / x - www - form - urlencoded",
    #     "Host": "github.com",
    #     "Origin": "https: // github.com",
    #     "cookies": cookie,
    #     "Referer": "https: // github.com / login",
    #     "Sec - Fetch - Dest": "document",
    #     "Sec - Fetch - Mode": "navigate",
    #     "Sec - Fetch - Site": "same - origin",
    #     "Sec - Fetch - User": "?1",
    #     "Upgrade - Insecure - Requests": "1",
    #     "User - Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    # }

    new_rsp = requests.get(url=profile_url, cookies=cookie).text
    page_soup = BeautifulSoup(new_rsp, 'lxml')
    items = page_soup.find('h2', {"class": "f4 text-normal mb-2"}).text
    commits = items.split(" ")
    print("你的commits数量是{}".format(commits[6]))


if __name__ == '__main__':
    name = "name"
    password = "password"
    github_login(name, password)

















