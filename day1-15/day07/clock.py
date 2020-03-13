#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 22:02
# @Author  : Roohom
# @Site    : 
# @File    : clock.py
# @Software: PyCharm
"""
定义和使用时钟类
"""

import time
# 下文实现实时打印当前的时间，并且不会换行
import sys

class Clock(object):
    # Python中的函数是没有重载的概念的
    # 因为Python中函数的参数没有类型而且支持缺省参数和可变参数
    # 用关键字参数让构造器可以传入任意多个参数来实现其他语言中的构造器重载
    def __init__(self, **kw):
        if 'hour' in kw and 'minute' in kw and 'second' in kw:
            self._hour = kw['hour']
            self._minute = kw['minute']
            self._second = kw['second']
        else:
            tm = time.localtime(time.time())
            self._hour = tm.tm_hour
            self._minute = tm.tm_min
            self._second = tm.tm_sec

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
    def show_time(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


if __name__ == '__main__':
    clock = Clock()
    while(True):
        # os.system('cls')在编译器可能是行不通的，但在命令行可能能实现

        # 其关键就在于使用'\r'这个转义字符（回到行首），  sys.stdout.write首先打印这一行后不带任何结尾（print打印结尾带end="\n"，
        # 表示自带换行，换行了就不能在对已经打印的这一行进行更改编辑），使用了转移字符"\r"使得光标回到行首，
        # 再把缓冲区显示出来，就得到了我们所需要的效果。
        # ————————————————
        # 版权声明：本文为CSDN博主「roohom」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
        # 原文链接：https://blog.csdn.net/qq_39161804/article/details/81456913
        sys.stdout.write("\r{}".format(clock.show_time()))
        sys.stdout.flush()
        time.sleep(1)
        clock.run()





