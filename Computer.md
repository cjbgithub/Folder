修改Windows默认安装路径：

regedit -> HKEY_LOCAL_MACHINE->SOFTWARE->Microsoft->Windows->CurrentVersion -> 修改ProgramFilesDir数值为D:\Program Files\Software



计算机保存信息的戒指：

+ 内部存储器
    - 寄存器
    - 高速缓冲存储器（Cache）
    - 主存储器
+ 外部存储器
    + 磁盘
        - 软盘（A、B）
        - 硬盘（C...）
            + 固态硬盘SSD
            + 机械硬盘HDD
    + 光盘
    + U盘

硬盘分区是对硬盘的一种格式化，然后才能用硬盘保存信息
+ 主分区（活动分区）C
+ 扩展分区 -> 逻辑分区

机械硬盘是由一个或多个铝制或玻璃纸的碟片组成，呈圆形  
机械硬盘读取数据是CAV(Constant Angular Velocity)，恒定角速度  
读取速度相同时间内读取外圈的数据比内圈的数据多，即外圈读取速度快  
正常分区一般C盘位于外圈，读取速度较快

在CPU在读取内存，内存不够时会根据内存情况调用虚拟内存（一般在C盘）





# 高性能服务系统建构与实践

Nginx是一款轻量级的Web服务器/反向代理服务器及电子邮件代理服务器。

一致性Hash算法应用于分布式计算系统、分布式存储系统、数据分析等领域。



# 1.SVN

```python
# 安装subversion
[root@localhost ~]# yum -y install subversion
# 查看安装版本
[root@localhost ~]# rpm -aq subversion
# 创建svn数据目录
[root@localhost ~]# mkdir -p /application/svndata
# 创建svn密码目录
[root@localhost ~]# mkdir -p /application/passwd
# 启动svn服务
[root@localhost ~]# svnserve -d -r /application/svndata/
# 查看svn进程
[root@localhost ~]# ps -ef|grep svn
[root@localhost ~]# netstat -lntup | grep 3690
# 创建svn版本库
[root@localhost ~]# svnadmin create /application/svndata/sadoc
# 修改svn配置文件
[root@localhost ~]# vim /application/svndata/sadoc/conf/svnserver.conf
[genneral]
anon-access = none
auth-access = write
passwd-db = /application/svnpasswd/passwd
authz-bd = /application/svnpasswd/authz
# 拷贝svn配置文件
[root@localhost ~]# cp authz passwd /application/svnpasswd
[root@localhost ~]# vim /application/svnpasswd/authz
[users]
cjb = cjb
test = test
[root@localhost ~]# vim /application/svnpasswd/authz
[groups]
wanda = test, test1
[sadoc:/]
cjb = rw
test = r
@wanda = r
# svn 防火墙iptables开启端口3690
[root@localhost ~]# systemctl stop firewalld
[root@localhost ~]# systemctl disable firewalld
[root@localhost ~]# yum install -y iptables-services
[root@localhost ~]# systemctl start iptables
[root@localhost ~]# systemctl enable iptables
[root@localhost ~]# iptables -I INPUT -p tcp --dport 3690 -j ACCEPT
[root@localhost ~]# iptables -I OUTPUT -p tcp --dport 3690 -j ACCEPT
[root@localhost ~]# service iptables save
[root@localhost ~]# service iptables restart
[root@localhost ~]# systemctl restart iptables
# linux客户端
[root@localhost ~]# mkdir /svndata
[root@localhost ~]# svn co svn://192.168.17.91/sadoc /svndata --username=cjb --password=cjb
# 拷贝分支
[root@localhost ~]# svn copy svn://192.168.17.91/sadoc/trunk svn://192.168.17.91/sadoc/branch/branch2019 -m "create a branch" --username=cjb --password=cjb
[root@localhost svndata]# svn co file:///application/svndata/sadoc/
# 字符集报错
[root@localhost ~]# export LC_CTYPE="en_US.UTF-8"
[root@localhost ~]# export LC_ALL=
[root@localhost ~]# locale
# 查看数据
[root@localhost ~]# svn ls svn://192.168.17.91/sadoc --username=cjb --password=cjb
# 提交版本
[root@localhost svndata]# rm -fr sadoc
[root@localhost svndata]# touch {a..c}
[root@localhost svndata]# svn add a b c
[root@localhost svndata]# svn ci -m "add data"
[root@localhost svndata]# mkdir -p /svn/trunk /svn/branch /svn/tag
[root@localhost svndata]# svn import /svn svn://192.168.17.91/sadoc -m "import"
[root@localhost svndata]# svn import /svn file:///application/svndata/sadoc -m "import"

```

