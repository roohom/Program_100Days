# YourSQL

> 更多的数据库操作和使用规范访问[MySQL](https://mysql.com/)

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

### 数据库的操作

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





### 数据表的操作

#### 创建表

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

#### 修改表结构

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

#### 修改表名

~~~mysql
语法: 
alter table 原表名 rename as 新表名;
rename table 原表名 to 新表名;
~~~

#### 更改表中的自增的值

~~~mysql
# 在常规情况下，auto_increment默认情况下从1开始连续递增
alter table users auto_increment = 1000;
~~~

#### 修改表引擎

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

#### 删除表

~~~mysql
drop table 表名;
~~~

#### 查找表

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

### 多表操作

> category分类表，为一方，也就是主表，必须提供主键cid
>
> products商品表，为多方，也就是从表，必须提供外键category_id

实例：

~~~mysql
CREATE TABLE category (
cid VARCHAR(32) PRIMARY KEY ,
cname VARCHAR(50)
);
CREATE TABLE products(
pid VARCHAR(32) PRIMARY KEY ,
pname VARCHAR(50),
price INT,
flag VARCHAR(2), #是否上架标记为：1表示上架、0表示下架
category_id VARCHAR(32),
CONSTRAINT products_fk FOREIGN KEY (category_id) REFERENCES category (cid)
);
~~~

实例操作：

~~~mysql
#1 向分类表中添加数据
INSERT INTO category (cid ,cname) VALUES('c001','服装');
#2 向商品表添加普通数据,没有外键数据，默认为null
INSERT INTO products (pid,pname) VALUES('p001','商品名称');
#3 向商品表添加普通数据，含有外键信息(category表中存在这条数据)
INSERT INTO products (pid ,pname ,category_id) VALUES('p002','商品名称2','c001');
笛卡尔积（了解）
一般情况下，没有任何意义。
内连接
左右表能关联上的数据显示出来，否则不显示。
#4 向商品表添加普通数据，含有外键信息(category表中不存在这条数据) -- 失败,异常
INSERT INTO products (pid ,pname ,category_id) VALUES('p003','商品名称2','c999');
#5 删除指定分类(分类被商品使用) -- 执行异常
DELETE FROM category WHERE cid = 'c001';
~~~



- 内连接

  左右表能关联得上的显示出来，否则不显示。

  分为**显示内连接**和**隐式内连接**

~~~mysql
# 隐式内连接
# 语法格式：
select * from A,B where 条件;
# 案例：
select *
from category c,product p
where c.cid = p.category_id
外连接
左外连接 left [outer] join
获取到左表中所有右表不符合条件的数据，此时关联不上的字段为空。
右外连接 right [outer] join
获取右表中的所有左表不符合条件的数据，此时关联不上的字段为空。
3. 多表查询
# 显示内连接
#语法格式
select * from A inner join B on 条件;
# 案例：
select *
from category c [inner] join product p on c.cid = p.category_id
# 注： inner 可以省略
~~~

- 外连接

  - 左外连接

    获取到左表中所有右表不符合条件的数据，此时关联不上的字段为空。

    ~~~mysql
    # 语法格式
    select * from A left outer join B on 条件;
    # 案例
    select * from category c
    left [outer] join products p
    on c.cid = p.category_id
    ~~~

  - 右外连接

    获取右表中的所有左表不符合条件的数据，此时关联不上的字段为空。

    ~~~mysql
    # 语法格式
    select * from A right outer join B on 条件;
    # 案例
    select * from category c
    right [outer] join products p
    on c.cid = p.category_id
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

### 基础查询

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


### 聚合查询

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



### 分组查询

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


### 多表查询

- 子查询

  子查询：一条select语句结果作为另一条select语法一部分（查询条件，查询结果，表等）。
  select ....查询字段 ... from ... 表.. where ... 查询条件

  ~~~mysql
  # 案例1
  select a.* from product a,
  (select pname,max(price) max_price
  from product
  group by pname) as p
  where p.pname=a.pname and p.max_price=a.price;
  # 案例2
  select p.*
  from product p -- 检索 product
  where p.price=( -- 过滤 price = max(price)
  select max(price) -- 根据分组计算出最大的 price
  from product
  where p.pname = product.pname -- price = max(price) and 都是海澜之家
  group by pname
  );
  # 案例3
  # 需求 查询出来分类为化妆品的所有商品
  SELECT * FROM products p
  WHERE p.category_id =
  (
  SELECT c.cid FROM category c
  WHERE c.cname='化妆品'
  );
  # 案例4
  # 需求，查询出来分类为化妆品或者服饰的所有商品
  SELECT * FROM products p
  WHERE p.category_id in
  (
  SELECT c.cid FROM category c
  WHERE c.cname='化妆品' or c.cname='服饰'
  );
  # 案例5
  # 需求，通过子查询 隐式内连接查询所有化妆品的所有商品
  SELECT * FROM products p ,
  (SELECT * FROM category WHERE cname='化妆品') c
  WHERE p.category_id = c.cid;
  ~~~

## MySQL索引

> 索引是 MySQL 中一种十分重要的数据库对象。它是数据库性能调优技术的基础，常用于实现数据的快速检索。
>
> 索引就是根据表中的一列或若干列按照一定顺序建立的列值与记录行之间的对应关系表，实质上是一张描述索引列的列值与原表中记录行之间一一对应关系的有序表。

### 概述

在 MySQL 中，通常有以下两种方式访问数据库表的行数据：

- 1) 顺序访问
  顺序访问是在表中实行全表扫描，从头到尾逐行遍历，直到在无序的行数据中找到符合条件的目标数
  据。这种方式实现比较简单，但是当表中有大量数据的时候，效率非常低下。
