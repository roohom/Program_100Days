#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 09:40
# @Author  : Roohom
# @Site    : 
# @File    : v37.py
# @Software: PyCharm

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# 可能需要手动添加路径
driver = webdriver.Chrome()

url = "http://www.baidu.com"

driver.get(url)

text = driver.find_element_by_id("wrapper").text

print(text)
print(driver.title)

# 得到页面的快照
driver.save_screenshot("index.png")

# id='kw' 的是百度的输入框，得到输入框的ui元素之后输入“大熊猫”
driver.find_element_by_id("kw").send_keys(u'大熊猫')
# 输入之后需要点击搜索 id=‘su’是百度的搜索按钮，click模拟点击
driver.find_element_by_id('su').click()

time.sleep(5)
driver.save_screenshot("daxiongmao.png")


# 获取当前页面的cookie
print(driver.get_cookies())

# 模拟输入两个按键 ctrl+A
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
# CTRL + X
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

driver.find_element_by_id('kw').send_keys(u'500px图片')
driver.save_screenshot("px500zhaopian.png")
driver.find_element_by_id('su').send_keys(Keys.RETURN)

time.sleep(5)
driver.save_screenshot('zhaopian2.png')

# 清空输入框
driver.find_element_by_id('kw').click()
driver.save_screenshot('clear.png')

# 不用了需要关闭
driver.quit()












