#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/10 18:47
# @Author  : Roohom
# @Site    : 
# @File    : v33.py
# @Software: PyCharm
from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'

rsp = request.urlopen(url)

content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

print("=="*30)

tsgs = soup.find_all(name='meta')

print(tsgs)


