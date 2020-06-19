## 玩树莓派过程中遇到的一些问题和搜索到的解决办法


- 刚安装完新系统，通过HDMI线连接屏幕没有数据输出，显示no signal问题

解决办法:
1. 打开安装了树莓派官方系统的SD卡，在里面找到config.txt文件
2. 打开刚在文件，在里面找到这些:
~~~~
hdmi_safe=1
overscan_left=xxx
overscan_right=xxx
overscan_top=xxx
overscan_bottom=xxx
hdmi_group=xxx
hdmi_mode=xxx
hdmi_drive=xxx
~~~~
然后一一将前面的注释去掉即可。

- 无法安装aptitude

解决办法:


~~~~
1. 更新软件源
2. sudo apt-get update
3. sudo apt-get dist-upgrade
~~~~
>注意: 这样操作可能会使得卸载apt，卸载了apt之后非常麻烦(2020-6-19,暂未找到解决办法重新装回apt)
>

