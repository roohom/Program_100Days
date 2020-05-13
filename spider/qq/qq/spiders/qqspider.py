#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 17:54
# @Author  : Roohom
# @Site    : 
# @File    : qqspider.py
# @Software: PyCharm

import scrapy
import re


from qq.items import QQItem


class QQSpider(scrapy.Spider):
    name = 'qq'
    # 设置只能爬取腾讯域名
    allowed_domains = {'hr.tencent.com'}
    start_urls = {
        'https://hr.tencent.com/positon.php?&start=0#a'

    }
    def parse(self, response):
        """
        :param response:
        :return:
        """
        # 下载结果自动存放在response中
        for each in response.xpath('//*[@class="even]'):
            item =  QQItem()
            name = each.xpath()
    #对于每一个工作信息内容




