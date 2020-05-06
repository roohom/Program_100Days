#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 21:37
# @Author  : Roohom
# @Site    : 
# @File    : v20.py
# @Software: PyCharm


import requests
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
# 构造一个请求头，请求头至少应该包括传入的数据的长度
# request要求传入的请求头是一个dict格式
headers = {
    # 因为使用post， 至少应该Content-Length
    'Content-Length': str(len(data))
}

rsp = requests.post(url=baseurl, data=data, headers=headers)

# 把json字符串转化成字典
print(rsp.text)
print(rsp.json())
items = rsp.json()


for item in items['data']:
    print(item['k'], '-----', item['v'])









