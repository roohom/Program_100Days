#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 21:23
# @Author  : Roohom
# @Site    : 
# @File    : v03.py
# @Software: PyCharm

# 使用Request类，功能更强，更像是浏览器来访问服务器，实现身份隐藏


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

req = request.Request(url=baseurl, data=data, headers=headers)

# 因为已经构造了一个Request的请求案例，则所有的请求信息都可以封装在Request实例中
# 发出请求
rsp = request.urlopen(req)

json_data = rsp.read().decode('utf-8')
print(type(json_data))  # <class 'str>
print(json_data)  # {"errno":0,"data":[{"k":"apple","v":"n. \u82f9\u679c;"},{"k":"apples","v":"n. \u82f9\u679c;

# 把json字符串转化成字典
json_data = json.loads(json_data)
print(type(json_data))  # <class 'dict>
print(json_data)

for item in json_data['data']:
    print(item['k'], '-----', item['v'])

