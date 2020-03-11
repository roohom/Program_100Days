#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 22:09
# @Author  : Roohom
# @Site    : 
# @File    : email.py
# @Software: PyCharm

"""
使用python发邮件
"""
"""
Traceback (most recent call last):
  File "E:/Pycharm Projects/Program_100Days/day13/email.py", line 13, in <module>
    from smtplib import SMTP
  File "C:\Users\rooho\AppData\Local\Programs\Python\Python37-32\lib\smtplib.py", line 47, in <module>
    import email.utils
  File "E:\Pycharm Projects\Program_100Days\day13\email.py", line 13, in <module>
    from smtplib import SMTP
ImportError: cannot import name 'SMTP' from 'smtplib' (C:\Users\rooho\AppData\Local\Programs\Python\Python37-32\lib\smtplib.py)

Process finished with exit code 1
"""


from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    # 请自行修改下面的邮件发送者和接收者
    sender = 'roohom@qq.com'
    receivers = ['911066833@qq.com', '1984392149@qq.com']
    message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = Header('王大锤', 'utf-8')
    message['To'] = Header('董如红', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP('smtp.qq.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, 'secretpass')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')


if __name__ == '__main__':
    main()