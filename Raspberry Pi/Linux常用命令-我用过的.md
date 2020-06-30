# 常用命令

删除文件夹

- 1.删除文件夹下所有的文件和文件夹，不作任何提示
>说明： -r  向下递归，不管多少级目录，一并删除；-f 直接强行删除，不作任何提示
~~~~
rm -rf folderName
~~~~

- 2.删除文件
>说明: 文件filename.xxx将被强制删除
~~~~
rm-f /var/log/httpd/filename.xxx
~~~~

- 3.移动文件
>对于文件 源文件 转移至 目标文件夹
>对于文件夹 源文件夹 转移至 目标文件夹
~~~~
sudo mv source_folder_path destination_folder_path
~~~~

## 系统性

1. 显示文件列表命令
~~~~
ls 英文单词list的缩写

ls -a 显示指定目录下的所有目录与文件，包括隐藏文件
ls -l 以列表方式显示文件的详细信息
ls -h 配合-l以人性化的方式显示文件大小
~~~~
~~~~
ls #查看当前目录内容(缺点: 隐藏文件看不到)
ls -a #查看当前目录内容,包括隐藏文件
ls -al #查看目录内容的详细信息(查看文件类型、权限、大小等)
ls -lh #查看目录内容的详细信息,以K,M,G方式显示文件大小
ls /root #查看/root目录下内容
~~~~

2.目录查看、目录创建和目录删除
~~~~
pwd 查看当前工作目录
mkdir 创建文件夹
    mkdir -p /root/aaa/bbb 创建有层级的目录
rm -rf 删除目录  r是英文单词recursive的缩写，f是force的缩写，代表在文件夹里递归强制删除没有任何提醒，
~~~~
3.创建文件
~~~~
touch a.txt  在当前目录创建a.txt文件
touch /root/a.txt 在root文件夹下创建a.txt文件
~~~~

3.移动文件  
mv命令
~~~~
mv 源文件目录 目的文件目录
~~~~

也可以用来更改文件名
~~~~
mv 原名 更改后的名字
~~~~

4.查看文件
cat命令
~~~~
cat /root/initial-setup-ks.cfg
~~~~

5.复制命令
cp命令
~~~~
cp a.txt dir1 #将a.txt复制到dir1目录
cp a.txt b.txt #将a.txt复制到b.txt
~~~~

6.压缩与解压缩
tar命令
~~~~
参数     解释
-c    创建一个新tar文件
-v    显示运行过程的信息
-f    指定文件名
-z    调用gzip压缩命令进行压缩
-t    查看压缩文件的内容
-x    解开tar文件
~~~~

6.1 解压
~~~~
tar -zxvf 压缩文件[-C] [指定解压目录]

tar -zxvf redis-3.2.8.tar.gz #将文件解压到当前目录
tar -zxvf redis-3.2.8.tar.gz -C /root/dir #将文件解压到指定目录
~~~~
6.2压缩
~~~~shell
tar -c[z]vf 压缩文件目录

tar -cvf test.tar /root/test #打包
tar -czvf test.tar.gz /root/test #打包并压缩
~~~~

7.文件查找
7.1 find命令
用于查找符合条件的文件

~~~~shell
find / -name 'ins*' #查找/目录下以文件名ins开头的文件
find / -type f -size +100M #查找/目录下文件大小大于100M的文件
find / -type f -size +100M -size -200M #大于100M且小于200M的文件

-type后的参数f是指文件，同样可以用d指文件夹，l指链接
~~~~
locate命令

> locate不能检索 **/tmp或者media**文件夹下的文件
> locate的查找需要给一个**绝对路径**，不能是相对路径(因为数据库里的存储的路径都是绝对路径，没有办法从任何位置查找相对路径)

~~~shell
先updatedb更新一下数据库
再：
locate -i /home/itcast/aa/app.sh # -i参数代表不区分大小写
locate -i /home*app.sh* # 查找带app的文件，模糊查询

> locate不能检索 /tmp或者media文件夹下的文件
> locate的查找需要给一个绝对路径，不能是相对路径(因为数据库里的存储的路径都是绝对路径，没有办法从任何位置查找相对路径)
~~~

whereis命令

只能搜索文件名，且是二进制文件

~~~shell
whereis grep #grep: /usr/bin/grep /usr/share/man/man1/grep.1.gz /usr/share/man/man1p/grep.1p.gz
~~~

7.1 grep命令
用于对文件进行文本查询

~~~~shell
grep lang anaconda-ks.cfg #在文件中查找lang
grep a anaconda-ks.cfg --color #在文件中查找a,高亮显示

cat hello |grep hello # 先查看当前文件的内容，然后在其内容中查找指定的字符串
~~~~

8.tail和head命令

查看文件最后n行的内容

~~~~shell
tail -n10 /app/log/acess.log # 查看文件最后10行的内容
如果文件一直在变化，想查看最新的最后n行的内容
tail -f /app/log/acess.log # 查看最新的动态的日志文件内容（一直显示最后n行）

