# docker

```shell
# docker运行应用程序并输出hello
$ docker run ubuntu:latest /bin/echo "hello-world"

# 交互式容器
$ docker run -i -t ubuntu:latest /bin/bash
  - t：在信容器内指定一个伪终端或终端
  - i：允许对容器内的标准输入（STDIN）进行交互

# 后台启动容器
$ docker run -d ubuntu:latest /bin/sh -c "while true; do echo hello world; sleep 1; done"

$ docker pull training/webapp
$ docker run -d -P training/webapp python app.py
  - d：让容器后台运行
  - P：将容器内部使用的网络端口映射到我们使用的主机上

$ docker run -d -p training/webapp python app.py

# 容器端口
$ docker port id/name

# 查看容器底层信息
$ docker inspect id/name

# 停止容器
$ docker stop id/name

# 重启容器
$ docker start id/name

# 查看最后一个创建的容器
$ docker ps -l

# 查看所有容器
$ docker ps -a

# 查看运行中的容器
$ docker ps

# 删除容器
$ docker rm id/name

$ docker images

$ docker pull image:version

$ docker search keyword

---更新镜像
$ docker run -t -i ubuntu:latest /bin/bash
apt-get update
$ docker commit -m="has update" -a="dunoob" id newname:tag
  - m 提交描述信息
  - a 作者
  - id 容器ID
  - newname:tag 新镜像name+tag
$ docker run -t -i newname:tag /bin/bash

# docker tag命令可以为镜像添加新的标签
$ docker tag newid newname:newtag

$ docker run -d -P 
  -P：是容器内部端口随机映射到主机的端口
  -p：是容器内部端口绑定到指定的主机端口
$ docker run -d -p 127.0.0.1:5001:5001 ubuntu

# --name标识来命名容器
$ docker run -d -P --name myubuntu

# 进入容器c6c787d00190
$ docker exec -it c6c787d00190 /bin/bash

$ docker run -i -t -d  --privileged -p 55402:22 -p 80:80 --name gitlib_ubuntu_1 gitlib_ubuntu:latest /usr/sbin/sshd -D
```



















# ubuntu

```shell
# 删除操作
$ docker rmi mysql
# 运行环境
$ docker run -t -i ubuntu /bin/bash

root@user:/# apt-get update -y
root@user:/# apt-get upgrade -y
root@user:/# apt-get install sudo -y
root@user:/# apt-get -y remove vim-common
root@user:/# apt-get -y install vim

root@user:/# apt-get install -y openssh-client openssh-server
root@user:/# sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
root@user:/# sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/g' /etc/ssh/sshd_config
root@user:/# mkdir /var/run/sshd
root@user:/# echo "root:123456" | chpasswd
root@user:/# /usr/sbin/sshd



root@user:/# sudo apt-get install -y build-essential zlib1g-dev libyaml-dev libssl-dev libgdbm-dev libreadline-dev libncurses5-dev libffi-dev curl openssh-server redis-server checkinstall libxml2-dev libxslt-dev libcurl4-openssl-dev libicu-dev logrotate python-docutils pkg-config cmake nodejs

# 查看docker进程
root@0d54dc720eaf:/# ps -aux | grep docker

# ifconfig(ifconfig -a)
apt-get install net-tools
# ping
apt-get install iputils-ping
# ip(ip addr)
apt-get install iproute2
# 查看进程
root@0d54dc720eaf:/# sudo netstat -antup
# 刷新DNS
root@0d54dc720eaf:/# sudo apt-get install nscd
root@0d54dc720eaf:/# sudo /etc/init.d/nscd restart
```

> ubuntu安装docker

```shell
# 1. 安装软件包，允许通过https使用镜像仓库
root@0d54dc720eaf:/# sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
# 2. Docker官方GPG密钥
root@0d54dc720eaf:/# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# 3. 密钥指纹验证
root@0d54dc720eaf:/# sudo apt-key fingerprint 0EBFCD88
# 4. stable镜像
root@0d54dc720eaf:/# sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
# 5. 安装docker
root@0d54dc720eaf:/# sudo apt-get install docker-ce

```









# centos

```shell
$ docker run -itd -p 127.0.0.1:8083:8083 --name centos_1 centos /usr/sbin/init
c5cc2a13db74d79bca4eefe6c966f4267e1839440d5ce01cadf3f46951b61d97
$ docker exec -it centos_asus /bin/bash
[root@2335ab0f0328 /]# yum -y install sudo
[root@c5cc2a13db74 /]# sudo yum -y install vim 
[root@2335ab0f0328 /]# sudo yum install -y yum utils device-mapper-persistent-data lvm2
[root@2335ab0f0328 /]# sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
[root@2335ab0f0328 /]# sudo yum-config-manager --enable docker-ce-edge
[root@2335ab0f0328 /]# yum list docker-ce.x86_64 --showduplicates | sort -r
[root@2335ab0f0328 /]# sudo yum install docker-ce-18.04.0.ce-3.el7.centos

# 安装service
[root@eadcc9900244 /]# yum list | grep initscripts
[root@eadcc9900244 /]# yum install initscripts

 HWADDR=02:42:ac:11:00:02

[root@eadcc9900244 network-scripts]# sudo yum makecache fast
[root@eadcc9900244 network-scripts]# sudo yum -y install docker-ce

[root@eadcc9900244 /]# service docker status
[root@eadcc9900244 /]# reboot

# 安装PXC
[root@eadcc9900244 /]# docker pull percona/percona-xtradb-cluster
[root@eadcc9900244 /]# docker load < /home/soft/pxc.tar.gz
[root@eadcc9900244 /]# docker tag docker.io/percona/percona-xtradb-cluster docker.io/pxc



```





# 容器

```shell


```

