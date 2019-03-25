# 1. Linux命令

## 1.1 SHELL

Linux系统内核负责完成对硬件资源的分配、调度等管理任务。

Bash（Bourne-Again SHell）解释器

 - 上下键调取过往执行过的命令
 - Tab键补全命令或参数
 - 强大的批处理脚本
 - 实用的环境变量功能

## 1.2 查看帮助命令

```shell
[root@localhost ~]# man man
	- 查询：/linux ?linux；向后向前定位：n N；空格 up down home end q
	- NAME			命令名称
	- SYNOPSIS		参数的大致使用方法
	- DESCRIPTION		介绍说明
	- EXAMPLES		演示
  - OVERVIEW		概述
  - DEFAULTS		默认功能
  - OPTIONS			具体可用选项
  - ENVIRONMENT		环境变量
  - FILES			用到的文件
  - SEE ALSO		相关资料
  - HISTORY			维护历史与联系方式
```

## 2.3 常用系统工作命令

**1．echo命令**

```shell
[root@localhost ~]# echo [字符串 | $变量]
# 终端输出字符串或变量提取后的值
[root@localhost ~]# echo helloworld
helloworld
[root@localhost ~]# echo $SHELL
/bin/bash
```

**2．date命令**

```shell
[root@localhost ~]# date [选项] [+指定的格式]
# 显示及设置系统时间或日期 %t %H %l %M %S %j
[root@localhost ~]# date
2019年 03月 25日 星期一 20:21:32 CST
[root@localhost ~]# date "+%Y-%m-%d %H:%M:%S"
2019-03-25 20:22:11
root@localhost ~]# date -s "20001201 08:01:01"
2000年 12月 01日 星期五 08:01:01 CST
[root@localhost ~]# date
2000年 12月 01日 星期五 08:01:26 CST
# 当天是当年中的第几天
[root@localhost ~]# date "+%j"
336
```

**3．reboot命令**

```shell
[root@localhost ~]# reboot
# root用户重启计算机
```

**4．poweroff命令**

```shell
# root关闭计算机
[root@localhost ~]# poweroff
```

**5．wget命令**

```shell
[root@localhost ~]# wget [参数] 下载地址
# 终端下载网络文件
  -b	后台下载模式
  -P	下载到指定目录
  -t	最大尝试次数
  -c	断点续传
  -p	下载页面内所有资源，包括图片、视频等
  -r	递归下载
```

**6．ps命令**

```shell
[root@localhost ~]# ps [参数]
# 查看系统中的进程状态
  -a	显示所有进程（包括其他用户的进程）
  -u	用户以及其他详细信息
  -x	显示没有控制终端的进程
# 常见进程状态
  R（运行）		进程正在运行或在运行队列中等待
  S（中断）		进程处于休眠中，当某个条件形成后或者接收到信号时，则脱离该状态
  D（不可中断） 	进程不响应系统异步信号，即便用kill命令也不能将其中断
  Z（僵死）		进程已经终止，但进程描述符依然存在, 直到父进程调用wait4()系统函数后将进程释放
  T（停止）		进程收到停止信号后停止运行
```

**7．top命令**

```shell
# top动态监视进程活动与负载等信息

# 系统时间、运行时间、登录终端数、系统负载（1分钟、5分钟、15分钟内的平均值，数值越小意味着负载越低）
top - 08:34:28 up  1:18,  5 users,  load average: 0.00, 0.01, 0.05
# 进程总数、运行中的进程数、睡眠中的进程数、停止的进程数、僵死的进程数
Tasks:  94 total,   1 running,  93 sleeping,   0 stopped,   0 zombie
# 用户占用资源百分比、系统内核占用资源百分比、改变过优先级的进程资源百分比、空闲的资源百分比等
# 其中数据均为CPU数据并以百分比格式显示，例如“97.1 id”意味着有97.1%的CPU处理器资源处于空闲
%Cpu(s):  0.3 us,  0.3 sy,  0.0 ni, 99.3 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
# 物理内存总量、内存使用量、内存空闲量、作为内核缓存的内存量
KiB Mem :  1014968 total,   763768 free,    99940 used,   151260 buff/cache
# 虚拟内存总量、虚拟内存使用量、虚拟内存空闲量、已被提前加载的内存量
KiB Swap:   839676 total,   839676 free,        0 used.   753088 avail Mem 

  PID USER      PR  NI   VIRT    RES     SHR S %CPU %MEM   TIME+ COMMAND               
 3062 root      20   0  573924  19160   6020 S  0.3  1.9   0:01.08 tuned                 
 4065 root      20   0  162012   2248   1568 R  0.3  0.2   0:00.04 top          
```

**8．pidof命令**

```shell
[root@localhost ~]# pidof [参数] [服务名称]
# 查询某个指定服务进程的PID
```

**9．kill命令**

```shell
[root@localhost ~]# kill [参数] [进程PID]
# 终止某个指定PID的服务进程
```

**10．killall命令**

```shell
[root@localhost ~]# killall [参数] [服务名称]
# 终止某个指定名称的服务所对应的全部进程
```

