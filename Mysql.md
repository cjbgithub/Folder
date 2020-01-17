# MySQL安装

```python
#1.清理旧的mysql源
rpm -qa|grep -i mysql
yum -y remove mysql80-community-release-el8-1.noarch
# 2.下载安装包到/usr/local/mysql
wget https://dev.mysql.com/get/mysql80-community-release-el7-1.noarch.rpm
# 3.安装yum repo并更新yum缓存
rpm -Uvh mysql80-community-release-el7-1.noarch.rpm
# 4.查看mysql yum仓库中的mysql版本
yum repolist all | grep mysql
# 5.启用MySQL5.7 禁用MySQL8.0
#   没有yum-config-manager命令则安装yum-utils(yum -y install yum-utils)
yum-config-manager --disable mysql80-community
yum-config-manager --enable mysql57-community
#   查看启用版本
yum repolist enabled | grep mysql
# 6.安装mysql
yum install mysql-community-server
# 7.开启并查看mysql服务，获取mysql初始化密码
service mysqld start
service mysqld status
cat /var/log/mysqld.log | grep password
# 8.登陆mysql并修改密码
mysql -uroot -p
mysql> set global validate_password_policy=LOW;
mysql> set global validate_password_length=4;
mysql> alter user 'root'@'localhost' identified by 'root';
```























































