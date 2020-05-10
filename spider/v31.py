#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/10 18:20
# @Author  : Roohom
# @Site    : 
# @File    : v31.py
# @Software: PyCharm
from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'

rsp = request.urlopen(url)

content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

content = soup.prettify()
# print(content)
print("==" *12)
#print(soup.head)
print("==" *12)
print(soup.meta)
print("==" *12)
print(soup.link.name)
print(soup.link.attrs)
print(soup.link.attrs['type'])
print("==" *12)
print(soup.title) #<title>百度一下，你就知道</title>
print(soup.title.name) #title
print(soup.title.string) #百度一下，你就知道
print("==" *12)
print(soup.name)
print(soup.attrs)
print(soup.name)


