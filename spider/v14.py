#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 10:22
# @Author  : Roohom
# @Site    : 
# @File    : v14.py
# @Software: PyCharm

from urllib import request

# 导入Python SSL处理模块
import ssl

# 利用非认证上下文环境替换认证的上下文环境
ssl_create_default_https_context = ssl._create_unverified_context()


url = 'https://www.12306.cn/mormhweb/'
rsp = request.urlopen(url)
html = rsp.read().decode()
print(html)


