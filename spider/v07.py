#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 22:31
# @Author  : Roohom
# @Site    : 
# @File    : v07.py
# @Software: PyCharm

"""
使用代理访问网站
"""


from urllib import request, error

if __name__ == '__main__':
    url = "http://www.baidu.com"

    # 1.
    # 设置代理地址
    proxy = {'http': '110.243.19.127:9999'} # 代理来自goubanjia.com
    # 2.
    # 创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3.
    # 创建opener
    opener = request.build_opener(proxy_handler)
    # 4.
    # 安装opener
    request.install_opener(opener)

    # 现在可以打开url，则使用代理服务器

    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)


