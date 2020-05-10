#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/10 23:14
# @Author  : Roohom
# @Site    : 
# @File    : v36.py
# @Software: PyCharm

"""
使用selenium操作百度搜索
"""


from selenium import webdriver
import time

# 通过keys模拟键盘
from selenium.webdriver.common.keys import Keys

# 操作哪个浏览器就对哪个浏览器建立一个实例
# 自动按照环境变量去查找相应的浏览器
driver = webdriver.PhantomJS()

# 如果浏览器没有在相应的环境变量中，需要指定

driver.get("http://www.baidu.com")
time.sleep(1)


# 通过函数查找title标签
print("Title:{}".format(driver.title))




