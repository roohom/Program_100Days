#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 21:50
# @Author  : Roohom
# @Site    : 
# @File    : badWord.py
# @Software: PyCharm

"""
替换字符串中的不良字符
"""

import re
def main():
    sentence = '你为什么一直在弄这个，你一直做这个是你妈逼的？'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)

if __name__ == '__main__':
    main()