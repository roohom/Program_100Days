#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/10 20:58
# @Author  : Roohom
# @Site    : 
# @File    : v34.py
# @Software: PyCharm

from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'

rsp = request.urlopen(url)

content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

print(soup.prettify())
print("==="* 12)
titles = soup.select("title")
print(titles[0])

print("==="* 12)
metas = soup.select("meta[content='always']")
print(metas[0])




