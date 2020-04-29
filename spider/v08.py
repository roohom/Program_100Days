#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 17:36
# @Author  : Roohom
# @Site    : 
# @File    : v08.py
# @Software: PyCharm


# 在没有cookie的情况下登录
from urllib import request


if __name__ == '__main__':
    url = 'http://www.renren.com/974330879/profile'

    rsp = request.urlopen(url)
    html = rsp.read().decode()

    # print(html)
    with open('rsp.html', 'w') as f:
        f.write(html)









