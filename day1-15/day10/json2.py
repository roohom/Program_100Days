#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 22:34
# @Author  : Roohom
# @Site    : 
# @File    : json2.py
# @Software: PyCharm
"""
写入json数据
"""

import json

teacher_dict = {'name':'drh', 'age':22, 'title':'侦探'}
json_str = json.dumps(teacher_dict)
print(json_str)
print(type(json_str))
fruits_list = ['apple', 'orange', 'strawberry', 'banana', 'pitaya']
json_str = json.dumps(fruits_list)
print(json_str)
print(type(json_str))