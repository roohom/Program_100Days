#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/10 18:13
# @Author  : Roohom
# @Site    : 
# @File    : v30.py
# @Software: PyCharm

from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'

rsp = request.urlopen(url)

content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

content = soup.prettify()
print(content)
















