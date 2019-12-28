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
  - NAME            命令名称
  - SYNOPSIS        参数的大致使用方法
  - DESCRIPTION     介绍说明
  - EXAMPLES        演示
  - OVERVIEW        概述
  - DEFAULTS        默认功能
  - OPTIONS         具体可用选项
  - ENVIRONMENT     环境变量
  - FILES           用到的文件
  - SEE ALSO        相关资料
  - HISTORY         维护历史与联系方式
```

## 1.3 常用系统工作命令

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
  R（运行）      进程正在运行或在运行队列中等待
  S（中断）      进程处于休眠中，当某个条件形成后或者接收到信号时，则脱离该状态
  D（不可中断）   进程不响应系统异步信号，即便用kill命令也不能将其中断
  Z（僵死）      进程已经终止，但进程描述符依然存在, 直到父进程调用wait4()系统函数后将进程释放
  T（停止）      进程收到停止信号后停止运行
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

## 1.4 系统状态检测命令

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

## 1.5 工作目录切换命名

**1．pwd命令**

```shell
[root@localhost ~]# pwd [选项]
# 显示当前用户所处的工作目录
```

**2．cd命令**


```shell
[root@localhost ~]# cd [目录名称]
# 切换工作路径
# cd -          返回上一次所处的目录
# cd ..         进入上一级目录
# cd ~          切换当前用户的根目录
# cd ~username  切换其他用户的根目录
```

**3．ls命令**


```shell
[root@localhost ~]# ls [选项] [文件]
# 显示目录中的文件信息
  -a	查看全部文件
  -l	查看文件属性、大小等详细信息
  -d	查看目录属性信息
```

## 1.6 文件文本编辑命令

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

## 1.7 文件目录管理命令

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
  if    输入的文件名称
  of    输出得文件名称
  bs    设置没个”块“的大小
  count 设置要复制”块“的个数
```

**7．file命令**


```shell
[root@localhost ~]# file 文件名
# 查看文件的类型
```

## 1.8 打包压缩与搜索命令

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
  -name             匹配名称
  -perm             匹配权限（mode为完全匹配，-mode为包含即可）
  -user             匹配所有者
  -group            匹配所有组
  -mtime -n +n      匹配修改内容的时间（-n指n天以内，+n指n天以前）
  -atime -n +n      匹配访问文件的时间（-n指n天以内，+n指n天以前）
  -ctime -n +n      匹配修改文件权限的时间（-n指n天以内，+n指n天以前）
  -nouser           匹配无所有者的文件
  -nogroup          匹配无所有组的文件
  -newer f1 !f2     匹配比文件f1新但比f2旧的文件
  -type b/d/c/p/l/f 匹配文件类型（块设备、目录、字符设备、管道、链接文件、文本文件）
  -size             匹配文件的大小（+50KB为查找超过50KB的文件，而-50KB为查找小于50KB的文件）
  -prune            忽略某个目录
  -exec …… {}\;     后面可跟用于进一步处理搜索结果的命令
