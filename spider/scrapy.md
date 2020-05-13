# Scrapy
# 爬虫框架
- 框架:
- 爬虫框架
    - scrapy
    - pyspider
    - crawley
- scrapy框架介绍
    - https://doc.scrapy.org/en/latest/
    
- 安装
    - 利用pip        
- scrapy概述
    - 包含各个部件
        - ScrapyEngine:核心    
        - Scheduler调度器:引擎发来的request请求，调度器需要处理，然后交换引擎
        - Downloader下载器:把引擎发来的requests发出请求，得到response
        - Spider爬虫:负责把下载器得到的网页/结果进行分解，分解成数据+链接
        - ItemPipeline管道:详细处理Item
        - DownloaderMiddleware下载中间件:自定义下载的功能扩展组件
        - SpiderMiddlerware爬虫中间件:对spider进行功能扩展
- 爬虫项目大概流程
    - 新建项目: scrapy startproject xxx
    - 明确需要目标/产出:编写item.py
    - 制作爬虫: 地址spider/xxspider.py
    - 存储内容: pipelines.py        
        
        
        
        
        
        
        
        
        
        
        