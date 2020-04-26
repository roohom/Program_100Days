#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 21:34
# @Author  : Roohom
# @Site    : 
# @File    : v04.py
# @Software: PyCharm


# URLerror的使用
"""
想用爬虫打开远程地址，都应该用trl来尝试，这样方便接收错误和解决错误
"""

from urllib import request,error


if __name__ == '__main__':
    url = "http://www.baiiiiiiidu.com"
    try:
        req = request.Request(url)
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print('URLerror:{}'.format(e.reason))
        print('URLerror:{}'.format(e))
    except Exception as e:
        print(e)


# URLerror:[Errno 11001] getaddrinfo failed
# URLerror:<urlopen error [Errno 11001] getaddrinfo failed>
