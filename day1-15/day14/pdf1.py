#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 22:11
# @Author  : Roohom
# @Site    : 
# @File    : pdf1.py
# @Software: PyCharm
"""
读取pdf文件
"""

from PyPDF2 import PdfFileReader

with open('Python编程快速上手—让繁琐工作自动化 PDF中文高清晰完整版.pdf', 'rb') as f:
    reader = PdfFileReader(f, strict=False)
    print(reader.numPages)
    if reader.isEncrypted:
        reader.decrypt('')
    current_page = reader.getPage(5)
    print(current_page)
    print(current_page.extractText())



