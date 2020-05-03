#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 22:59
# @Author  : Roohom
# @Site    : 
# @File    : v17.py
# @Software: PyCharm


"""
爬取豆瓣电影数据
了解ajax的基本爬取方式
"""

from urllib import request
import json


url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=60&limit=20'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'

}

req = request.Request(url=url, headers=headers)

rsp = request.urlopen(req)
data = rsp.read().decode()

data = json.loads(data)

for item in data:
    print(item['title'], '----->', item['url'])

import pandas
df=pandas.DataFrame(data)
df.to_excel('D:\\douban.xlsx') # 保存到Excel