版本库目录格式
[<版本库>:/项目/目录]
@<用户组名> = <权限>
<用户名> = <权限>



办公测试环境

IDC测试环境

正式生产环境

软件版本统一，尽量单一

JIRA Mantis



代码发布架构方案：

1.SVN应用

①.钩子应用

②.ldap统一认证

2.大型企业代码发布

3.业务变更管理

设计一个代码发布的方案

CSVN，GIT安装部署



# 2.CSVN(apche+svn)

1

# 3.高并发

计算密集型领域（图像处理和服务端编程）使用并行计算效果较高

同步和异步：同步是请求响应后继续执行，异步是请求由另外一个线程执行，主线程继续

并发和并行：并发是短时间内执行多个程序，并行是每时每刻有多个程序持续执行

临界区：公共资源被同时修改后数据错误

阻塞和非阻塞：阻塞是一个线程占用临界区并不释放资源，其他线程无法工作，非阻塞是多个线程可同时进入临界区

死锁、饥饿和活锁

加速比=优化前系统耗时/优化后系统耗时



# redis

## redis安装

```python
[root@localhost ~]# cd /usr/local/src/
# 1.下载redis
[root@localhost src]# wget http://download.redis.io/releases/redis-5.0.7.tar.gz
# 2.解压压缩包
[root@localhost src]# tar -zxvf redis-5.0.7.tar.gz 
[root@localhost src]# cd redis-5.0.7
# 3.make
[root@localhost redis-5.0.7]# make
# 4.test
[root@localhost redis-5.0.7]# make test
You need tcl 8.5 or newer in order to run the Redis test
# 5.tcl
[root@localhost redis-5.0.7]# yum install tcl
# 6.安装redis
[root@localhost redis-5.0.7]# make PREFIX=/usr/local/redis install
# 7.拷贝配置文件
[root@localhost redis-5.0.7]# cd /usr/local/redis
[root@localhost redis]# cp /usr/local/src/redis-5.0.7/redis.conf ./
# 8.启动服务
[root@localhost redis]# ./bin/redis-server ./redis.conf
# 9.设置后台启动服务
[root@localhost ~]# vim /usr/local/redis/redis.conf 
daemonize yes
```

## redis常用命令

```python
# 删除key
127.0.0.1:6379> del key1 key2 ... keyn
# 重命名存在的key
127.0.0.1:6379> rename key newkey
# 重命名不存在的key
127.0.0.1:6379> renamenx key newkey
# 移动key到数据库bd（默认开启15个数据库，select 0）
127.0.0.1:6379> move key bd
# 查询key（*匹配任意多个字符、?匹配单个字符、[]匹配括号内某1个字符）
127.0.0.1:6379> keys pattern
# 返回随机key
127.0.0.1:6379> random key
# key是否存在
127.0.0.1:6379> exists key
# key类型
127.0.0.1:6379> type key
# key设置生命周期（秒）
127.0.0.1:6379> expire key 
# key查询生命周期（秒）
127.0.0.1:6379> ttl key
# key设置为永久有效
127.0.0.1:6379> persist key  
```

## redis字符串操作

```python
# 在key存在（xx）或不存在（nx）时设置key及其生命周期
127.0.0.1:6379> set key value [ex 秒数 | px 毫秒数] [nx | xx]
# 批量设置key
127.0.0.1:6379> mset key1 value1...
# 获取key
127.0.0.1:6379> get key
# 批量获取key
127.0.0.1:6379> mget key1 key2 ... keyn
# key修改字符串偏移量offset后的值（超出范围自动补\x00）
127.0.0.1:6379> setrange key offset value
# key追加内容
127.0.0.1:6379> append key value
# 截取key指定范围字符串
127.0.0.1:6379> getrange key start stop
# key获取旧值并设置新值
127.0.0.1:6379> getset key newvalue
# key自减
127.0.0.1:6379> incr key
# key按指定整数自增
127.0.0.1:6379> incrby key number
# key按指定浮点数自增
127.0.0.1:6379> incrbyfloat key floatnumber
# key自减
127.0.0.1:6379> desc key
# key按指定整数自减
127.0.0.1:6379> descby key number
# key获取二进制表示对应偏移量位上的值
127.0.0.1:6379> getbit key offset
# key设置二进制表示对应偏移量位上的值
127.0.0.1:6379> setbit key offset value
# 对多个key作operation（AND、OR、NOT、XOR）并保存到destkey
127.0.0.1:6379> bitop operation destkey key [key2 ...]
```

