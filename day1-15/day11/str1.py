#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 22:00
# @Author  : Roohom
# @Site    : 
# @File    : str1.py
# @Software: PyCharm

"""
字符串常用操作
"""

import pyperclip


print('My brother\'s name is \'007\'')
print(r'My brother\'s name is \'007\'')

str = 'hello123world'
print('he' in str)
print('her' in str)

print(str.isalpha())
print(str.isalnum())
print(str.isdecimal())

print(str[0:5].isalpha())
print(str[5:8].isdecimal())

list = ['床前明月光', '疑是地上霜', '举头望明月', '低头思故乡']
print('-'.join(list))
sentence = 'You go your way I will go mine'
words_list = sentence.split()
print(words_list)
email = '          roohom@qq.com           '
print(email)
print(email.strip())
print(email.lstrip())

pyperclip.copy('老虎不发猫你当我是病危啊！')



