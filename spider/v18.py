#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 23:38
# @Author  : Roohom
# @Site    : 
# @File    : v18.py
# @Software: PyCharm

import requests

url = 'http://www.baidu.com'

# 两种请求方法
# 使用get请求
rsp = requests.get(url)

print(rsp.text)

# 使用request请求
rsp = requests.request('get', url)
print(rsp.text)




