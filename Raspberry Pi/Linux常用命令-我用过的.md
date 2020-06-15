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
