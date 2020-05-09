#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/9 10:23
# @Author  : Roohom
# @Site    : 
# @File    : search_url_for_py.py
# @Software: PyCharm

"""
批量爬取百度上的页面，返回有注册页面的网址
"""



import requests
from bs4 import BeautifulSoup
import time
import re


# 将百度的url转成真实的url
def convert_url(url):
    resp = requests.get(url=url,
                        headers=headers,
                        allow_redirects=False
                        )
    return resp.headers['Location']


# 获取url
def get_url(wd):
    # 将爬取到的url保存，如不需要删除相关代码
    file_url = open('url.txt', 'a+')
    list = []
    s = requests.session()
    r = s.get("https://www.baidu.com/s?wd=" + wd + "&pn=1", headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    for so in soup.select('#content_left .t a'):
        g_url = so.get('href')
        list.append(convert_url(g_url))
        file_url.write(convert_url(g_url) + '\n')
    screen(list)
    list.clear()
    # 程序停止8秒，避免爬取太快被禁止访问
    time.sleep(8)
    # 10为第2页，20为第三页，30为第四页，以此类推
    for i in range(10, 600, 10):
        url = 'https://www.baidu.com/s'
        params = {
            "wd": wd,
            "pn": i,
            "oq": wd
        }
        r = s.get(url=url, headers=headers, params=params)
        soup = BeautifulSoup(r.text, 'lxml')
        for so in soup.select('#content_left .t a'):
            g_url = so.get('href')
            list.append(convert_url(g_url))
            file_url.write(convert_url(g_url) + '\n')
        screen(list)
        list.clear()
        # 不能总是停止8秒，不知道影不影响，但是保险起见模仿的像人随机一点
        # 但其实可以不用的，因为screen方法执行的时间肯定不一样，别问我那为什么不改，我任性
        time.sleep(10 + (i / 10))
    file_url.close()


# 筛选url
def screen(list):
    s_url = open('s_url.txt', 'a+')
    for url in list:
        try:
            requests.packages.urllib3.disable_warnings()
            r = requests.get(url=url, headers=headers1, verify=False, allow_redirects=False)
            print(url)
            # 符合则将该url写入文件
            if re.search('手机号', r.text) and (
                    re.search('短信验证码', r.text) or re.search('获取验证码', r.text) or re.search('发送验证码', r.text)):
                print('符合')
                s_url.write(url + '\n')
        except:
            print('异常')
            continue
    s_url.close()


if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0",
        "Host": "www.baidu.com",
    }
    headers1 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"
    }
    wd = "注册页面"
    get_url(wd)



