#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/10 17:53
# @Author  : Roohom
# @Site    : 
# @File    : v28.py
# @Software: PyCharm

from lxml import etree

# 只能读取xml格式的内容
html = etree.parse("./v27.html")
rst = etree.tostring(html, pretty_print=True)


print(rst)

















