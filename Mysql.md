# MySQL安装

```
#1.清理旧的mysql源
[root] rpm -qa|grep -i mysql
[root] yum -y remove mysql80-community-release-el8-1.noarch
#2.下载安装包到/usr/local/mysql
[root] wget https://dev.mysql.com/get/mysql80-community-release-el7-1.noarch.rpm
#3.安装yum repo并更新yum缓存
[root] rpm -Uvh mysql80-community-release-el7-1.noarch.rpm
#4.查看mysql yum仓库中的mysql版本
[root] yum repolist all | grep mysql
#5.启用MySQL5.7 禁用MySQL8.0
#  没有yum-config-manager命令则安装yum-utils(yum -y install yum-utils)
[root] yum-config-manager --disable mysql80-community
[root] yum-config-manager --enable mysql57-community
#  查看启用版本
[root] yum repolist enabled | grep mysql
#6.安装mysql
[root] yum install mysql-community-server
#7.开启并查看mysql服务，获取mysql初始化密码
[root] service mysqld start
[root] service mysqld status
[root] cat /var/log/mysqld.log | grep password
#8.登陆mysql并修改密码
mysql -uroot -p
mysql> set global validate_password_policy=LOW;
mysql> set global validate_password_length=4;
mysql> alter user 'root'@'localhost' identified by 'root';
#9.清理mysql源
[root] yum -y remove mysql80-community-release-el7-1.noarch
#10.防火墙设置永久启动并开放端口
[root] firewall-cmd --zone=public --add-port=3306/tcp --permanent
[root] systemctl enable firewalld.service
[root] firewall-cmd --reload
[root] firewall-cmd --quert-port=3306/tcp
#11.修改host，允许远程登陆
mysql> use mysql;
mysql> update user set host='%' where user='root';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'root' WITH GRANT OPTION;
mysql> flush privileges;
# 自定义mysql语句的结束符号
delimiter //
```

