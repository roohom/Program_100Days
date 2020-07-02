# YourSQL

## 表的字段约束

- unsigned  无符号，给数值类型使用表示为正数，不写可以表示正负数
- 字段类型后面加括号限制宽度
  - char(5), varchar(7)，在字符类型后面加限制 表示字符串的长度
  - int(4)没有实际意义，默认无符号的int为int(11)，有符号的int为int(10)
  - int(4) unsigned zerofill只有当给int类型设置前导零时，设置int的宽度才会有实际意义
- not null 不为空
- default 设置默认值
- primary key 主键不能为空，且唯一，一般和自动递增一起配合使用
- auto_increment 定义列为自增属性，一般用于主键，数值会自动增加1
- unique 唯一索引(数据不能重复: 用户名)可以增加查询速度，但是会降低插入和更新速度



## 运算符

- 数据库特有的比较：in , not in, is null, is not null, like, between, and
  - in(22,25) 等价于 >=22 and <=25 
- like :支持特殊符号%和_;

>其中%表示任意数量的任意字符，_表示任意一位字符

## 主键

1.表中每一行都应该有可以唯一标识自己的一列，用于记录两条记录不能重复，任意两行都不具有相同的主键值

2.应该总是定义主键，虽然并不总是都需要主键，但大多数据库设计人员都应该保证他们创建的每一个表都具有一个主键，以便于以后的数据操作和管理。

### 要求

- 记录一旦插入到表中，主键最好不要修改

- 不允许null

- 不在主键列中使用可能会更改的值

  >例如，如果使用一个名字作为主键以标识某个供应商，当该供应商合并和更改其名字时，必须更改这个主键

- 自增整数类型：数据库会在插入数据时自动为每一条记录分配一个自增整数，这样我们就完全不用担心主键重复，也不用自己预先生成主键

- 可以使用多个列作为联合主键，但蓝河主键并不常用，使用多列作为主键时，所有列值的组合必须是唯一的



## MySQL数据库与数据表操作

- 数据库的操作

1.创建数据库

~~~mysql
create database if not exists 库名 default charset=utf8;
~~~

2.查看所有数据库

~~~mysql
show databases;
~~~

3.打开/使用/进入库

~~~mysql
use 库名;
~~~

4.删除数据库

~~~mysql
drop database 库名;
~~~

5.查看正在试用的数据库

~~~mysql
select database();
~~~





- 数据表的操作

1.创建表

~~~mysql
create table 表名(字段名， 类型， [字段约束]，...)

类型:
	varchar(n) 字符串
	int        整形
	double     浮点
	date       时间
	timestamp  时间戳
约束:
primary key    主键，被主键修饰字段中的数据，不能重复，不能为null
~~~

实例:

~~~mysql
create table users(
	id int unsigned not null primary key auto_increment,
    username varchar(5) not null,
    password char(32) not null,
    age tinyint not null default 20
)engine=innodb default charset=utf8;

# 查看表结构
desc 表名;

# 查看建表语句
show create table 表名;

~~~

2.修改表结构

>语法格式: alter table 表名 action(更改的选项)

- 添加字段

  ~~~mysql
  # 语法： alter table 表名 add 添加的字段信息
  alter table users add num int not null;
  
  # 在users表中age字段后面添加一个email字段
  alter table users add email varchar(50) after age;
  
  # 在指定字段之前添加字段，在users表中email字段前面添加一个phone
  alter table users add phone char(11) not null after age;
  
  # 在表的最前面添加一个字段
  alter table users add aa int first;
  ~~~

- 删除字段

  ~~~mysql
  # 删除字段 alter table 表名 drop 被删除的字段名
  alter table users drop aa;
  ~~~

  

- 修改字段

  ~~~mysql
  语法格式： alter table 表名 change|modify 被修改的字段信息
  change: 可以修改字段名
  modify: 不能修改字段名，只能修改字段的相关信息
  
  # 修改表中的num字段，类型,不修改表名
  alter table users modify num tinyint not null default 12;
  
  # 修改表中的num字段为int并且字段名为nn
  alter table users change num nn int;
  ~~~

  >注意：一般情况下无特殊要求，不要轻易修改表结构

