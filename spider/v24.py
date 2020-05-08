#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 15:01
# @Author  : Roohom
# @Site    : 
# @File    : v24.py
# @Software: PyCharm
"""
匹配中文
"""

import re

hello = u'您好，我的世界'

pattern = re.compile(r'[\u4e00-\u9fa5]+')
m = pattern.findall(hello)
print(m)







