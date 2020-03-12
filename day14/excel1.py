#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 21:47
# @Author  : Roohom
# @Site    : 
# @File    : excel1.py
# @Software: PyCharm
"""
创建excel文件
"""

from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

workbook = Workbook()
sheet = workbook.active
data = [
    [1001, '李白', '刺客', '1990000000'],
    [1002, '亚瑟', '战士', '1820000000']
]

sheet.append(['学号', '姓名', '性别', '电话'])
for row in data:
    sheet.append(row)

tab = Table(displayName="Table1", ref="A1:E5") #如果使用单引号：warn("File may
                                               # not be readable: column headings must be strings.")

tab.tableStyleInfo = TableStyleInfo(
    name='TableStyleMedium9', showFirstColumn=False,
    showLastColumn=False, showRowStripes=True, showColumnStripes=True
)
sheet.add_table(tab)
workbook.save('王者峡谷数据.xlsx')

