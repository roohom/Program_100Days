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
~~~~
tar -c[z]vf 压缩文件目录

tar -cvf test.tar /root/test #打包
tar -czvf test.tar.gz /root/test #打包并压缩
~~~~