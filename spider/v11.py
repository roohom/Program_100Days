#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 09:35
# @Author  : Roohom
# @Site    : 
# @File    : v11.py
# @Software: PyCharm


"""
把获取到的cookie打印出来
"""


from urllib import request, parse
from http import cookiejar

# 创建Cookie.Jar的实例
cookie = cookiejar.CookieJar()

# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

# 创建http请求管理器
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)


def login():
    """
    负责初次登录
    需要输入用户名和密码，用来获取登录cookie凭证
    :return:
    """
    # 此url需要从登录form的action属性中提取
    url = "http://www.renren.com/PLogin.do"

    # 模拟post请求
    # 此键值需要从登录form的两个对应的input中提取name属性
    data = {
        'email' : '18256993059',
        'password': "roohom123"
    }

    # 把数据进行编码
    data = parse.urlencode(data)
    req = request.Request(url, data=data.encode())

    # 使用opener发起请求
    rsp = opener.open(req)


if __name__ == '__main__':
    """
    执行完login()会得到授权的cookie
    将得到的cookie打印出来
    """
    login()
    print(cookie)
    for item in cookie:
        # print(type(cookie))
        # print(item)
        for i in dir(item):
            print(i)
            print(item)
            print("-----------------------------")


