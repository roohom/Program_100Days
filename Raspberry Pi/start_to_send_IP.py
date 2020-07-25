#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 22:20
# @Author  : Roohom
# @Site    : 
# @File    : start_to_send_IP.py
# @Software: PyCharm

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import sys
import socket, fcntl, struct, time
import datetime

SMTPserver = "smtp.qq.com"
Sender = "roohom@qq.com"  # 发送到邮箱的地址
password = "xxxxxxxxxxxxx"  # 邮箱授权码
time.sleep(5)
nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 顺便打印下时间，方便识别


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.1.1.1", 80))
    ip_address = s.getsockname()[0]
    s.close
    return ip_address


# ip=get_ip('wlan0')#获取 wlan0的网卡
ip = get_ip()
# ip=str(sys.argv)
tet = 'My Raspberry Pi restart now!' + '\n' + '开机时间: ' + nowTime + '\n' + '\n' + '本机IP地址是：' + ip
print("server ip:", tet)
msg = MIMEText(tet, 'plain', 'utf-8')

msg["Subject"] = Header(u'树莓派IP', 'utf-8').encode()
msg["From"] = Sender
msg["to"] = "roohom@qq.com"  # 发送到哪里
mailserver = smtplib.SMTP(SMTPserver, 25)

try:
    # 登录邮箱
    mailserver.login(Sender, password)
    mailserver.sendmail(Sender, ["roohom@qq.com"], msg.as_string())
    mailserver.quit()
    print("success!!")
except smtplib.SMTPException:
    print("error:failed!!")


