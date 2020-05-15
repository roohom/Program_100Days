#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 22:37
# @Author  : Roohom
# @Site    : 
# @File    : github_commits.py
# @Software: PyCharm

"""
获取GitHub上自己的commits数量
version=1.0

思路:
1. 使用cookie登录自己的GitHub
2. 将自己的主页download下来
3. 分析页面数据，把commits的标签提出来

本版本是使用cookie登录，存在时效问题，时间久了就可能无法实现功能。
下个版本中考虑使用用户名和密码登录
"""


import requests
from bs4 import BeautifulSoup

url = "https://github.com/roohom"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "_octo=GH1.1.1206442831.1572359077; _ga=GA1.2.844106960.1574934706; _device_id=8f5a9985a082e26a5c15e5d74bfaf7a3; user_session=YXqGrxZOvX9G0O8mF745lsCAwO2k5iATntKGU0Q_bE5M9DRP; __Host-user_session_same_site=YXqGrxZOvX9G0O8mF745lsCAwO2k5iATntKGU0Q_bE5M9DRP; logged_in=yes; dotcom_user=roohom; has_recent_activity=1; _gat=1; tz=Asia%2FShanghai",
    "Host": "github.com",
    "If-None-Match": 'W/"2ae610dd3cfade66cc246c00567a8c10"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}

rsp = requests.get(url, headers=headers).text

soup = BeautifulSoup(rsp, "lxml")
items = soup.find('h2', {"class":"f4 text-normal mb-2"}).text
commits = items.split(" ")

print("你的commits数量是{}".format(commits[6]))








