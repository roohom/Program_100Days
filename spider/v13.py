#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 10:05
# @Author  : Roohom
# @Site    : 
# @File    : v13.py
# @Software: PyCharm


from urllib import request, parse
from http import cookiejar

# 创建Cookie.Jar的实例
cookie = cookiejar.MozillaCookieJar()
cookie.load('cookie.txt', ignore_expires=True, ignore_discard=True)


# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

# 创建http请求管理器
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)


def getHomePage():
    url = 'http://www.renren.com/974330879/profile'

    # 如果已经执行了login函数，则opener自动已经包含相应的cookie
    rsp = opener.open(url)

    html = rsp.read().decode()
    with open('rsp-opener-another.html', 'w') as f:
        f.write(html)


if __name__ == '__main__':
    getHomePage()