#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 22:31
# @Author  : Roohom
# @Site    : 
# @File    : boss_recruit.py
# @Software: PyCharm
"""
爬取boss直聘职位信息
本版本只在登录身份下获取职位列表

参考自:https://blog.csdn.net/qq_37819695/article/details/90708166
"""

import requests
from bs4 import BeautifulSoup
import random
import json
import time

user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15"
]

headers = {
        "user-agent": random.choice(user_agent_list)
    }

get_citicode_url = "https://www.zhipin.com/wapi/zpCommon/data/city.json"


# 获取城市代码
def get_city_code(city_name):
    rsp = requests.get(get_citicode_url, headers=headers)
    rsp = json.loads(rsp.text)
    cities = rsp["zpData"]["cityList"]
    city_code = None
    for city in cities:
        if city["name"]==city_name:
            city_code = city["code"]

    # print(city_code)
    return city_code


"""
query: python
city: 101190400
industry: 
position: 
"""
# get_pos_url = "https://www.zhipin.com/job_detail/?query=python&city=101190400&industry=&position="


def get_url(query='', city="", industry="", position="", page=1):
    base_url = "https://www.zhipin.com/job_detail/?query={}&city={}&industry={}&position={}&page={}".format(query, city, industry, position, page)
    urls = []
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    page_list = soup.find("div", "page").find_all("a")
    urls.append(base_url)
    while page_list[len(page_list) - 1]["href"] != "javascript:;":
        page += 1
        url = base_url.format(query, city, industry, position, page)
        urls.append(url)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        page_list = soup.find("div", "page").find_all("a")
    return urls


def get_html(url):
    response = requests.get(url, headers=headers)
    return response.text


def job_info(job_name, company, industry, finance, staff_number, salary, site, work_experience, education_bak, job_desc):
    return {
        "job_name": job_name,
        "company": company,
        "industry": industry,
        "finance": finance,
        "staff_number": staff_number,
        "salary": salary,
        "site": site,
        "work_experience": work_experience,
        "education_bak": education_bak,
        "job_desc": job_desc
    }


def get_job_desc(jid, lid):
    url = "https://www.zhipin.com/wapi/zpgeek/view/job/card.json?jid={}&lid={}"
    response = requests.get(url.format(jid, lid), headers=headers)
    html = json.loads(response.text)["zpData"]["html"]
    soup = BeautifulSoup(html, "lxml")
    desc = soup.find("div", "detail-bottom-text").get_text()
    return desc


def get_content(html):
    bs = BeautifulSoup(html, 'lxml')
    contents = []
    for info in bs.find_all("div", "job-primary"):
        job_name = info.find("div", "job-title").get_text()
        company = info.find("div", "company-text").a.get_text()
        jid = info.find("div", "info-primary").a["data-jid"]
        lid = info.find("div", "info-primary").a["data-lid"]
        desc = get_job_desc(jid, lid)
        texts = [text for text in info.find("div", "info-primary").p.stripped_strings]
        site = texts[0]
        work_exp = texts[1]
        edu_bak = texts[2]
        salary = info.span.get_text()
        companies = [text for text in info.find("div", "company-text").p.stripped_strings]
        industry = companies[0]
        if len(companies) > 2:
            finance = companies[1]
            staff_num = companies[2]
        else:
            finance = None
            staff_num = companies[1]
        contents.append(job_info(job_name, company, industry, finance, staff_num, salary, site, work_exp, edu_bak, desc))
        time.sleep(1)
    return contents




def main():
    city_name = "深圳"
    city = get_city_code(city_name)
    query = "python"
    urls = get_url(query=query, city=city)
    contents = []
    for url in urls:
        html = get_html(url)
        content = get_content(html)
        contents += content
        time.sleep(5)
    print(contents)


if __name__ == '__main__':
    main()








