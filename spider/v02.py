#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 22:50
# @Author  : Roohom
# @Site    : 
# @File    : v02.py
# @Software: PyCharm
# 程序完成情况： 未完成


# 使用有道翻译

baseurl = 'http://fanyi.youdao.com/translate_o?smartresu' \
          'lt=dict&smartresult=rule'

from urllib import request, parse
import json

your_word= input("键入你想翻译的内容：")

data = {
    'i': 'your_word'
}

data = parse.urlencode(data).encode('utf-8')

rsp = request.urlopen(baseurl, data=data)
json_data = rsp.read().decode('utf-8')
print(json_data)

json_data = json.loads(json_data)
print(json_data)

