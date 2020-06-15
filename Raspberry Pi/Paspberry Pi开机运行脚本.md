
# 树莓派开机运行脚本程序

>在持续搜索了网上大量的方法和尝试之后，终于找到了正确的方法。网上有些方法繁琐有些简单，但却都不顶用，直到找到了这一篇：[点这里](https://blog.csdn.net/zhaohb3486/article/details/106131113)

- 第一步，先给你的脚本以权限,比如你想要执行的脚本名字叫test.py(该文件在/home/pi文件夹之下)，那么先进入到他的目录下，再执行
~~~~
sudo chmod 777 test.py
~~~~

- 第二步，打开/etc/rc.local
~~~~
sudo nano /etc/rc.local
~~~~

- 第三步，在/etc/rc.local文件中（语句exit 0 之上一行）添加执行脚本命令
~~~~
/home/pi/test.py
~~~~