- 2) 索引访问
  索引访问是通过遍历索引来直接访问表中记录行的方式。使用这种方式的前提是对表建立一个索引，在
  列上创建了索引之后，查找数据时可以直接根据该列上的索引找到对应记录行的位置，从而快捷地查找
  到数据。索引存储了指定列数据值的指针，根据指定的排序顺序对这些指针排序。

索引分类

- B-树索引
- 哈希索引
- 普通索引
- 唯一性索引
- 主键索引

### 索引的操作

- 普通索引的格式

  ~~~mysql
  #1 直接新增索引
  CREATE INDEX indexName ON mytable(username([length]));
  # 案例
  create index idx_product_categoryId on products(category_id);
  #2 通过修改表结构创建索引
  # 修改表结构
  ALTER table tableName ADD INDEX indexName(columnName)
  # 案例
  alter table products add index idx_product_categoryId (category_id);
  # 创建表结构时候直接创建索引
  CREATE TABLE mytable(
  ID INT NOT NULL,
  username VARCHAR(16) NOT NULL,
  INDEX indexName(username(length))
  );
  ~~~

- 查看索引信息

  ~~~mysql
  # 通过元数据信息及索引的名称获取索引信息。
  select * from information_schema.INNODB_INDEXES where
  NAME='idx_product_categoryId';
  # 查看某张表比如 product 表的索引信息。
  show index from products;
  ~~~

- 删除索引

  ~~~mysql
  #1 根据指定的索引名称删除索引
  DROP INDEX [indexName] ON mytable;
  ## 案例：
  drop index idx_product_flag on products;
  #2 通过修改表结构来删除索引
  alter table mytable drop index indexName;
  ## 案例：
  alter table products drop index idx_product_flag;
  ~~~

- 创建唯一索引

  ~~~mysql
  #1 直接新增索引
  CREATE UNIQUE INDEX indexName ON mytable(username([length]));
  # 案例
  create unique index idx_uniq_hashcode on products(`hashcode`);
  #2 通过修改表结构创建索引
  # 修改表结构
  ALTER table tableName ADD UNIQUE INDEX indexName(columnName)
  # 案例
  alter table products add unique index idx_uniq_hashcode (hashcode);
  # 创建表结构时候直接创建索引
  CREATE TABLE mytable(
  ID INT NOT NULL,
  username VARCHAR(16) NOT NULL,
  UNIQUE [INDEX] indexName(username(length))
  );
  ~~~

