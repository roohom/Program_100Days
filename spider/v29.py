#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/10 17:59
# @Author  : Roohom
# @Site    : 
# @File    : v29.py
# @Software: PyCharm

from lxml import etree

html = etree.parse('./v27.html')
print(type(html))

rst = html.xpath('//book')
print(type(rst))
print(rst)

rst = html.xpath('//book[@category="sport"]')
print(type(rst))
print(rst)

# 查找带有category属性且值为sport得book元素下的year元素
rst = html.xpath('//book[@category="sport"]/year')
rst = rst[0]
print(type(rst))
print(rst)
print(rst.tag)
print(rst.text)

