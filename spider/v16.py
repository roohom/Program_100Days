#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 22:38
# @Author  : Roohom
# @Site    : 
# @File    : v16.py
# @Software: PyCharm

"""
爬取豆瓣电影数据
了解ajax的基本爬取方式
"""

from urllib import request
import json


url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=60&limit=20'

'''
如果用 urllib.request.urlopen 方式打开一个URL,服务器端只会收到一个单纯的对于该页面访问的请求,但是服务器并不知道发送这个请求使用的浏览器,操作系统,硬件平台等信息,而缺失这些信息的请求往往都是非正常的访问,例如爬虫.
有些网站验证请求信息中的UserAgent(它的信息包括硬件平台、系统软件、应用软件和用户个人偏好),如果UserAgent存在异常或者是不存在,那么这次请求将会被拒绝(如上错误信息所示)
所以可以尝试在请求中加入UserAgent的信息

解决办法见v17
'''

rsp = request.urlopen(url)
data = rsp.read().decode()

data = json.loads(data)
print(data)



