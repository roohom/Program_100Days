#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 17:41
# @Author  : Roohom
# @Site    : 
# @File    : v09.py
# @Software: PyCharm

# 在有cookie的情况下登录
from urllib import request

if __name__ == '__main__':
    url = 'http://www.renren.com/974330879/profile'
    headers = {
        'cookie': 'anonymid=k9l54dnlo21n8p; depovince=GW; _r01_=1; JSESSIONID=abc-V1zHrIxvJdIA0rfhx'
                  '; ick_login=7c0afc48-1779-4c71-a90a-bef98fb985d9; taihe_bi_sdk_uid=3af020db'
                  'ccdf707ff3d92efdde830922; taihe_bi_sdk_session=52782ba245047468095bd27a73650abb; '
                  'ick=22934045-f2c2-42c6-b00b-a9e765d4984d; t=449195d72fb85bcd1370399efa8ff2809; societyguest'
                  'er=449195d72fb85bcd1370399efa8ff2809; id=974330879; xnsid=3ab7ed66; XNESSESSIONID=3ed4d755055f; WebO'
                  'nLineNotice_974330879=1; jebecookies=a2fef377-eae9-4eae-a6f8-e3e44eae28ed|||||; ver=7.0; loginfrom=n'
                  'ull; jebe_key=2922641d-b8e0-4199-b4b7-4c3b677708f8%7C5232aaabdf3bc07afa97b37b5459d04d%7C158815284250'
                  '3%7C1%7C1588152843102; jebe_key=2922641d-b8e0-4199-b4b7-4c3b677708f8%7C5232aaabdf3bc07afa97b37b5459d'
                  '04d%7C1588152842503%7C1%7C1588152843104; wp_fold=0'
    }

    # 发送请求
    req = request.Request(url, headers=headers)
    rsp = request.urlopen(req)

    html = rsp.read().decode()

    with open('rsp-cookie.html', 'w') as f:
        f.write(html)