3.修改表名

~~~mysql
语法: 
alter table 原表名 rename as 新表名;
rename table 原表名 to 新表名;
~~~

4.更改表中的自增的值

~~~mysql
# 在常规情况下，auto_increment默认情况下从1开始连续递增
alter table users auto_increment = 1000;
~~~

5.修改表引擎

~~~mysql
# 推荐在定义表时，表引擎为innodb
mysql> show create table stu\G;
*************************** 1. row ***************************
       Table: stu
Create Table: CREATE TABLE `stu` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(5) NOT NULL,
  `password` char(32) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `age` tinyint(4) NOT NULL DEFAULT '20',
  `nn` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
1 row in set (0.00 sec)

ERROR:
No query specified

# 查看当前数据库下制定表的存储引擎
show table status from 库名 where name='users';

# 修改表引擎
alter table users engine = 'myisam';
~~~

6.删除表

~~~mysql
drop table 表名;
~~~

7.查找表

~~~mysql
查看当前数据库中的所有表:
show tables;

查看当前表的结构:
desc 表名
~~~



## 数据操作DML

>数据的DML操作：添加数据、修改数据、删除数据

添加数据

~~~mysql
# 标准添加
insert into 表名 (字段名1，字段名2，字段名3，...) values(字段值1，字段值2，字段值3，...)

# 批量添加
  insert into 表名 values
->(字段值,.....)，
->(字段值,.....)，
->(字段值,.....)，
->(字段值,.....);
或者:
  insert into 表名 values(值1，值2，值3...)
~~~

修改数据

~~~mysql
update 表名 set 字段名=值 where 条件
~~~

删除数据

~~~mysql
# delete 删除表数据比较慢，属于DML操作，在删除的时候会创建日志，可以回滚
# truncate 删除表是表级别的操作，属于DDL操作，删除速度较快不可回滚
delete from 表名 where 条件
truncate table 表名;
~~~

## 数据查询DQL

- 语法格式

~~~mysql
select 字段列表|* from 表名 [options]
options：
[where 搜索条件]
[group by 分组字段 [having 分组条件]]
[order by 排序字段 排序规则]
[limit 分页参数]
~~~

- 基础查询

~~~mysql
# 查询表中所有列所有数据
select * from users;

# 指定字段列表进行查询
select id,name,phone from users;
~~~

- where条件查询

  - 可以在where子句中指定任何条件
  - 可以使用and或or指定一个或多个条件
  - where也可以运用在update和delete后
  - where子句类型程序语言中if条件，根据mysql表中的字段值来进行数据的过滤

  ~~~mysql
  select * from users where age > 22;
  ~~~

  

## SQL约束

### 主键约束

- primary key约束唯一标识数据库表中的每条记录
  - 主键不能为空
  - 主键必须唯一
  - 每张表只能有一个主键

~~~mysql
create table if not exists stu(
    id int primary key ,
    num int(10),
    home_city varchar(50)
);

create table if not exists student(
    id int,
    num int(10),
    home_city varchar(50),
    constraint p_id primary key (id)
);

alter table stu add primary key (id);
~~~

- 删除主键约束

~~~mysql
alter table stu drop primary key;
~~~

- 自动增长列auto_increment

自动增长列类型必须是整形，自动增长列必须为键(一般为主键)

~~~mysql
设置自动增长列的起始值
alter table 表名 auto_increment = 1000;
~~~



- 非空约束not null

指定的字段的值不接受null空值

- 唯一约束
  - unique约束唯一标识数据库中的每条记录
  - unique和primary key约束均为列或集合提供了唯一性的保证
  - primary key拥有自动定义的unique约束

> 注意: 每个表可以有多个unique约束，但是每个表只能有一个primary key约束

~~~mysql
# 创建带unique约束的表
表内添加:
create table if not exists test(
    id int primary key auto_increment ,
    name varchar(50),
    num int(10) unique
);

表外添加:
alter table test change id id int(4) unique ;
或者: 
alter table test add unique (num);
~~~

删除唯一约束:

~~~mysql
alter table test drop index num;
~~~

