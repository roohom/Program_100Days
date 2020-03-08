#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 22:29
# @Author  : Roohom
# @Site    : 
# @File    : json1.py
# @Software: PyCharm

import json


json_str = '{"name":"drh", "age":"22", "title":"学生"}'
result = json.loads(json_str)

print(result)
print(type(result))
print(result['name'])
print(result['age'])

