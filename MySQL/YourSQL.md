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
select [distinct] * | 列名 from users where 条件;

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

- 条件查询

  通过order by语句，可以将查询的结果进行排序

  ~~~mysql
  select * from 表名 order by 排序字段 ASC|DESC; # (默认是asc)
  ~~~

- 聚合查询

  五个聚合查询的函数

  - count() 统计指定列不为null的记录行数
  - sum() 计算指定列的数值和，如果指定列不是数值类型，计算结果为0
  - max() 计算指定列的最大值，如果指定的列不是数值类型，那么使用字符串排序运算
  - min()  计算指定列的最小值，如果指定的列不是数值类型，那么使用字符串排序运算
  - avg() 计算指定列的平均值，如果指定列的类型不是数值类型，计算结果为0

  ~~~mysql
  # 主键可以作为统计的字段
  select count(pid) 
  from product;
  
  
  ## 当聚合sum累加，空值默认会隐式转换为0进行累加
  ## 如果字段是数字字符串，隐式转换为数字进行sum累加
  ## 如果当前字段是以数字开头的字符串，会截取到第一个不为数字的位之前作为数字进行sum累加
  ## 如果不是以数字开头的字符串，sum累加，等于0
  
  # 平均值
  select pname,avg(price)
  from product 
  group by pname;
  # 平均值 sum/count
  select pname,sum(price)/count(price)
  from product
  group by panme;
  ~~~

  ~~~mysql
  # 需求:将根据pname查询出来的最大的price对应的所有信息展示出来
  # 方法一：
  select a.* from product as a,
  (select pname,max(price) as max_price
  group by pname) as p
  where p.pname = a.pname and p.max_price = a.price;
  
  # 方法二:
  select p.* 
  from product as p
  where p.price=(
  	select max(price)
      from product
      where p.pname = product.pname
      group by pname
  )
  ~~~

- 分组查询

  使用group by语句对查询信息进行分组

  格式：

  ~~~mysql
  select 字段1，字段2... from 表名 group by 分组字段 having 分组条件
  ~~~

  - having与where的区别:
    - having 是在分组后对数据进行过滤，where是在分组前对数据进行过滤
    - having后面可以使用分组函数（统计函数），where后面不可以使用分组函数

    ~~~mysql
    select pname,count(1)
    from product 
    where pname = '海澜之家'
    group by pname
    having count(1)>1;
    ~~~

- 分页查询

  ~~~mysql
  SELECT 字段1，字段2... FROM 表名 LIMIT M,N
  M: 整数，表示从第几条索引开始，计算方式 （当前页-1）*每页显示条数
  N: 整数，表示查询多少条数据 offset 偏移量（每页显示多少条数据）
  SELECT 字段1，字段2... FROM 表名 LIMIT 0,5
  SELECT 字段1，字段2... FROM 表名 LIMIT 5,5
  #查询product表的前5条记录
  SELECT * FROM product LIMIT 0,5
  ~~~

  **重要实例：**

  ~~~mysql
  # 查询出每个产品中价格 price 排名第二的价位的信息，如果没有为 null , pname
  # 创建一个表，有两个字段 id salary (1,100)(2,200)(3,300)
  # 方法 1 不等于最大的情况，再求最大。
  select Max(salary)
  from tmp
  where salary not in (select Max(salary) from tmp);
  # 方法 2 从第二个取1个
  select salary from tmp order by salary limit 1,1;
  ~~~

- insert into select语句

  ~~~mysql
  INSERT INTO table2
  SELECT column_name(s)
  FROM table1;
  # 案例: 将数据 拷贝到另外一个表结构一样的数据表里。
  # 保证拷贝的目标表必须存在。
  insert into product2
  select * from product;
  ~~~

  ~~~mysql
  # 允许table2 不存在，直接创建表和数据
  CREATE TABLE table2 as
  SELECT column_name(s)
  FROM table1;
  # 案例： 创建一个 与 product 一样表结构的表和数据
  create table product2 as
  select * from product;
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