## 2.4 系统状态检测命令

**1．ip命令**

​	查看当前的网卡配置与网络状态等信息，主要查看网卡名称、inet后面的IP地址、ether后面的网卡物理地址（MAC地址），以及RX、TX的接受数据包与发送数据包的个数

**2．uname命令**

```shell
[root@localhost ~]# uname [-a]
# 查看系统内核与系统版本等信息
# 内核名称、主机名、内核发行版本、节点名、系统时间、硬件名称、硬件平台、处理器类型以及操作系统名称
[root@localhost ~]# uname -a
Linux localhost.localdomain 3.10.0-957.10.1.el7.x86_64 #1 SMP Mon Mar 18 15:06:45 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
[root@localhost ~]# cat /etc/centos-release
CentOS Linux release 7.6.1810 (Core)
```

**3．uptime命令**

```shell
# 查看系统中的负载信息
# 显示当前系统时间、系统已运行时间、启用终端数量以及平均负载值
# 平均负载值指的是系统在最近1分钟、5分钟、15分钟内的压力情况
# 负载值越低越好，尽量不要长期超过1，在生产环境中不要超过5
[root@localhost ~]# uptime
 21:25:29 up  1:47,  6 users,  load average: 0.00, 0.01, 0.05
```

**4．free命令**

```shell
[root@localhost ~]# free [-h]
# 查看系统中内存的使用情况
[root@localhost ~]# free -h
              total        used        free      shared  buff/cache   available
Mem:           991M         98M        744M        6.7M        148M        733M
Swap:          819M          0B        819M
```

**5．who命令**

```shell
[root@localhost ~]# who [参数]
# 查看当前登入主机的用户终端信息
[root@localhost ~]# who
root     tty1         2019-03-25 19:38
root     pts/0        2019-03-25 19:38 (192.168.0.110)
root     pts/1        2019-03-25 20:03 (192.168.0.110)
```

**6．last命令**

```shell
[root@localhost ~]# last [参数]
# 查看所有系统的登陆记录
```

**7．history命令**

```shell
[root@localhost ~]# history [-c]
# 显示历史执行过的命令，-c可以清空所有的命令历史记录
[root@localhost ~]# cat ~/.bash_history
```

**8．sosreport命令**

```shell
[root@localhost ~]# sosreport
# 用于收集系统配置及架构信息并输出诊断文档以及校验码
```

## 2.5 工作目录切换命名

**1．pwd命令**

```shell
[root@localhost ~]# pwd [选项]
# 显示当前用户所处的工作目录
```

**2．cd命令**


```shell
[root@localhost ~]# cd [目录名称]
# 切换工作路径
# cd -			返回上一次所处的目录
# cd ..			进入上一级目录
# cd ~			切换当前用户的根目录
# cd ~username		切换其他用户的根目录
```

**3．ls命令**


```shell
[root@localhost ~]# ls [选项] [文件]
# 显示目录中的文件信息
  -a  查看全部文件
  -l  查看文件属性、大小等详细信息
  -d  查看目录属性信息
```

## 2.6 文件文本编辑命令

**1．cat命令**

```shell
[root@localhost ~]# cat [选项] [文件]
# 查看纯文本文件（内容较少）
```

**2．more命令**


```shell
[root@localhost ~]# more [选项] [文件]
# 查看纯文本文件（内容较多）
```

**3．head命令**

```shell
[root@localhost ~]# head [选项] [文件]
# 查看纯文本文件的前n行
[root@localhost ~]# head -n 20 anaconda-ks.cfg 
#version=DEVEL...
```

**4．tail命令**


```shell
[root@localhost ~]# tail [选项] [文件]
# 查看纯文本文档的后N行或持续刷新内容
```

**5．tr命令**

```shell
[root@localhost ~]# tr [原始字符] [目标字符]
# 用于替换文本文件中的字符
```

**6．wc命令**

```shell
[root@localhost ~]# wc [选项] 文本
# 统计指定文本的行数、字数、字节数
  -l  只显示行数
  -w  只显示单词数
  -c  只显示字节数
[root@localhost ~]# wc -l /etc/passwd
19 /etc/passwd
```

**7．stat命令**

```shell
[root@localhost ~]# stat 文件名称
# 查看文件的具体存储信息和时间等信息
```

**8．cut命令**


```shell
[root@localhost ~]# cut [参数] 文本
# 按”列“提取文本字符
[root@localhost ~]# cut -d: -f1 /etc/passwd
# 提取passwd文件的用户名信息，即提取以冒号为间隔符号的第一列内容
root
bin
daemon
adm...
```

**9．diff命令**


```shell
[root@localhost ~]# diff [参数] 文本
# 比较多个文本文件的差异
  --brief	确认两个文件是否不同
  -c		详细比较多个文件的差异之处
```

## 2.7 文件目录管理命令

**1．touch命令**


