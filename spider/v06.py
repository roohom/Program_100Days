#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 22:07
# @Author  : Roohom
# @Site    : 
# @File    : v06.py
# @Software: PyCharm

"""
更改UserAgent进行伪装
"""

from urllib import request,error


if __name__ == '__main__':
    url = 'http://www.baidu.com'

    try:

        # 使用head方法伪装UA
        # headers = {}
        # headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version' \
        #                         '/5.1.7 Safari/534.57.2'
        # req = request.Request(url, headers=headers)
        req = request.Request(url)
        req.add_header("User-Agent", 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2')
        # 正常访问
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)

print('Done>>>>>>>>>>>>>>')