head -n10 /app/log/acess.log # 查看最早的10行日志文件内容
~~~~

8.1 more和less命令

more可以分页显示文件的内容，一般是往下，**space**往下，按**b**往上翻页

~~~~shell
more logname.log
~~~~

less分页查看文件内容，可以通过方向键控制

~~~shell
less logname.log
~~~



### 系统管理

1.linux命令之系统管理

~~~~shell
ps #显示和终端有关的命令，是英文单词process status的缩写
ps -ef # 查看系统启动了的所有线程
ps -ef |grep firefox # 查看当前有无Firefox的进程
ps -aux | grep firefox # 查看进程的详细信息
~~~~

2.结束进行kill命令

~~~shell
kill -9 PID # pid是当前进程的id，不建议在生产环境使用此命令，可能会导致崩溃
# 这里的-9是指信号量SIGKILL，详情可以见kill -l

killall firefox # 通过程序名称杀掉程序进程
~~~



3.管道命令“|”

将一个命令的输出用作于另一个命令的输入

~~~shell
ps -ef | grep firefox # 在当前的进程中查找firefox的进程
cat aa/hellword.md | grep hello | wc -l # 查看hellowword.md文件里面有多少个hello
~~~



4.用户的创建与删除

**创建**用户useradd

~~~~shell
useradd itheima # 创建名为itheima的用户
passwd itheima # 为itheima用户设置密码

whoami # 查看当前用户是谁
~~~~

root用户和普通用户的区别

>1.root用户文件夹在根目录下/root，而普通用户是在/home/用户名下
>
>2.root用户的命令行符号是#，而普通用户的是$
>
>3.主机前@用户名不同

**删除**用户userdel

~~~shell
userdel -r itheima # 删除用户及递归删除指定用户下的所有文件/文件夹
#Note：如果当前的进程被占用，需要终止进程再删除用户 ，谨慎操作
~~~

root用户与普通用户的切换

~~~shell
su root # 从当前用户切换到root用户，需要输入密码
su itheima # 切换回之前的用户，不需要密码，快捷键 ctrl+D，快速切换回之前的用户，退出root用户
~~~

### 文件权限更改

属主u，组内g，其他用户o

1.chmod命令

~~~shell
chmod u+x helloword.md # 让属主用户拥有helloword.md的可执行权限
chmod g+w+x /home/itcast/aa/helloword.md # 将helloworld.md修改为所属分组添加可读写修改的权限
chmod o-r /home/itcast/aa/helloword.md #让其他用户没有helloworld的可读权限
chmod 777 /home/itcast/aa/helloword.md # 让所有用户都拥有hellowordld.md的可读写可执行权限
chmod 7 /home/itcast/aa/helloword.md # 相当于007
chmod g=w+x /home/itcast/aa/helloword.md # 让所属组内用户拥有helloword.md的可写可执行权限
chmod u=r+w,g=r,o=r /home/itcast/aa/helloword.md # 相同与644
~~~

### 网络和服务管理

~~~~shell
systemctl set-hostname node1
~~~~



~~~shell
service network restart # 重新启动网络服务
service mysqld restart # 重启mysql
service network status # 查看网络服务的状态
~~~

### 其他命令

Linux命令创建软连接（相当于Windows中创建快捷方式）

**ln命令**

源文件路径一定要是**绝对路径**

~~~shell
ln -s /usr/bin/ls  /home/itcast/aa/ls # 将ls命令生成软连接发送到itcast的aa目录下，软链接的名称是ls

~~~

<img src="C:\Users\rooho\AppData\Roaming\Typora\typora-user-images\image-20200630145001618.png" style="zoom: 67%;" />

三个地方的文件都是同样的大小，占据同样大小的内存，任何一个位置改变，另外的位置该文件都会同步改变。如果采用拷贝，则不能达到这样的效果。

### vi/vim编辑器

1.设置行号

~~~vim
set nu或者是set number
~~~

2.进入文件的第n行

~~~shell
vi/vim 文件名 +10 # 进入文件的第10行
~~~

3.进入末行模式

~~~shell
:
~~~

4.进入编辑模式

~~~shell
输入i或者insert或者双击键盘上的字母
~~~

5.进入命令模式

~~~shell
Esc
~~~

常用命令

~~~shell
命令    功能
o     在当前行后面插入一空行
O     在当前行前面插入一空行
dd     删除光标所在行
ndd   从光标位置向下连续删除n 行
yy    复制光标所在行
nyy   从光标位置向下连续复制n行
p     粘贴
u     撤销上一次命令
gg    回到文件顶部
G     回到文件末尾
/str  查找str
~~~

末行模式命令

![image-20200630150934034](C:\Users\rooho\AppData\Roaming\Typora\typora-user-images\image-20200630150934034.png)