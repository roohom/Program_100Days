#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/19 08:05
# @Author  : Roohom
# @Site    : 
# @File    : boss_recruit_v3.py
# @Software: PyCharm
"""
使用Selenium登录boss直聘，并爬取职位信息
但需要手动拉动验证码
"""
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

url = "https://login.zhipin.com/?ka=header-login"

driver = webdriver.Chrome()
driver.get(url)

driver.find_element_by_xpath('//input[@name="account"]').send_keys("18256993059")
time.sleep(3)
driver.find_element_by_xpath('//input[@name="password"]').send_keys("roohom123")
time.sleep(3)

driver.find_element_by_xpath('//button[@class="btn"]')
time.sleep(3)



















