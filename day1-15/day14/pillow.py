#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 21:17
# @Author  : Roohom
# @Site    : 
# @File    : pillow.py
# @Software: PyCharm

"""
使用pillow操作图像
"""

from PIL import Image

img = Image.open('image-show.jpg')
print(img.size)
print(img.format)
print(img.format_description)
img.save('image.png')

img2 = Image.open('image.png')
img3 = img2.crop((335, 435, 430, 616))

for x in range(4):
    for y in range(5):
        img2.paste(img3, (95*y, 180*x))

img2.resize((img.size[0]//2, img.size[1]//2))
img2.rotate(90)
img2.save('image-show2.png')