offset 最大 2^32-1，即最大字符串为 512M

```python
# 大小写转换
# A 65 (0100 0001)
# a 97 (0110 0001)
127.0.0.1:6379> set char A
# 1.使用bitop操作
127.0.0.1:6379> setbit lower 2 1
127.0.0.1:6379> bitop or result char lower
127.0.0.1:6379> get result
# 2.使用setbit操作
127.0.0.1:6379> setbit char 2 1
127.0.0.1:6379> get char
```
bitop操作返回的是字符串长度，一个字符串两个字节，8bit
```python
# 记录一亿人一周内登陆的数据，记录数据的位数对应登陆用户的编号
# 1.初始化数据
127.0.0.1:6379> setbit mon 100000000 1
# 2.登陆时设置值
127.0.0.1:6379> setbit mon 3 1				-- 3号用户周一登陆
127.0.0.1:6379> setbit mon 5 1				-- 5号用户周一登陆
127.0.0.1:6379> setbit mon 7 1				-- 7号用户周一登陆
127.0.0.1:6379> setbit thu 100000000 1
127.0.0.1:6379> setbit thu 3 1				-- 3号用户周二登陆
127.0.0.1:6379> setbit thu 5 1
127.0.0.1:6379> setbit thu 8 1
127.0.0.1:6379> setbit wen 100000000 1
127.0.0.1:6379> setbit wen 3 1				-- 3号用户周三登陆
127.0.0.1:6379> setbit wen 4 1
127.0.0.1:6379> setbit wen 6 1
# 3.运算并记录结果
127.0.0.1:6379> bitop and result mon thu wen
# 4.获取指定登陆人是否三天内连续登陆的次数
127.0.0.1:6379> getbit result 3				-- 3号用户是否连续三天登陆的结果
127.0.0.1:6379> getbit result 4				-- 4号用户是否连续三天登陆的结果
```

## redis链表(link)结构

```python
# 左边插入元素
127.0.0.1:6379> lpush key value
# 获取右边元素
127.0.0.1:6379> rpop key
# 截取指定位置元素
127.0.0.1:6379> lrange key start stop
# 删除count个元素，count>0 左边删、count<0 右边删
127.0.0.1:6379> lrem key count value
# 剪切指定位置元素并赋值给key
127.0.0.1:6379> ltrim key start stop
# 获取index上的值
127.0.0.1:6379> lindex key index
# 计算链表元素个数
127.0.0.1:6379> llen key
# 在链表中寻找search并在前|后添加元素value
127.0.0.1:6379> linsert key after|before search value
# 从source链尾获取元素并放在dest链头
127.0.0.1:6379> rpoplpush source dest
```

## redis集合(set)命令

集合性质：确定性，唯一性，无序性

```python
# 添加元素
127.0.0.1:6379> sadd key value1 value2 ...
# 删除元素,返回真正删除元素的个数
127.0.0.1:6379> srem key value1 value2 ...
# 返回并删除一个随机元素
127.0.0.1:6379> spop key
# 返回一个随机元素
127.0.0.1:6379> srandmember key
# 判断元素在集合中是否存在
127.0.0.1:6379> sismember key value
# 返回所有元素
127.0.0.1:6379> smembers key
# 计算集合中元素个数
127.0.0.1:6379> scard key
# 删除source中元素value并将其添加到dest中
127.0.0.1:6379> smove source dest value
# 计算并返回交集
127.0.0.1:6379> sinter key1 key2 ...
# 计算交集并添加到dest中
127.0.0.1:6379> sinterstore dest key1 key2 ...
# 计算并返回交集
127.0.0.1:6379> suion key1 key2 ...
# 计算并返回差集(key1-key2-...)
127.0.0.1:6379> sdiff key1 key2 ...
```

