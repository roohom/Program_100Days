#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/5 23:02
# @Author  : Roohom
# @Site    : 
# @File    : v19.py
# @Software: PyCharm

"""
使用参数headers和params
"""

import requests

url = 'http://www.baidu.com/s?'

kw = {
    'wd': '熊猫'
}

headers = {
    'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}

rsp = requests.get(url, params=kw, headers=headers)

print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code)

