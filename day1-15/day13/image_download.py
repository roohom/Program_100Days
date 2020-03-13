#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 21:22
# @Author  : Roohom
# @Site    : 
# @File    : image_download.py
# @Software: PyCharm

"""
通过requests来实现一个访问网络数据接口并从中获取美女图片下载链接然后下载美女图片到本地的例子程序，程序中使用了天行数据提供的网络API
"""

import requests
from time import time
from threading import Thread


class DownloadHanlder(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('D:\\迅雷下载' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    resp = requests.get('http://api.tianapi.com/meinv/?key=4120941042b6a9708c9606e071bc6e3e&num=10') #天性数据的接口，需要自己申请
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        DownloadHanlder(url).start()



if __name__ == '__main__':
    main()