- 删除索引

  ~~~mysql
  #1 根据指定的索引名称删除索引
  DROP INDEX [indexName] ON mytable;
  # 案例：
  drop index indexName on mytable;
  #2 通过修改表结构来删除索引
  alter table mytable drop index indexName;
  # 案例：
  alter table products drop index idx_uniq_hashcode;
  ~~~

> 在唯一索引中
>
> ~~~mysql
> unique not null 等价于 primary key
> ~~~

### 索引的使用原则和注意事项

- 占空间
- 需要维护，维护需要成本（时间成本、资源成本）

### 应用场景

1.多表关联，使用on，关联操作时需要建索引；

2.where条件，过滤<,<=,=,>=,between,in以及某些时候的like(不以通配符%或_开头的情形)

~~~mysql
#1 建立索引
select * from user u where u.name in ('王','李');
#2 建立索引
select pid,price,category_id
from product p
where p.price in ( -- 普通索引
select price from t_product_price where price >200
);
~~~

3.查看执行计划

~~~mysql
explain select * from category c inner join products p on c.cid =
p.category_id
~~~

## MySQL开窗函数

## SQL约束

### 表的字段约束

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

### 外键约束

~~~mysql
语法：
alter table 从表 add [constraint] [外键名称] foreign key (从表外键字段名) references

主表 (主表的主键);
[外键名称] 用于删除外键约束的，一般建议“_fk”结尾
alter table 从表 drop foreign key 外键名称
~~~

> 注意：
>
> 主表没有建立主键，需要先创建主表的主键，然后才能创建从表外键约束。
> 创建外键的目的： 保证数据完整性
> 不能在从表中添加主表中关联的cid不存在的分类。



## MySQL数据库导入导出和权限管理

### 数据的导入导出

- MySQL数据库数据的导出

  ~~~shell
  # 只在shell端，不进入mysql
  # 键入以下命令
  mysqldump -u root -p 库名 > ~/地址/名称
  ~~~

  导出一个库中所有数据，会形成一个建表和添加语句组成的sql文件

- 将数据库中的表导出

  ~~~shell
  mysqldump -u root -p 库名 表名 > ~地址/名称
  ~~~

  

- 数据导入

  把导出的sql文件数据导入到数据库中

  - 先进入到数据库中创建一个库用来接收你想导入的数据

  - 退出mysql

  - ~~~shell
    mysql -u root -p 你刚才建的库 <  文件名
    ~~~

### 权限管理

> root用户是数据库红权限最高的用户
>
> 可以创建不同的用户，或者项目，创建不同的mysql用户，并适当地授权，完成数据库的相关操作
>
> 这样就一定程度上保证了数据库的安全

- 创建用户

  ~~~mysql
  grant授权的操作 on 授权的库.授权的表 to 账户@登录地址 identified by '密码'；
  
  # 在mysql中创建一个叫 baicai 的用户，并赋予其在yoursql数据库对所有表中进行 增和查 的权限
  grant select, insert on yoursql.* to baicai@'%' identifid by '123456' # % 代表登录地址不限
  
  # 给用户 huacai 密码 123456 对yoursql数据库中所有表所有的操作权限
  grant all on yoursql.* to huacai@'%' identified by '123456'
  
  # 删除用户
  drop user 'huacai'@'%'
  ~~~

  

## Python操作数据库

> 使用pymysql包
>
> 详情历程可以见：[Pymysql](https://pypi.org/project/PyMySQL/)

- 大致流程

  - 1.链接mysql数据库
  - 2.创建游标对象
  - 3.准备sql
  - 4.用游标对象执行sql
  - 5.提取结果
  - 6.关闭数据库连接

  

> 连接mysql数据库时，cursorclass = pymysql.cursors.DictCursor可以把结果转为字典类型，默认为元组

~~~python
import pymysql.cursors

# Connect to the database
# 连接mysql数据库
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
# 2.创建游标对象
cursor = connection.cursor()

# 3.准备sql语句
sql = "select version()"

# 4.执行sql语句
cursor.execute(sql)

# 5.提取结果 fetchall() 提取所有的结果 fetchone() 提取一条结果
data = cursor.fetchall()

# 6.关闭数据库连接
connection.close()

# 将获取到的数据输出
print(data)
~~~

