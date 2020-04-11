#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 17:02
# @Author  : Roohom
# @Site    : 
# @File    : p01.py
# @Software: PyCharm

"""
获取GitHub上自己一年以内的commits数量//未成功
"""


from urllib import request


if __name__ == '__main__':

    url = "https://github.com/"
    your_repo = input("input your username:")
    url += your_repo

    rsp = request.urlopen(url)
    html = rsp.read()
    html = html.decode()

    print(html)







