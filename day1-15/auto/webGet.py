#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 19:35
# @Author  : Roohom
# @Site    : 
# @File    : webGet.py
# @Software: PyCharm

import requests

res = requests.get("https://github.com/roohom/Python-100-Days/blob/master/Day01-15/01.%E5%88%9D%E8%AF%86Python.md")
print(res)

play_File = open("新建文本文档.txt", 'wb')
for chunk in res.iter_content(1000):
    play_File.write(chunk)

play_File.close()