[firewall开放3306端口](https://www.cnblogs.com/huizhipeng/p/10127333.html)



>  修改用户密码

```mysql
第一种：set password for root@localhost password('root'); flush privileges;
第二种：mysqladmin -uroot -proot password
第三种：update mysql.user set authentication_string=password('root') where user='root' and host='localhost'; flush privileges;
```

> 忘记密码

修改/etc/my.cnf，在[mysqld]下面添加skip-grant-tables，重启mysql服务并重新登陆修改密码，然后恢复配置

> 用户管理

```mysql
# username	：用户名
# host		：本地使用localhost，任意主机登陆使用通配符%，指定网段：192.168.%.%
# password	：登陆密码
# 1.创建用户
create user 'username'@'host' identified by 'password';
# 2.查看权限
show grants for 'username'@'host';
# 3.删除用户
drop user 'username'@'host';
delete from mysql.user where name='username' and host='host';
```

> 权限管理

```mysql
# all privileges：所有权限
# *.*			：所有库所有表
# 对现有用户授权
grant grant1, grant2, ... on 数据库对象 to 'username';
# 创建用户并授权
grant grant1, grant2, ... on 数据库对象 to 'username'@'host' identified by 'password';
# 回收除登陆权限以外的权限
revoke grant1, grant2, ... on 数据库对象 from 'username'@'host';
```

# MySQL事务及视图

> 事务介绍

​		对数据库进行读或写操作的一个过程。有两个目的，第一个是为数据库提供了一个从失败中恢复到正常状态的方法，同时提供了数据库在异常状态下仍能保持一致性的方法；第二个是当多个应用程序在并发访问数据集时，可以在这些应用程序之间提供一个隔离方法，以防止彼此的操作相互干扰。

​		事务特性（ACID）：原子性(Automatic)一致性(Consistency)隔离性(Isolation)持久性(Durability)

​		使用事务时表的引擎必须为innodb引擎

> 事务的操作

事务的开启：begin;

事务的提交：commit;

事务的回滚：rollback;

> 事务自动提交

```mysql
# 查看自动提交
mysql> show variables like 'autocommit';
# 临时关闭自动提交
mysql> set autocommit=0;
# 临时开启自动提交
mysql> set autocommit=1;
# 永久修改自动提交
修改配置文件/etc/my.cnf在[mysqld]下添加autocommit=1;然后重启服务
```

> 修改表的引擎

```mysql
mysql> show engines;
mysql> alter table test engine='CSV';
```

> 视图介绍

​		视图（View）是一种虚拟存在的表，它是一个逻辑表，本身是不包含数据的，作为一个select语句保存在数据字典中。通过视图可以展现基表（用来创建视图的表base table）的部分数据，即视图的数据来源于基表。

​		视图的优点：简单、安全，数据独立，不占空间

​		视图的缺点：性能差、限制修改

> 视图的操作

```mysql
# 创建视图
mysql> create view <视图名称> as select 语句;
mysql> create view <视图名称> (字段) as select 语句;
mysql> create or replace view <视图名称>;
# 修改视图
mysql> alter view <视图名称> as select 语句;
# 删除视图
mysql> drop view <视图名称>;
```

# MySQL索引及存储引擎

> 索引介绍

​		索引是一个单独的，存储在磁盘上的数据结构，它们包含着对数据表里面的所有记录的引用指针，使用索引可以快速的找出在某列或多列由特定值的行

​		索引的优点：通过创建唯一索引，来保证数据表中的每一行数据的唯一性；可以加快数据的检索速度；

​		索引的缺点：索引需要占用物理空间；改动表中数据时，需要动态维护索引，降低了数据的维护速度；

​		常见的索引：

- index：普通索引，允许出现相同内容，可以为NULL

- unique：唯一索引，不可以出现相同内容，但是可以为NULL

- primary key：主键索引，每个表只能有一个主键索引，删除主键前必须先删除自增

- foreign key：外键索引

- full text：全文索引，词为单位，停止词（出现频率很高）对全文检索失效，char/varchar/text，忽略大小写

- 混合索引

```mysql
# 创建表时创建索引
mysql> create table name(..., unique(id));
# 添加索引；没有索引名称时会以默认的字段名为索引名称
mysql> alter table 表名 add index [索引名称] (字段名称);
# 直接创建索引
mysql> create index 索引名称 on 表名 (字段名称);
# 查看索引
mysql> show idnex from 表名\G
# 删除索引
mysql> drop index 索引名称 on 表名;
mysql> alter table 表名 drop index 索引名称;
# 删除自增
mysql> alter table test change id id int(17) unsigned zerofill not null;
# 全文检索
mysql> select * from 表名 where match (字段名) against ('检索内容');
mysql> select * from 表名 where match (字段名) against ('检索内容*' in boolean mode);
# +表示检索词1必须有，-表示检索词1必须无，检索词2可有可无
mysql> select * from 表名 where match (字段名) against ('+/-检索1 检索2' in boolean mode);
# 查匹配度
mysql> select id, match (字段名) against ('检索内容') from 表名;
```

> 存储引擎

​		数据库引擎是数据库底层软件组织，不同的存储引擎提供不同的存储机制，索引技巧，锁定水平等功能，使用不同的数据库引擎，可以获得特定的功能。

```mysql
# 查看存储引擎
mysql> show engines;
mysql> show create table name\G
# 查看当前库所有表状态
mysql> show table status\G
# 创建表时设置engine
mysql> create table name(...) engine='InnoDB';
# 修改表engine
mysql> alter table name engine='InnoDB';
# 修改默认引擎
修改配置文件/etc/my.cnf在[mysqld]下添加default-storage-engine='InnoDB';保存后重启服务
```

MyISAM   不支持事务、外键；表级锁；保存表的具体行数；奔溃恢复不好；支持全文索引（full text）

InnoDB    支持事务、外键；行级锁；不保存表的具体行数；奔溃恢复好；5.6版本以后支持全文索引；

​				  InnoDB在update不确定范围时做表级锁

> 联合索引
>

联合索引又称为组合索引或复合索引

```mysql
# 创建联合索引
mysql> alter table 表名 add index(字段1, 字段2, 字段3...);
# 删除联合索引
mysql> alter table 表名 drop 索引名称;
```

# MySQL慢查询及优化

```mysql
mysql> show variables like '%slow%';
mysql> set global slow_query_log = on;
mysql> show variables like '%slong%';
```

> 优化建议

1. 尽量避免使用 select * from，尽量精确到具体的字段
2. 尽量避免使用or，会使索引失效
3. 加上limit限制行数
4. 使用模糊查询时，%放在前面会使索引失效
5. 要注意条件类型的转换，会使索引失效

# MySQL备份

备份类型：完全备份、部分备份（增量备份(基于上次备份)、差异备份(基于首次备份)）

备份方式：逻辑备份（直接生产sql，效率低，节约空间）、物理备份（拷贝物理数据，速度较快，浪费空间）

备份场景：热备份（不影响读写操作）、温备份（不影响读操作）、冷备份（不允许读写操作）

```
mysql> mysqldump -u 用户 -h host -p 密码 daname table | gzip > dir
```



