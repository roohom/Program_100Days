#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 21:44
# @Author  : Roohom
# @Site    : 
# @File    : v05.py
# @Software: PyCharm


from urllib import request,error


if __name__ == '__main__':
    url = "http://www.cnipa.gov.cn/www"
    try:
        req = request.Request(url)
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print('URLerror:{}'.format(e.reason))
        print('URLerror:{}'.format(e))
    except error.URLError as e:
        print('URLerror:{}'.format(e.reason))
        print('URLerror:{}'.format(e))
    except Exception as e:
        print(e)


# URLerror:Not Found
# URLerror:HTTP Error 404: Not Found