#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 23:41
# @Author  : Roohom
# @Site    : 
# @File    : xpath01.py
# @Software: PyCharm

"""
使用selenium来练习xpath
"""
from selenium import webdriver
import requests
import time

url = "http://www.baidu.com"

driver = webdriver.Chrome()

driver.get(url)

time.sleep(2)
driver.find_element_by_xpath('//input[@name="wd"]').send_keys("python")
time.sleep(2)
driver.find_element_by_xpath('//input[@value="百度一下"]').click()
driver.save_screenshot("search_for_python.png")

















