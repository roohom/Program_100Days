#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 10:40
# @Author  : Roohom
# @Site    :
# @File    : v15.py
# @Software: PyCharm

"""
破解有道词典
"""

def youdao(key):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    data = {
        "i": "girl,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15882146656485",
        "signv": "58e960e2f098a4a529d9dc11b984d1f2",
        "ts": "1588214665648",
        "bv": "b286f0a34340b928819a6f64492585e8",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }

    data = parse.urlencode(data).encode()
    headers = {

    }


