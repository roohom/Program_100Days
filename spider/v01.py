#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 21:34
# @Author  : Roohom
# @Site    : 
# @File    : v01.py
# @Software: PyCharm

# 使用百度翻译
# post方法

"""
学习爬虫要归类学习，学会一类的方法，反复练

利用parse模块模拟post请求

分析百度翻译
步骤：
1. 打开F12
2. 输入一个单词，每键入一个字母都会有请求
3. 请求地址是:
4. 利用NetWork-All-Headers查看发现Form Data的kw：你键入的单词
5. 检查返回内容格式，发现返回的是json格式内容==> 需要用到json包
"""

from urllib import request, parse
import json

# 大致流程：
# 1. 利用data构造内容，然后用urlopen打开
# 2. 返回一个json格式的结果
# 3. 结果应该就是你输入的单词的翻译


baseurl = 'https://fanyi.baidu.com/sug'  # 这个需要自己去翻译的官网进行分析，也是重要的一步

your_word = input("请输入你想翻译的英文单词:")
# dict格式
data = {
    # your_word是翻译输入的英文内容
    'kw': your_word
}

# 需要使用parse模块对data进行编码
data = parse.urlencode(data).encode('utf-8')

# 构造一个请求头，请求头至少应该包括传入的数据的长度
# request要求传入的请求头是一个dict格式
headers = {
    # 因为使用post， 至少应该Content-Length
    'Content-Length': len(data)
}

# 发出请求
rsp = request.urlopen(baseurl, data=data)
json_data = rsp.read().decode('utf-8')
print(type(json_data))  # <class 'str>
print(json_data)  # {"errno":0,"data":[{"k":"apple","v":"n. \u82f9\u679c;"},{"k":"apples","v":"n. \u82f9\u679c;

# 把json字符串转化成字典
json_data = json.loads(json_data)
print(type(json_data))  # <class 'dict>
print(json_data)  # {'errno': 0, 'data': [{'k': 'apple', 'v': 'n. 苹果;'}, {'k': 'apples', 'v': 'n. 苹果;
# apple的复数;'}, {'k': 'apple juice', 'v': ' 苹果汁;'}, {'k': 'apple pie', 'v': 'n. 苹果派;
# 苹果馅饼;完美的家庭生活; 温馨舒适;'}, {'k': 'applet', 'v': 'n. 小应用程序; 小程序;'}]}


for item in json_data['data']:
    print(item['k'], '-----', item['v'])
