# Python
## 1.Python基础知识
### 1.1.第一个Python程序
文件地址栏输出cmd直接进入命令行
```
python
print("hello world!")
```
**.py**结尾的文件为Python文件

> 运行Python的四种方法
1. 直接点击**.py文件**运行
2. cmd运行`python file.py`
3. cmd运行`file.py`
4. 打开IDLE（Python shell）打开文件点击Run -> Run module

### 1.2.注释
> 单行注释（# ）
> 多行注释（''' ''）
> 中文支持（#coding=utf-8、#-*-coding:utf-8-*-）

### 1.3.变量类型
+ Numbers
  - int
  - long
  - float
  - complex(复数)
+ Boolean
+ String
+ List
+ Tuple(元祖)
+ Dictionary

查看变量类型：`type(variableName)`

### 1.4.标识符和关键字
标识符由**字母、下划线和数字**组成，且**数字不能开头**
**Python区分大小写**

查看Python关键字(不允许使用关键字定义标识符)
```
import keyword
keyword.kwlist
```

### 1.5.输出
`print("hello world!"")`

> 格式化输出
```
age = 18
name = "chery"
print("姓名%s,年龄%d"%(name, age))
```

> 常用格式化符号

|格式化符号|转换|
|:---:|:---:|
|%c|字符|
|%s|通过str()字符串转换来格式化|
|%i|有符号十进制整数|
|%d|有符号十进制整数|
|%u|无符号十进制整数|
|%o|八进制整数|
|%x|十六进制整数（小写字母）|
|%X|十六进制整数（大写字母）|
|%e|索引符号（小写'e'）|
|%E|索引符号（大写'E'）|
|%f|浮点实数|
|%g|%f和%e的简写|
|%G|%f和%E的简写|

### 1.6.输入
python2:input("please input something.")、raw_input("please input something.")
python3:input("please input something.")
python3中的input()和python2中的raw_input()功能一样

### 1.7.运算符


















## 2.判断语句和循环语句