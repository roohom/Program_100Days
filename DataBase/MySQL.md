# MySQL基本知识

#### 常用命令：

1. 查看当前mysql中的所有的库  

   > show databases;

2. 选择需要操作的库，打开库

   > use mysql;

3. 查看当前库中的所有数据表

   > show tabls;

4. 查看表中的数据：

   >select * from user; -->查看user表中所有数据的所有字段（数据很多很乱，看不清）

   > 查看user表中的所有数据的host和user字段列

   > select host, user from user



**库就像是文件夹，库中有很多个表，表就像我们的excel表格文件一样，每一个表中都可以存储很多数据**

MySQL中可以有很多不同的库，库中可以有很多不同的表，表中可以定义不同的列（字段），表中可以根据结构去存储很多的数据。



如何创建自己的库？

create database 库名 default charset=utf8；

~~~~nysql
创建表的语法：

create database 表名(
    字段名 类型 字段约束
    字段名 类型 字段约束
    字段名 类型 字段约束
    字段名 类型 字段约束
)engine==innodb default charset=utf8；
~~~~







添加数据：

insert into user(name, age, sex) values('admin', 26, '男')；



总结：

认识库、表的概念和关系

mysql的基本命令：登录，查看库，选择库，创建表，添加数据，查询数据。



## 基础操作命令

### 1.数据库操作

~~~~
查看数据库 -> show database;
创建数据库 -> create database 库名 default charset=utf8;
删除数据库 -> drop database 库名;
打开数据库 -> use 库名;
~~~~



### 2.数据表操作

~~~~mysql
查看表 show tables;

创建表 create table 表名(字段名1 类型，字段名2 类型)engine=innodb default charset=utf8；   ->如果表不存在就创建表，如果存在就不执行命令
create table if not exists 表名(字段1 类型，字段2 类型)；

create table if not exists users(
    id int not null primary key auto_increment,
    name varchar(4) not null,
    age tinyint,
    sex enum('男','女')
)engine=innodb default charset=utf8;

删除表： drop table 表名;

表结构：desc 表名;

查看建表语句: show create table users(表名);

~~~~



### 3.记录操作 增删改查

**增：**

~~~~mysql
insert into 表名(字段1,字段2,字段3) values(值1,值2,值3);
insert into 表名(字段1,字段2,字段3) values(a值1,a值2,b值3),(b值1,b值2,b值3);
~~~~

**删：**

~~~~mysql
delete from 表名 where 字段=某个值;
~~~~

**改：**

~~~~mysql
update 表名 set 字段=某个值 where 条件;
update 表名 set 字段1=值1,字段2=值2 where 条件;
update 表名 set 字段=字段+值 where 条件;
~~~~

**查：**

~~~~mysql
select * from 表名;
select 字段1,字段2,字段3 from 表名;
select * from 表名 where 字段=某个值;
~~~~



总结：

增：insert into （where）

删：delete from (where)

改：update ... set...   (where)

查：select from    (where)

