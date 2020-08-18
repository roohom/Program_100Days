#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/18 21:11
# @Author  : Roohom
# @Site    : 
# @File    : perfumeList.py
# @Software: PyCharm


import xlwt
# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding = 'utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('My Worksheet')

# 写入excel
# 参数对应 行, 列, 值
worksheet.write(0,0, label = 'this is test')

# 保存
workbook.save('D:\\perfume.xls')