## redis有序集合(order set)命令

```python
# 添加元素
127.0.0.1:6379> zadd key score1 value1 score2 value2 ...
# 删除元素
127.0.0.1:6379> zrem key value1 value2 ...
# 按照score删除元素
127.0.0.1:6379> zremrangebyscore key min max
# 按照order删除元素
127.0.0.1:6379> zremrangebyrank key start stop
# 查看排名
127.0.0.1:6379> zrank key member
# 按照排名范围返回元素[并返回分数]
127.0.0.1:6379> zrange key start stop [withscores]
# 按照降序排名返回元素
127.0.0.1:6379> zrevrange key start stop
# 排序后按照score获取元素
127.0.0.1:6379> zrangebyscore key min max [withscores] limit offset N
# 统计元素个数
127.0.0.1:6379> zcard key
# 统计指定范围元素个数
127.0.0.1:6379> zcount key min max
# 按照元素权重及指定聚合方法计算多个集合的交集
127.0.0.1:6379> zinterstore destination numkeys key1 [key2 ...] [weights weight [weight ...]] [aggregate sum|min|max]
# 示例
127.0.0.1:6379> zadd bag 2 a 3 b 4 c
127.0.0.1:6379> zadd pag 1 a 2.5 b 8 d
127.0.0.1:6379> zinterstore tmp 2 bag pag
127.0.0.1:6379> zinterstore tmp 2 bag pag aggregate sum
127.0.0.1:6379> zinterstore tmp 2 bag pag aggregate min
127.0.0.1:6379> zinterstore tmp 2 bag pag weights 1 2
127.0.0.1:6379> zrange tmp 0 -1 withscores
```

## redis哈希(Hash)命令

```python
# 设置field域的值value
127.0.0.1:6379> hset key field value
# 批量设置值
127.0.0.1:6379> hmset key field1 value1 [field2 value2 ...]
# 获取值
127.0.0.1:6379> hget key field
# 批量获取值
127.0.0.1:6379> hmget key field1 field2 ...
# 获取所有值
127.0.0.1:6379> hgetall key
# 删除值
127.0.0.1:6379> hdel key field
# 返回元素个数
127.0.0.1:6379> hlen key
# 判断元素是否存在
127.0.0.1:6379> hexists key field
# 自增
127.0.0.1:6379> hinrby key field value
127.0.0.1:6379> hinrbyfloat key field value
# 获取所有field
127.0.0.1:6379> hkeys key
# 获取所有value
127.0.0.1:6379> hvals key
```

## redis事务

|      | MySQL             | Redis       |
| ---- | ----------------- | ----------- |
| 开启 | start transaction | multi       |
| 语句 | 普通SQL           | 普通命令    |
| 失败 | rollback回滚      | discard取消 |
| 成功 | commit            | exec        |

执行中间出错时，rollback全部回滚，discard不能撤回已正确执行的命令

悲观锁：只能由一个人操作；乐观锁（redis）：其他人也可以操作，数据变更时撤销操作

```python
127.0.0.1:6379> mset ticket 1 money 500
127.0.0.1:6379> watch
127.0.0.1:6379> multi
127.0.0.1:6379> decr ticket
127.0.0.1:6379> decrby money 100
127.0.0.1:6379> exec
127.0.0.1:6379> mget ticket money
127.0.0.1:6379> unwatch
```

## redis消息订阅

```python
127.0.0.1:6379> publish key 'message'
127.0.0.1:6379> subscribe key
127.0.0.1:6379> psubscribe key*
127.0.0.1:6379> pubsub channels
```



```python
# 
127.0.0.1:6379> 
# 
127.0.0.1:6379> 
# 
127.0.0.1:6379> 
# 
127.0.0.1:6379> 
# 
127.0.0.1:6379>  
# 
127.0.0.1:6379> 
# 
127.0.0.1:6379> 
# 
127.0.0.1:6379> 
# 
127.0.0.1:6379> 
# 
127.0.0.1:6379>  
# 
127.0.0.1:6379> 
# 
127.0.0.1:6379> 
# 
127.0.0.1:6379> 
# 
127.0.0.1:6379> 
# 
127.0.0.1:6379> 
```

