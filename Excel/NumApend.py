#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 22:37
# @Author  : Roohom
# @Site    : 
# @File    : NumApend.py
# @Software: PyCharm

"""
使用Python操作
从此文件中按姓名查找对应的学号填写到另一个excel中的姓名之前
参考：https://www.cnblogs.com/pangwanzi/p/6475871.html
"""

import xlrd
from xlutils.copy import copy
import xlwt
import os

filename1 = r'D:\recent\20200426-合肥学院疫情防控主题教育成绩合格学生信息 (李五个班).xls'
filename2 = r'D:\recent\16电子1第二学期期末成绩.xlsx'

# 打开excel
NameSheet = xlrd.open_workbook(filename1)
NumSheet = xlrd.open_workbook(filename2)

# 复制一个
nsheet = copy(NameSheet)
msheet = copy(NumSheet)

# 从复制的excel文件中得到第一个sheet
sheet1 = nsheet.get_sheet(0)
sheet2 = msheet.get_sheet(0)
table1 = NameSheet.sheets()[0]
table2 = NumSheet.sheets()[0]


for i in range(15,34):
    for j in range(57):
        cell1 = table1.cell_value(i,1)  # 扫描第一个表的第i行第2列
        cell2 = table2.cell_value(j,2)
        cell3 = table1.cell_value(i,0)
        cell4 = table2.cell_value(j,1)
        if cell1==cell2:                # 如果第一个标的第i行第2列和第二个表的第j行第3列相同 即姓名匹配
            sheet1.write(i, 0, cell4)   # 就讲第二个表的第j行第2列的内容（学号）复制写入到第一个表的第i行第1列

os.remove(filename1)          # 删除原来的第一个表
nsheet.save(filename1)        # 将得到的新表保存（就是原来的表新增内容之后的样子）



