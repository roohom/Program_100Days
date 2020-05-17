#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 10:33
# @Author  : Roohom
# @Site    : 
# @File    : boss_recruit_v2.py
# @Software: PyCharm
"""
爬取boss直聘下制定关键词(python)的职位信息
此版本只爬取了第一页
并且必须用cookie登录
由于能力不足，尚未完成破解
"""

"https://www.zhipin.com/job_detail/?query=python&city=101190400&industry=&position="

import requests
from selenium import webdriver
import time
import random
from bs4 import BeautifulSoup

# url = "https://www.zhipin.com/suzhou/?sid=sem_pz_bdpc_dasou_title"
#
# driver = webdriver.Chrome()
# driver.get(url)
# driver.find_element_by_class_name("ipt-search").send_keys("python")
# print("正在键入搜索内容>>>>>>>>>>>>>>>>")
# time.sleep(1)
# driver.find_element_by_xpath('//button[@class="btn btn-search"]').click()
# print("点击搜索按钮>>>>>>>>>>>>>>>>>>>")
# time.sleep(2)
#
# data = driver.page_source
#
# print(data)
# driver.quit()

user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; ) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
]

headers = {
    "referer": "https://www.zhipin.com/suzhou/?sid=sem_pz_bdpc_dasou_title",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": random.choice(user_agent_list)
    }


url = "https://www.zhipin.com/job_detail/?query=python&city=101190400&industry=&position="
res = requests.get(url)
cookies = res.cookies.get_dict()
rsp = requests.get(url, headers=headers,cookies=cookies).text
soup = BeautifulSoup(rsp, "lxml")
items = soup.find_all("span", {"class": "job-name"})
for item in items:
    print(item.string)





