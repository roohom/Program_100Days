#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 10:40
# @Author  : Roohom
# @Site    :
# @File    : v15.py
# @Software: PyCharm

"""
破解有道词典
处理JS加密

通过查找，能找到js代码中操作代码
1. 这个是计算salt的公式 r = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10));
2. sign: n.md5("fanyideskweb" + t + r + "ebSeFb%=XZ%T[KZ)c(sy!");
md5一共需要四个参数，第一个和第四个都是固定值的字符串，第三个是所谓的salt，第二个是。。。。。
第二个参数就是输入的要查找的单词
"""

from urllib import request, parse


def getSalt():
    """
    salt
    :return: salt
    """
    import time, random
    salt = int(time.time()*1000) + random.randint(0, 10)
    return salt


def getMD5(k):
    import hashlib
    md5 = hashlib.md5()
    md5.update(k.encode('utf-8'))

    sign = md5.hexdigest()
    return sign


def getSign(key, salt):
    sign = 'fanyideskweb' + key + str(salt) + 'ebSeFb%=XZ%T[KZ)c(sy!'
    sign = getMD5(sign)

    return sign


def youdao(key):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    salt = getSalt()
    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(salt),
        "sign": getSign(key, salt),
        "ts": "1588214665648",
        "bv": "b286f0a34340b928819a6f64492585e8",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }

    data = parse.urlencode(data).encode()
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        # "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=-487267925@10.108.160.19; OUTFOX_SEARCH_USER_ID_NCOO=44199253.42152389; _ntes_nnid=7c252dbe64e633d98de29b4364576d75,1583658514973; JSESSIONID=aaacajtWWg0nca32pskhx; ___rl__test__cookies=1588237907246",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)


if __name__ == '__main__':
    youdao('girl')