[root@localhost home]# find /etc -name "host*" -print
/etc/host.conf...
[root@localhost home]# fine / -perm -4000 -print
/usr/bin/chfn...
```


# 2. 管道符、重定向、环境变量

## 2.1 输入输出重定向

+ 标准输入重定向（STDIN，文件描述符为0）：默认从键盘输入，也可从其他文件或命令中输入。
+ 标准输出重定向（STDOUT，文件描述符为1）：默认输出到屏幕。
+ 错误输出重定向（STDERR，文件描述符为2）：默认输出到屏幕。

> 输入重定向符号及其作用

| 符号                 | 作用                                         |
| -------------------- | -------------------------------------------- |
| 命令 < 文件          | 将文件作为命令的标准输入                     |
| 命令 << 分界符       | 从标准输入中读入，直到遇见分界符才停止       |
| 命令 < 文件1 > 文件2 | 将文件1作为命令的标准输入并将标准输出到文件2 |

> 输出重定向符号及其作用

| 符号                             | 作用                                                         |
| -------------------------------- | ------------------------------------------------------------ |
| 命令 > 文件                      | 将标准输出重定向到一个文件中（清空原有文件的数据）           |
| 命令 2> 文件                     | 将错误输出重定向到一个文件中（清空原有文件的数据）           |
| 命令 >> 文件                     | 将标准输出重定向到一个文件中（追加到原有内容的后面）         |
| 命令 2>> 文件                    | 将错误输出重定向到一个文件中（追加到原有内容的后面）         |
| 命令 >> 文件 2>&1、命令 &>> 文件 | 将标准输出与错误输出共同写入到文件中（追加到原有内容的后面） |

## 2.2 管道命令符

“命令A | 命令B”：把前一个命令原本要输出到屏幕的标准正常数据当作是后一个命令的标准输入


```shell
# 找出被限制登陆用户
[root@localhost ~]# grep /sbin/nologin /etc/passwd
# 统计文本行数
[root@localhost ~]# wc -l
# 统计被限制登陆用户的个数
[root@localhost ~]# grep /sbin/nologin /etc/passwd | wc -l
15
[root@localhost ~]# echo "Content" | mail -s "Subject" otheruser
[root@localhost ~]# mail -s "Readme" root@otheruser.com << over
```

## 2.3 命令行的通配符

+ (*)         匹配零个或多个字符
+ (?)          匹配单个字符
+ [0-9]]     匹配0~9之间的单个数字的字符
+ [abc]]    匹配a、b、c三个字符中的任意一个字符

```shell
[root@localhost ~]# ls -l /dev/sda*
brw-rw----. 1 root disk 8, 0 3月  26 07:14 /dev/sda
brw-rw----. 1 root disk 8, 1 3月  26 07:14 /dev/sda1
brw-rw----. 1 root disk 8, 2 3月  26 07:14 /dev/sda2
[root@localhost ~]# ls -l /dev/sda?
brw-rw----. 1 root disk 8, 1 3月  26 07:14 /dev/sda1
brw-rw----. 1 root disk 8, 2 3月  26 07:14 /dev/sda2
[root@localhost ~]# ls -l /dev/sda[0-9]
brw-rw----. 1 root disk 8, 1 3月  26 07:14 /dev/sda1
brw-rw----. 1 root disk 8, 2 3月  26 07:14 /dev/sda2
```

## 2.4 常用转义字符

+ 反斜杠（\）：使反斜杠后面的一个变量变为单纯的字符串
+ 单引号（''）：转义其中所有的变量为单纯的字符串
+ 双引号（""）：保留其中的变量属性，不进行转义处理
+ 反引号（``）：把其中的命令执行后返回结果

## 2.5 重要的环境变量







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

## 2.1 输入输出重定向



## 2.3 22







# 3. vim编辑器、shell命令

## 3.1 Vim文本编辑器

命令模式：控制光标移动，可对文本进行复制、粘贴、删除和查找

输入模式：正常的文本录入

末行模式：保存或退出文档，以及设置编辑环境

> 常用命令

| 命令 | 作用                                               |
| ---- | -------------------------------------------------- |
| dd   | 删除（剪切）光标所在整行                           |
| 5dd  | 删除（剪切）从光标处开始的5行                      |
| yy   | 复制光标所在整行                                   |
| 5yy  | 复制从光标处开始的5行                              |
| n    | 显示搜索命令定位到的下一个字符串                   |
| N    | 显示搜索命令定位到的上一个字符串                   |
| u    | 撤销上一步的操作                                   |
| p    | 将之前删除（dd）或复制（yy）过的数据粘贴到光标后面 |

> 末行模式中可用命令

| 命令          | 作用                                 |
| ------------- | ------------------------------------ |
| :w            | 保存                                 |
| :q            | 退出                                 |
| :q!           | 强制退出（放弃对文档的修改内容）     |
| :wq!          | 强制保存退出                         |
| :set nu       | 显示行号                             |
| :set nonu     | 不显示行号                           |
| :命令         | 执行该命令                           |
| :整数         | 跳转到该行                           |
| :s/one/two    | 将当前光标所在行的第一个one替换成two |
| :s/one/two/g  | 将当前光标所在行的所有one替换成two   |
| :%s/one/two/g | 将全文中的所有one替换成two           |
| ?字符串       | 在文本中从下至上搜索该字符串         |
| /字符串       | 在文本中从上至下搜索该字符串         |

**1. 编写简单文档**

````
[root@localhost ~]# vim practice.txt
a/i/o -> write -> esc -> :wq!
[root@localhost ~]# cat practice.txt
````
**2. 配置主机名称**

````
[root@localhost ~]# vim /etc/hostname
linuxprode.com
[root@localhost ~]# reboot
[root@localhost ~]# hostname
````

**3. 配置网卡信息**

````
[root@localhost ~]# cd /etc/sysconfig/network-scripts/
[root@localhost ~]# vim ifcfg-eno16777736
TYPE=Ethernet
BOOTPROTO=static
NAME=eno16777736
ONBOOT=yes
IPADDR=192.168.10.10
NETMASK=255.255.255.0
GATEWAY=192.168.10.1
DNS1=192.168.10.1
[root@localhost ~]# reboot
[root@localhost ~]# ping 192.168.10.10
````

**4. 配置Yum仓库**

````
[root@localhost ~]# cd /etc/yum.repos.d
[root@localhost ~]# vim rhel7.repo
[rhel7]
name=rhel7
baseurl=file:///media/cdrom
enabled=1
gpgcheck=0
[root@localhost ~]#
[root@localhost ~]#
[root@localhost ~]#
````

## 3.2 shell脚本

交互式：输入一条执行一条

批处理：一次性执行多条命令

```
[root@localhost ~]# echo $SHELL
/bin/bash
```

**1. 简单的脚本**



**2. 接受参数**

$0：shell脚本程序的名称

$#：总共几个参数

$*：所有位置的参数值

$?：上一次命令的执行返回值

$1、$2、$3...：第N个位置的参数值

**3. 判断参数**

> 测试语句格式（条件表达式两边均有一个空格）：【 条件表达式 】

按测试对象：文件测试语句/逻辑测试语句/整数值比较语句/字符串比较语句

> 文件测试所用的参数

| 操作符 | 作用                       |
| ------ | -------------------------- |
| -d     | 测试文件是否为目录类型     |
| -e     | 测试文件是否存在           |
| -f     | 判断是否为一般文件         |
| -r     | 测试当前用户是否有权限读取 |
| -w     | 测试当前用户是否有权限写入 |
| -x     | 测试当前用户是否有权限执行 |

> 可用的整数比较运算符

| 操作符 | 作用                  |
| ------ | --------------------- |
| -eq    | 是否等于              |
| -ne    | 是否不等于            |
| -gt    | 是否大于 greater than |
| -lt    | 是否小于 less than    |
| -le    | 是否等于或小于        |
| -ge    | 是否大于或等于        |

## 3.3 流程控制语句

if/for/while/case



## 3.4 计划任务服务程序

> 一次性计划任务
>

```shell
[root@localhost ~]# at time
[root@localhost ~]# at -l
[root@localhost ~]# atrm 任务序号
```

> 长期性计划任务
>

```shell
[root@localhost ~]# crontab -e 创建、编辑
[root@localhost ~]# crontab -l 查看
[root@localhost ~]# crontab -r 删除
[root@localhost ~]# crontab -u 编辑其他人的计划任务
```

> 使用crond设置任务的参数

| 字段 | 说明                                     |
| ---- | ---------------------------------------- |
| 分钟 | 取值为0～59的整数                        |
| 小时 | 取值为0～23的任意整数                    |
| 日期 | 取值为1～31的任意整数                    |
| 月份 | 取值为1～12的任意整数                    |
| 星期 | 取值为0～7的任意整数，其中0与7均为星期日 |
| 命令 | 要执行的命令或程序脚本                   |


# 4. 用户身份与文件权限

## 4.1 用户身份与能力

**1. useradd命令**

> 创建用户：useradd [选项] 用户名

用户家目录存放位置/home，默认Shell解释器为/bin/bash，默认创建一个与该用户同名的基本用户组

| 参数 | 作用                                                      |
| ---- | --------------------------------------------------------- |
| -d   | 指定用户的家目录（默认为/home/username）                  |
| -e   | 账户的到期时间，格式为YYYY-MM-DD.                         |
| -u   | 指定该用户的默认UID                                       |
| -g   | 指定一个初始的用户基本组（必须已存在）                    |
| -G   | 指定一个或多个扩展用户组                                  |
| -N   | 不创建与用户同名的基本用户组                              |
| -s   | 指定该用户的默认[Shell](https://www.linuxcool.com/)解释器 |

```shell
[root@localhost ~]# useradd -d /home/linux -u 8888 -s /sbin/nologin linux_cjb
[root@localhost ~]# id linux_cjb
uid=8888(linux_cjb) gid=8888(linux_cjb) 组=8888(linux_cjb)
```

**2. groupadd命令**

> 创建用户组：groupadd [选项] 群组名

```
[root@localhost ~]# groupadd ronny
```

**3. usermod命令**

> 修改用户属性：usermod [选项] 用户名

用户信息存放位置：/etc/passwd

| 参数  | 作用                                                         |
| ----- | ------------------------------------------------------------ |
| -c    | 填写用户账户的备注信息                                       |
| -d -m | 参数-m与参数-d连用，可重新指定用户的家目录并自动把旧的数据转移过去 |
| -e    | 账户的到期时间，格式为YYYY-MM-DD                             |
| -g    | 变更所属用户组                                               |
| -G    | 变更扩展用户组                                               |
| -L    | 锁定用户禁止其登录系统                                       |
| -U    | 解锁用户，允许其登录系统                                     |
| -s    | 变更默认终端                                                 |
| -u    | 修改用户的UID                                                |

**4. passwd命令**

> 修改用户密码、过期时间、认证信息：passwd [选项] [用户名]

| 参数    | 作用                                                   |
| ------- | ------------------------------------------------------ |
| -l      | 锁定用户，禁止其登录                                   |
| -u      | 解除锁定，允许用户登录                                 |
| --stdin | 允许通过标准输入修改用户密码，如echo "NewPassWord"     |
| -d      | 使该用户可用空密码登录系统                             |
| -e      | 强制用户在下次登录时修改密码                           |
| -S      | 显示用户的密码是否被锁定，以及密码所采用的加密算法名称 |

**5. userdel命令**

> 删除用户：userdel [选项] 用户名

| 参数 | 作用                     |
| ---- | ------------------------ |
| -f   | 强制删除用户             |
| -r   | 同时删除用户及用户家目录 |

## 4.2 文件权限与归属

* -：普通文件
* d：目录文件
* l：链接文件
* b：块设备文件
* c：字符设备文件
* p：管道文件

> 读 r 4，写 w 2，执行 x 1，权限分配 文件所用者/文件所属者/其他用户

## 4.3 文件的特殊权限

**1. SUID**

可以让二进制程序的执行者临时拥有属主的权限（仅对拥有执行权限的二进制程序有效）

**2. SGID**































UID：user identification，0（管理员）、1-999（系统用户）、1000+（正常用户）

GID：group identification

创建用户会生成基本用户组，添加其他用户组称为扩展用户组。用户拥有一个基本用户组，多个扩展用户组



```shell
[root@localhost ~]#  [选项] []
```

```shell
[root@localhost ~]#  [选项] []
```

```shell
[root@localhost ~]#  [选项] []
```





















































# 5. 存储结构与磁盘划分





# 6. RAID与LVM磁盘阵列





# 7. Iptables与Firewall防火墙





# 8. ssh服务远程管理主机

```python
[root@localhost ~]# vim /etc/sysconfig/network-scripts/ifcfg-enp0s3
TYPE="Ethernet"
PROXY_METHOD="none"
BROWSER_ONLY="no"
BOOTPROTO="static"
IPADDR=192.168.17.91
MM_CONTROLLED=no
NETMASK=225.225.225.0
DEFROUTE="yes"
IPV4_FAILURE_FATAL="no"
IPV6INIT="yes"
IPV6_AUTOCONF="yes"
IPV6_DEFROUTE="yes"
IPV6_FAILURE_FATAL="no"
IPV6_ADDR_GEN_MODE="stable-privacy"
NAME="enp0s3"
UUID="0e9db9de-5a27-41d0-98a3-b75be2262145"
DEVICE="enp0s3"
ONBOOT="yes"

DNS1=192.168.17.1
DNS2=8.8.8.8
DNS3=4.4.4.4
```







