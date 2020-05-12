#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 15:50
# @Author  : Roohom
# @Site    : 
# @File    : v38.py
# @Software: PyCharm

from PIL import Image
import pytesseract as pt

image = Image.open(r"C:\Users\rooho\Desktop\验证码2.jpg")

text = pt.image_to_string(image)

print(text)