```shell
[root@localhost ~]# touch [选项] [文件]
# 创建空白文件或设置文件的时间
  -a  仅修改”读取时间“（atime)
  -m  仅修改”修改时间“（mtime)
  -d  同时修改atime与mtime
```

**2．mkdir命令**


```shell
[root@localhost ~]# mkdir [选项] 目录
# 创建空白的目录
```

**3．cp命令**


```shell
[root@localhost ~]# cp [选项] 源文件 目标文件
# 复制文件或目录
  -p  保留原始文件的属性
  -d  若对象为”链接文件“，则保留该”链接文件“的属性
  -r  递归持续复制（用于目录）
  -i  若目标文件存在则询问是否覆盖
  -a  相当于-pdf（p、d、f为上述参数）
```

**4．mv命令**


```shell
[root@localhost ~]# mv [选项] 源文件 [目标路径|目标文件名]
# 剪切文件重命名。删除源文件，保留剪切后的文件--文件重命名
```

**5．rm命令**


```shell
[root@localhost ~]# rm [选项] 文件
# 删除文件或目录
  -f  强制删除文件
  -r  删除目录
```

**6．dd命令**


```shell
[root@localhost ~]# dd [参数]
# 按照指定大小和个数的数据块来复制文件或转换文件
  if	输入的文件名称
  of	输出得文件名称
  bs	设置没个”块“的大小
  count	设置要复制”块“的个数
```

**7．file命令**


```shell
[root@localhost ~]# file 文件名
# 查看文件的类型
```

## 2.8 打包压缩与搜索命令

**1．tar命令**


```shell
[root@localhost ~]# tar [选项] [文件]
# tar命令用于对文件进行打包或解压
  -c	创建压缩文件
  -x	解开压缩文件
  -t	查看压缩包内有哪些文件
  -z	用Gzip压缩或解压
  -j	用bzip2压缩或解压
  -v	显示压缩或解压的过程
  -f	目标文件名
  -P	保留原始的权限与属性
  -p	使用绝对路径来压缩
  -C	指定解压到的路径
tar -czvf 压缩包名称.tar.gz 要打包的目录；tar -xzvf 压缩包名称.tar.gz
```

**2．grep命令**


```shell
[root@localhost ~]# grep [选项] [文本]
# grep命令用于在文本中执行关键词搜索，并显示匹配的结果
  -b	将可执行文件（binary）当作文本文件（text）来搜素
  -c	仅显示找到的行数
  -i	忽略大小写
* -n	显示行号
* -v	反向选择——仅列出没有”关键词“的行
[root@localhost home]# grep /sbin/nologin /etc/passwd
bin:x:1:1:bin:/bin:/sbin/nologin...
```

**3．find命令**


```shell
[root@localhost ~]# find [查找路径] 寻找条件 操作
# find命令用于按照指定条件查找文件
  -name				匹配名称
  -perm				匹配权限（mode为完全匹配，-mode为包含即可）
  -user				匹配所有者
  -group			匹配所有组
  -mtime -n +n			匹配修改内容的时间（-n指n天以内，+n指n天以前）
  -atime -n +n			匹配访问文件的时间（-n指n天以内，+n指n天以前）
  -ctime -n +n			匹配修改文件权限的时间（-n指n天以内，+n指n天以前）
  -nouser			匹配无所有者的文件
  -nogroup			匹配无所有组的文件
  -newer f1 !f2			匹配比文件f1新但比f2旧的文件
  -type b/d/c/p/l/f		匹配文件类型（块设备、目录、字符设备、管道、链接文件、文本文件）
  -size				匹配文件的大小（+50KB为查找超过50KB的文件，而-50KB为查找小于50KB的文件）
  -prune			忽略某个目录
  -exec …… {}\;			后面可跟用于进一步处理搜索结果的命令
[root@localhost home]# find /etc -name "host*" -print
/etc/host.conf...
[root@localhost home]# fine / -perm -4000 -print
/usr/bin/chfn...
```




```shell
[root@localhost ~]#  [选项] []
```



```shell
[root@localhost ~]#  [选项] []
```



```shell
[root@localhost ~]#  [选项] []
```



```shell
[root@localhost ~]#  [选项] []
```



```shell
[root@localhost ~]#  [选项] []
```



```shell
[root@localhost ~]#  [选项] []
```



```shell
[root@localhost ~]#  [选项] []
```



```shell
[root@localhost ~]#  [选项] []
```



```shell
[root@localhost ~]#  [选项] []
```



```shell
[root@localhost ~]#  [选项] []
```



```shell
[root@localhost ~]#  [选项] []
```



```shell
[root@localhost ~]#  [选项] []
```



```shell
[root@localhost ~]#  [选项] []
```



```shell
[root@localhost ~]#  [选项] []
```



```shell
[root@localhost ~]#  [选项] []
```





# 2. 管道符、重定向、环境变量





# 3. vim编辑器、shell命令





# 4. 用户身份与文件权限





# 5. 存储结构与磁盘划分





# 6. RAID与LVM磁盘阵列





# 7. Iptables与Firewall防火墙





# 8. ssh服务远程管理主机