# JVM

> Java虚拟机内存数据

- 程序计数器：存放下一条的指令

- 虚拟机栈：存放函数调用堆栈信息

- 本地方法区：

- Java堆：存放Java运行时的对象等数据

- 方法区：存放程序的元数据

​	处理器需要按照已有指令序列执行程序，计算机将指令地址存储在程序计数器（Program Counter Register）中，可确保准确获取下次执行的指令。

​	虚拟机栈存放在随机存储器（随机存取存储器，Random Access Memory，RAM）中，通过上下移动堆栈指针动态调整内存空间大小。栈数据可共享，但是栈内数据大小及生存周期是确定的。主要存放基本类型变量及对象引用。

​	栈访问速度快于堆，次于寄存器。

​	堆是存放在RAM中的通用性内存池，是一个运行时数据区，用来存放Java对象（动态分配内存大小），由垃圾回收负责清理空间，缺点是访问速度较慢。

































































# JVM

​    HotSpot(Java HotSpot Virtual Machine)从JDK1.3开始成为Sun JDK的默认虚拟机

​	HotSpot的垃圾收集机制Garbage Collection对应的产品Garbage Collector

## JVM术语

1. Millisecond ms

   millisecond(ms)  microsecond(µs)  nanosecond(ns)  picosecond(ps)，依次从大到小千分之一

2. Megabyte

3. 配置JVM Option

   ```java
   public class JvmDemoTest {
       public static void main(String[] args) {
           Runtime runtime = Runtime.getRuntime();
           int freeMemory = (int) (runtime.freeMemory() / 1024 / 1024);
           int totalMemory = (int) (runtime.totalMemory() / 1024 / 1024);
           System.out.println("Memory info :" + freeMemory + "M/"
                   + totalMemory + "M(free/total)");
       }
   }
   ```

4. 并行和并发计算
   并行是多个任务同时执行

   并发是多个任务交替执行，以达到宏观上同时执行的效果，而多个任务之间有可能还是串行的

5. 进程和线程

   进程是程序执行的一个实例，是资源非分配的最小单位。

   线程是进程内独立执行的一个单元执行流，是程序执行的最小单位。

6. 多线程 multithreading

   多线程是一种从软件或硬件上实现多个线程并发执行的技术

7. 内存泄漏 Memory Leak

   内存泄漏是指用动态存储分配函数动态开辟的空间在使用完毕后未被释放，直到程序结束

   ```Java
   // -Xms10m -Xmx20m
   public class MemoryLeakTest {
       static class Key {
           Integer id;
           public Key(Integer id) {this.id = id;}
           @Override
           public int hashCode() {return id.hashCode();}
       }
       public static void main(String[] args) {
           Map map = new HashMap();
           while (true)
               for (int i = 0; i < 10000; i++)
                   if (!map.containsKey(new Key(i)))
                       map.put(new Key(i), "Number:" + i);
       }
   }
   ```

8. Soft、Weak、Phantom、Final、JNI References





























## JVM Option

1. -XX:+PrintGCDetails

```
Heap 堆
 PSYoungGen 年轻代
  eden space 33280K, 92% used ...
  from space 5120K, 99% used ...
  to   space 5120K, 0% used ...
 ParOldGen total 87552K, used 1441K ...
  object space 87552K, 1% used ...
 Metaspace used 5806K ...
  class space used 595K, capacity 667K, committed 768K, reserved 1048576K
```
2. -Xloggc
```
Ordinary Object Pointer 普通指针对象，64位消耗的内存是32位的1.5倍。
	-XX:+UseCompressedOops 在64 bit JVM中压缩指针，可以节约内存
	-XX:+UseCompressedClassPointers 压缩类的元数据
	-XX:-UseLargePagesIndividualAllocation 大页内存使用时自动启用
-XX:+PrintGCDetails -verbose:gc -Xloggc:gc.log -XX:+useSerialGC
```
3. -XX+useSerialGC
4. -XX:+useParNewGC
5. -XX:+useParallelGC
6. -XX:+useParallelOldGC
7. -XX:+useConcMarkSweepGC
8. -XX:+useG1GC
| GC输出年轻代名称   | GC收集器                                |
| ------------------ | --------------------------------------- |
| def new generation | -XX:UseSerialGC                         |
| par new generation | -XX:UseParNewGC或-XX:UseConcMarkSweepGC |
| PSYoungGen         | -XX:UseParallelOldGC或-XX:UseParallelGC |
| garbage-first heap | -XX:UseG1GC                             |

