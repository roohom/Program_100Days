#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/10 18:37
# @Author  : Roohom
# @Site    : 
# @File    : v32.py
# @Software: PyCharm
from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'

rsp = request.urlopen(url)

content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

print(soup.name)

print('==' * 20)
for node in soup.head.contents:
    if node.name == 'meta':
        print(node)
        print("--------------------")
    if node.name == 'title':
        print(node.string)
