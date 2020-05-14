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
            name = each.xpath('./td[1]a/text()').extract()[0]
            detailLink = each.xpath('./td[1]a/@href').extract()[0]
            positionInfo = each.xpath('./td[2]a/text()').extract()[0]
            workLocation = each.xpath('./td[4]a/text()').extract()[0]

            item['name'] = name.encode('utf-8')
            item['detailLink'] = detailLink.encode('utf-8')
            item['positionInfo'] = positionInfo.encode('utf-8')
            item['workLocation'] = workLocation.encode('utf-8')

            curpage = re.search('(\d+)', response=url).group(1)
            page = int(curpage) + 10

            url = re.sub('\d+', str(page), response.url)

            yield scrapy.Request(url, callback=self.parse)

            yield item


