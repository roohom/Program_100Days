#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 10:28
# @Author  : Roohom
# @Site    : 
# @File    : email02.py
# @Software: PyCharm
"""
使用Python发邮件自动化-带html的邮件
"""

from email.mime.text import  MIMEText

mail_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
        <h1> 这是一封HTML格式邮件</h1>
        </body>
        </html>
        """

msg = MIMEText(mail_content, "html", "utf-8")

# 构建发送者地址和登录信息
# 发送email地址，此处地址直接使用我的qq邮箱，密码一般需要临时输入，此处偷懒
from_addr = "roohom@qq.com"
# 此处密码是经过申请设置后的授权码，不是不是不是你的qq邮箱密码
from_pwd = "tpocgnmjvnvlbihe"


# 构建邮件接受者信息
addr1 = "911066833@qq.com"
addr2 = "1984392149@qq.com"
addr3 = "1451171571@qq.com"
to_addr = [addr1, addr2, addr3]

smtp_srv = "smtp.qq.com"


try:
    import smtplib

    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)

    srv.login(from_addr, from_pwd)
    srv.sendmail(from_addr, to_addr, msg.as_string())
    srv.quit()
    print("邮件发送完成")
except Exception as e:
    print(e)