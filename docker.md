# docker命令

1. 基本命令

```shell
# 输出hello-world
$ docker run hello-world
# docker run 启动一个应用容器并输出hello-world
$ docker run ubuntu:15.10 /bin/echo "hello-world"
  - docker						Docker的二进制执行文件
  - run							与Docker组合来运行一个容器
  - ubuntu:15.10				指定运行的镜像，先从本地主机上查找，不存在从镜像仓库下载
  - /bin/echo "hello-world"		在启动的容器里面执行命令
# 运行交互式容器
$ docker run -i -t ubuntu:15.10 /bin/bash
  - t	在新容器内指定一个伪终端或终端
  - i	允许你对容器内的标准输入（STDIN）进行交互
# exit 命令或者 ctrl+D 来退出容器

# 创建以进程方式运行的容器，下面命令会输出容器ID
$ docker run -d ubuntu /bin/sh -c "while true; do echo hello world; sleep 1; done"
bf5af6860d62e38d58eadd4c620206dfbd2945e9abfa447823fadba48f52fa14

# 常看容器
$ docker ps
CONTAINER ID :  IMAGE :    COMMAN   :     CREATED    : STATUS PORTS  : NAMES
95e4b406aacc : ubuntu : "/bin/bash" : 44 minutes ago : Up 44 minutes : youthful_nash
5223501a0900 : ubuntu : "/bin/sh -" : 2 hours ago    : Up 2 hours    : suspicious_dhawan
  - CONTAINER ID：容器ID
  - NAMES：自动分配的容器名称

# 查看容器内的标准输出
$ docker logs 5223501a0900
$ docker logs suspicious_dhawan
hello world
hello world
hello world
...

# 停止容器
$ docker stop 5223501a0900
$ docker stop suspicious_dhawan
suspicious_dhawan
```



```shell
# 查看Docker客户端的所有命令
$ docker

# docker command --help 查看更加具体的Docker命令使用方法
$ docker stats --help

# dcoker容器中运行一个Python Flask应用来运行一个web应用
$ docker pull training/webapp # 载入镜像
$ docker run -d -P training/webapp python app.py
  - d：让容器在后台运行
  - P：将容器内部使用的网络端口映射到我们使用的主机上

# 查看WEB应用容器（多了端口信息，Docker开放5000端口（默认Python Flask端口）映射到主机端口32769上）
$ docker ps

# 可以通过-p参数类设置不一样的端口(容器内部的5000端口映射到我们本地主机的5000端口上)：
$ docker run -d -p 5000:5000 training/webapp python app.py



```





2. 镜像

```shell
$ docker run -t -i ubuntu /bin/bash
```

3. 安装ssh

```shell
root@95e4b406aacc:/# apt-get update -y
root@95e4b406aacc:/# apt-get install -y openssh-client openssh-server
# 允许root用户登陆
root@95e4b406aacc:/# sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
# 登陆密码验证
root@95e4b406aacc:/# sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/g' /etc/ssh/sshd_config

root@95e4b406aacc:/# mkdir /var/run/sshd
# 修改root用户的密码
root@95e4b406aacc:/# echo "root:123456" | chpasswd
# 启动ssh
root@95e4b406aacc:/# /usr/sbin/sshd
# 退出
root@95e4b406aacc:/# exit
```



4. 保存镜像

```shell
# 停止容器
$ docker stop a0fae1aa65a6
a0fae1aa65a6
# 保存镜像
$ docker commit a0fae1aa65a6 wanda_ubuntu
sha256:f56761ac8d3267afba466249e4a66fc61245d72668975f2e48b42e09cc5b5f15
# 删除容器
$ docker rm a0fae1aa65a6
# 重新创建容器
$ docker run -i -t -d --privileged -p 55402:22 -p 80:80 --name wanda_ubuntu_1 wanda_ubuntu:latest /usr/sbin/sshd -D
```

5. 安装依赖包

**sudo必须安装**

```shell
# 确认系统更新到最新

# 由于ubuntu安装的是vimrc.tiny，所以删除该版本，安装vim full版本

# vi打开utf-8文件乱码的解决方案

# 显示行号

# 安装依赖包

# 安装git

# 确认git版本在1.7.10以上


```

6. 安装Ruby

```shell



# 安装bundler，一个安装ruby的包系统，用bundler管理gem，选择淘宝提供的RubyGems镜像


# 终端出现下面的内容，说明设置成功


```

7. 创建系统用户





8. 安装mysql

```shell
# 安装mysql，期间会要求输入mysql root用户的密码

# 确认版本为5.5.14以上

# 登陆mysql

# 登录报错ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock'需要执行下面语句



```





安装Docker维护的版本

```shell
root@3776c9b1fdb3:/# apt-get update
root@3776c9b1fdb3:/# apt-get install -y apt-transport-https
root@3776c9b1fdb3:/# echo deb https//get.docker.com/ubuntu docker main>/etc/apt/sources.list.d/docker.list


root@3776c9b1fdb3:/# uname -a
Linux 3776c9b1fdb3 4.14.104-boot2docker #1 SMP Thu Feb 28 20:58:57 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux

root@3776c9b1fdb3:/# cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=18.04
DISTRIB_CODENAME=bionic
DISTRIB_DESCRIPTION="Ubuntu 18.04.2 LTS"




```