9. -XX:+PrintGCApplicationStoppedTime

     -XX:+PrintGCApplicationConcurrentTime

10. ConcGCThreads=8
      region大小默认为堆大小的1/2000

11. -XX:G1HeapRegionSize=32M

12. -XX:G1HeapWastePercent=5

    G1 GC不会回收的空闲内存比例是堆内存的5%

13. -XX:G1MixedGCCountTarget

14. -XX:+G1PrintRegionLivenessInfo

    诊断选项，打印Region存活对象信息，使用前必须开启-XX:+UnlockDiagnosticVMOptions

15. -XX:+G1ReservePercent

16. -XX:+G1SummarizeRSetStats

    诊断选项，打印RSet信息，使用前必须开启-XX:+UnlockDiagnosticVMOptions

    可同时使用-XX:+G1SummarizeRSetStatsPeriod

17. -XX:+G1TraceConcRefinement

    诊断选项，打印并行Refinement线程相关信息

    | Garbage Collector | Worker Threads Used |
    | ----------------- | ------------------------ |
    | Parallel GC | ParallelGCThreads  |
    | CMS GC | ParallelGCThreads ConcGCThreads |
    | G1 GC | ParallelGCThreads ConcGCThreads G1ConcRefinementThreads |

    | 名称            | 选项控制(-XX:)      | 作用                  |
    | --------------- | ----------------- | ----------------- |
    | ParallelGC Thread | ParallelGCThreads | GC的并行工作现成，专门用于独占阶段的工作，比如拷贝存货对象 |
    | ParallelMarkingThreads | ConcGCThreads | 并行标记阶段的并行线程，由主控现成和工作现成组成，可同应用程序并行执行 |
    | G1ConcurrentRedinementThreads | G1ConcRefinementThreads | 和应用程序一起运行，用于更新RSet |

18. -XX:+G1UseAdaptiveConcRefinement

      默认开启，动态计算GC中-XX:G1ConcRefinementGreenZone、-XX:G1ConcRefinementYellowZone、-XX:G1ConcRefinementRedZone的值

19. -XX:GCTimeRatio

      Java应用线程花费的时间与GC线程花费时间的比率

20. -XX:+HeapDumpBeforeFullGC / -XX:+HeapDumpAfterFullGC

21. -XX:InitiatingHeapOccupancyPercent=45

22. -XX:+useStringDedulplication

      默认不启用，对Java String对象去重

23. -XX:StringDeduplicationAgeThreshold

      默认值为3，字符串对象年龄超过设定阙值或者到老年代Region后成为去重候选对象，只做一次去重操作

24. -XX:+PrintStringdeduplicationStatistics

      默认关闭，可根据统计数据查看字符串去重后是否节约了大量堆内存空间

25. -XX:+G1UseAdaptiveHOP

      JDK9选项，通过动态调节标记阶段开始的时间，以达到提升应用程序吞吐量的目标

26. -XX:MaxGCPauseMills

      目标停顿时间，默认是200mx，G1 GC会尽力确保年轻代的回收时间保持在目标停顿时间内

27. -XX:MinHeapFreeRatio

      设置堆内存里可以空闲的最小的内存空间大小，默认为堆内存的40%

28. -XX:MaxHeapFreeRatio

      设置堆内存里可以空闲的最大的内存空间大小，默认为堆内存的70%

29. -XX:+PrintAdaptiveSizePolicy

      设置是否开启堆内存大小变化的相应记录信息打印

30. -XX:+ResizePLAB

31. -XX:+ResizeTLAB

32. -XX:+ClassUnloadingWithConcurrentMark

33. -XX:+ClassUnloading

34. -XX:+UnlockDiagnosticVMOptions -XX:PrintFlagsFinal

35. -XX:+UnlockExperimentVMOptions -XX:PrintFlagsFinal

36. -XX:+UnlockCommericalFeatures





















```

```