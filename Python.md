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
1. 直接点击**file.py**运行
2. cmd运行`python file.py`
3. cmd运行`file.py`
4. 打开IDLE（Python shell）打开文件点击Run -> Run module

### 1.2.注释
1. 单行注释（# ）
2. 多行注释（''' '''）
3. 中文支持（#coding=utf-8、#-\*-coding:utf-8-\*-）

### 1.3.变量类型
+ Numbers
  - int
  - long
  - float
  - complex(复数)
+ bool
  - True
  - False
+ str
+ list
+ tuple(元组)
+ Directory

查看变量类型：`type(variableName)`

### 1.4.标识符和关键字
标识符由**字母、下划线和数字**组成，且**数字不能开头**
**Python区分大小写**

> 查看Python关键字(不允许使用关键字定义标识符)
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
|%E|索引符号（大写"E"）|
|%f|浮点实数|
|%g|%f和%e的简写|
|%G|%f和%E的简写|

### 1.6.输入
python2：input("please input something.")、raw_input("please input something.")  
python3：input("please input something.")  
python3中的input()和python2中的raw_input()功能一样  

### 1.7.运算符
+ 算数运算符(a=10,b=20)

|运算符|描述|实例|
|:---:|:---|:---|
|+|加法|a+b=30|
|-|减法|a-b=-10|
|\*|乘法|a\*b=200|
|/|除法|b/a=2|
|//|取整除|返回商的整数部分|
|%|取余|返回商的余数部分|
|\**|幂|2\**2=4, 2\**10=1024|

+ 赋值运算符

|运算符|描述|实例|
|:---:|:---|:---|
|=|赋值运算符|把=右边的计算结果或引用给左边的变量|

+ 复合赋值运算符

|运算符|描述|实例|
|:---:|:---|:---|
|+=|加法赋值运算符|c+=a等效于c=c+a|
|-=|减法赋值运算符|c-=a等效于c=c-a|
|\*=|乘法赋值运算符|c*=a等效于c=c*a|
|/=|除法赋值运算符|c/=a等效于c=c/a|
|//=|取整除赋值运算符|c//=a等效于c=c//a|
|%=|取模赋值运算符|c%=a等效于c=c%a|
|\**=|幂赋值运算符|c**=a等效于c=c**a|

+ 比较（关系）运算符

|运算符|描述|实例|
|:---:|:---|:---|
|==|判断两个值是否相等|如a=3,b=3则(a==b)为True|
|!=|判断两个值是否不相等|如a=1,b=3则(a!=b)True|
|<>|判断两个值是否不相等|如a=1,b=3则(a!=b)True.类似于!=|
|>|判断右边值是否大于左边值|如a=7,b=3则(a>b)为True|
|<|判断左边值是否大于右边值|如a=7,b=23则(a<b)为True|
|>=|判断右边值是否大于等于左边值|如a=3,b=3则(a>=b)为True|
|<=|判断左边值是否大于等于右边值|如a=3,b=3则(a<=b)为True|

+ 逻辑运算符

|运算符|逻辑表达式|描述|
|:---:|:---:|:---|
|and|x and y|布尔"与"，x为True且y为True则返回True|
|or|x or y|布尔"或"，x为False且y为False则返回False|
|not|not x|布尔"非"|
### 1.8.数据类型转换
|运算符|描述|
|:---|:---|
|int(x [,base])|将x转换为一个整数|
|long(x [,base])|将x转换为一个长整数|
|float(x)|将x转换为一个浮点数|
|complex(real [,imag])|创建一个复数|
|str(x)|将对象x转换为字符串|
|repr(x)|将对象x转换为表达式字符串|
|**eval(x)**|用来计算在字符串中的有效Python表达式，并返回一个对象|
|tuple(s)|将序列s转换为一个元组|
|list(s)|将序列s转换为一个列表|
|chr(x)|将一个整数转换为一个字符|
|unichar(x)|将一个整数转换为Unicode字符|
|ord(x)|将一个字符转换为它的整数值|
|hex(x)|将一个整数转换为一个十六进制字符串|
|oct(x)|将一个整数转换为一个八进制字符串|

## 2.判断语句和循环语句
### 2.1.if语句
```
if condition 1 is True:
    do codes 1
# elif condition 2 is True:
#     do codes 2
# elif condition 3 is True:
#     do codes 3
else:
    do other codes
```
if可以嵌套
```
if condition 1 is True:
    if condition 1.1 is True:
        do codes 1
    elif condition 1.2 is True:
        do codes 2
    else:
        do codes 3
elif condition 2 is True:
    if condition 2.1 is True:
        do codes 4
else:
    do code 5
```

### 2.2.while循环
```
while condition is True:
    codes 1
    codes 2
    ...
```
> 实例99乘法表（i<=9为打印9行，j<=i为每行打印i次，\t为制表符）
```
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%d"%(i, j, i*j), end="\t")
        j += 1
    print()
    i += 1
```

### 2.3.for循环
```
for variable_temp in set(listOrStr...):
    do some codes...
else:
    循环条件不满足时执行的代码
```

### 2.4.break和continue
break结束所属层后面的循环  
continue跳过所属层当前循环，继续下一次循环  
break/continue只能在循环中使用，除此以外不能单独使用  
break/continue在嵌套循环中，只对临近层（所属层）循环起作用，其他层不起作用  
> for循环
```
name = "dabusidexiaoqiang"
for x in name:
    print("-----")
    if x == 'u':
        continue
    if x == "i":
        break
    print(x)
```

> while循环
```
i = 0
while i <= 9:
    i += 1
    if i == 8:
            break # 不打印第8行后面的
    j = 0
    while j <= i:
        j += 1
        if j == 5:
            continue # 不打印第5列，即跳过第五列打印
        print("(%d, %d)"%(i, j), end="\t")
    print()
```

## 3.字符串、列表、元组、字典
### 3.1.字符串
字符串是用双引号（`a="hello"`）或单引号（`b='world'`）定义的数据  
字符串下表索引(index)：0 -> len(str)
> **切片`[起始位置：结束位置：步长]`**

切片是指对操作的对象截取其中的一部分的操作。字符串、列表、元组都支持切片操作。
> name="pythoncommand"的下标

|                      | p | y | t | h | o | n | c | o | m | m | a | n | d |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|index(0，...，len(str)-1)| 0 | 1 | 2 | 3 |  4|  5|  6|  7|  8|  9| 10| 11| 12|
|index(-len(str)，...，-1)|-13|-12|-11|-10| -9| -8| -7| -6| -5| -4| -3| -2| -1|

```
name="pythoncommand"
print(name[0:3]) # 取下标0-2的字符
print(name[0:5]) # 取下标0-4的字符
print(name[3:5]) # 取下标3-4得字符
print(name[2:])  # 取下标为2开始到最后的字符
print(name[1:-2]) # 取下标1开始到最后第二个（len(str)-2）之间的字符，等价于print(name[1:len(name)-2])
print(name[::-1]) # 字符串反转
```

> 字符串常见操作

|序号|方法|描述|
|:---:|:---|:---|
|1|strings.**find**(str, start=0, end=len(strings))|查找字符串并返回索引值，没有返回-1|
|2|strings.**index**(str, start=0, end=len(strings))|跟find()方法一样，没有时报异常|
|3|strings.**count**(str, start=0, end=len(strings))|查找字符串出现的次数|
|4|strings.**replace**(str1, str2, strings.count(str1))|替换字符串，可指定替换次数|
|5|strings.**split**(str=" ", 2)|以指定分隔符切片字符串，可指定分割个数|
|6|strings.**capitalize**()|将字符串第一个字母大写|
|7|strings.**title**()|将字符串每一单词首字母大写|
|8|strings.**startswith**(obj)|检查字符串是否以obj开头，是则返回True，否则返回False|
|9|strings.**endswith**(obj)|检查字符串是否以obj结束，是则返回True，否则返回False|
|10|strings.**lower**()|将字符串大写字母转换为小写字母|
|11|strings.**upper**()|将字符串小写字母转换为大写字母|
|12|strings.**ljust**(width)|返回将原字符串左对齐，并用空格扩充至长度width的新字符串|
|13|strings.**rjust**(width)|返回将原字符串右对齐，并用空格扩充至长度width的新字符串|
|14|strings.**center**(width)|返回将原字符串居中对齐，并用空格扩充至长度width的新字符串|
|15|strings.**lstrip**()|返回将原字符串删除左边的空白字符的新字符串|
|16|strings.**rstrip**()|返回将原字符串删除右边的空白字符的新字符串|
|17|strings.**strip**()|返回将原字符串删除两边的空白字符的新字符串|
|18|strings.**rfind**(str, start=0, end=len(strings))|类似于find()函数，从右边开始查找字符串|
|19|strings.**rindex**(str, start=0, end=len(strings))|类似于index()函数，从右边开始查找字符串|
|20|strings.**partition**(str)|将字符串以str分割成三部分，str前，str和str后|
|21|strings.**rpartition**()|类似于partition()函数，从右边开始|
|22|strings.**splitlines**()|按照行分割，返回一个列表|
|23|strings.**isalpha**()|如果字符串所有字符都是字母，返回True，否则返回False|
|24|strings.**isdigit**()|如果字符串所有字符都是数字，返回True，否则返回False|
|25|strings.**isalnum**()|字符串所有字符都是字母或数字为True，否则返回False|
|26|strings.**isspace**()|如果字符串只包含空格，返回True，否则返回False|
|27|strings.**join**(str or set)|返回字符串拼接构造出的新字符串|

```
testStr = "haha nihao a \t heihei \t woshi nide \t hao \npengyou"
testStr.split() # \t、/n和空格都会去掉
```

### 3.2.列表
```
listA = [1, 2.3, "hello world", 'age10', ("tuple", 29)]
for item in listA:
    print(item)
i = 0
while i < len(listA):
    print(listA[i])
    i += 1
```
列表嵌套：列表可以作为一个元素添加到其他列表中

> 列表相关操作

1. 添加元素
    + append 末尾添加一个元素
    + extend 两个列表元素合并
    + insert(index, object) 在指定位置index前插入元素object
2. 修改元素
   + listA[index] = "content"
3. 查找元素
   + in、not in
   + index 同字符串函数index
   + count 同字符串函数count
4. 删除元素
   + del 根据元素下标删除元素
   + pop 删除最后一个元素
   + remove 根据元素的值进行删除
5. 排序
   + sort 将list按特定顺序进行排序，默认由小到大参数`reverse=True`可改为倒序，由大到小

### 3.3.元组、字典
元组语法格式：`(tuple1, tuple2, tuple3, ...)`元组**不可修改**  
访问元组`tuple[index]`，还可以使用count，index函数  
一个元素的元组：`a = (10,)`  

字典语法格式`{"key1": "value2", "key2": "value2"}`

> 字典常见操作

1. 修改元素
   + dic["key"] = "new_value"
2. 添加元素
   + dic["new_key"] = "new_value"
3. 删除元素
   + del dic["key"] 删除字典指定元素
   + dic.clear() 清空字典，返回空字典
4. 其他操作
   + len(dic) 返回字典元素个数
   + dic.values() 返回字典所有元素values的列表
   + dic.items() 返回字典所有元素key的列表
   + dic.has_key("key") 查找key是否存在，存在返回True，否则返回False

```
# 字符串遍历
for char in "hello world!":
    print(char, end=" ")
# 列表遍历
for item in [1, 2.3, "hello", 'char']:
    print(item, end=" ")
# 元组遍历
for num in (1, 2, 5, 10, 6):
    print(num, end=" ")
# 字典遍历
dict = {"name": "zhang", "age": "10", "address": "town"}
for item in dict.keys():
    print(item)
for item in dict.values():
    print(item)
for item in dict.items():
    print(item)
for key, value in dict.items():
    print("key=%s, value=%s"%(key, value))
for index, item in enumerate(dict.items()):
    print(index, item) # 带下标索引输出
```
**set 是集合类型，元素不重复**  
set、list、tuple之间可以相互转换  
使用set，可以实现对list中的元素去重
### 3.4.公共方法
> 运算符

|运算符|描述|支持的数据类型|python表达式|结果|
|:---|:---|:---|:---|:---|
|+|合并|字符串、列表、元组|[1, 2] + [3, 4]|[1, 2, 3, 4]|
|*|复制|字符串、列表、元组|"Hi!"*4|"Hi!Hi!Hi!Hi!"|
|in|元素是否存在|字符串、列表、元组、字典|3 in (1, 2, 3)|True|
|not in|元素是否不存在|字符串、列表、元组、字典|4 not in (1, 2, 3)|True|

注意，in在对字典操作时，判断的是字典的键

> python内置函数

|序号|方法|描述|
|:---:|:---|:---|
|1|cmp(item1, item2)|比较两个值|
|2|len(item)|计算容器中元素个数|
|3|max(item)|返回容器中元素最大值|
|4|min(item)|返回容器中元素最小值|
|5|del(item)|删除变量|

注意：cmp在比较字典数据时，先比较键，再比较值。len在操作字典数据时，返回的是键值对个数。

### 3.5.可变类型与不可变类型
**引用**是变量在内存的地址，用`id(obj)`来查看
1. 可变类型，值可以改变
    + 列表 list
    + 字典 dict
2. 不可变类型，值不可以改变
    + 数值类型 int, long, bool, float
    + 字符串 str
    + 元组 tuple

```
# 交换两个变量的值
a = 2
b = 3
a, b = (b, a)
a = a + b
b = a - b
a = a - b
```

## 4.函数
```
# 定义函数
def printInfo():
    "函数文档说明" # 还可以用 """函数文档说明""" 这种格式
    print("hello world")
    print(100 + 200)
# 调用函数
printInfo()
# 查看函数文档说明
help(printInfo)
```
定义函数时的参数为“形参”  
调用函数时的参数为“实参”  
函数也可以嵌套调用，即在函数A的定义中调用函数B，然后调用函数A

定义在函数内部的变量称为局部变量  
定义在函数外部的变量称为全局变量  
对于**不可变类型**，因其指向的数据不可修改，所以需要加`global variableName`才可以修改局部变量    
对于**可变类型**，因其引用的数据可修改，因此不使用`global`也可以修改局部变量

函数返回值可以是多个，原理同元组

> 缺省参数

调用函数，缺省参数没有传入时使用默认值
```
def info(name, age=35):
    return name, age # 等价于(name, age)
name, age = info("miki")
print(name, age)
print(info(age=12, name="xiaoming"))
```
注意：带有默认值的参数一定要位于参数列表的最后面。

> 不定长参数

不定长参数接受函数调用时传入的参数比定义的参数多出来的参数  
*args 存放所有未命名的变量参数，是一个元组  
**kwargs 存放命名参数，即形如 `key=value`的参数，kwargs为字典
```
def demo(a, b, *args, **kwargs):
    """不定长参数"""
    print("a=", a)
    print("b=", b)
    print("args=", args)
    print("kwargs:")
    for key, value in kwargs.items():
        print(key, "=", value)
demo(1, 2, 3, 4, 5, m=6, n=7, p=8)  # 注意传递的参数对应
c = (3, 4, 5)
d = {"m":6, "n":7, "p":8}
demo(1, 2, *c, **d)     # 注意元组与字典的传参方式
demo(1, 2, c, d)        # 注意不加星号与上面的区别
```

> 引用传参

Python中函数参数是引用传递  
对于不可变类型，因变量不能被修改，不会影响到变量自身  
对于可变类型，函数体中的运算有可能会更改传入的参数变量
```
def demo(a, b, c, d):
    """自增"""
    a = a + a
    b += b
    c = c + c # 不能修改list
    d += d
a_int = 1
b_int = 2
c_list = [1, 2]
d_list = [3, 4]
demo(a_int, b_int, c_list, d_list)
print(a_int)
print(b_int)
print(c_list)
print(d_list)
```

> 递归函数

自身循环调用的函数是递归函数
```
def demo(num):
    """num的阶乘：n!"""
    if num > 1:
        print(num, end="*") 
        return num * demo(num-1)
    elif num == 1:
        print(num, end=" = ") 
        return 1
    else:
        print("Num is Error.")
print(demo(10))
```

> 匿名函数
```
lambda [arg1 [, arg2, ...argn]: expression
```
Lambda函数能接受任何数量的参数但是只能返回一个表达式的值  
匿名函数不能直接用print，因为lambda需要一个表达式
```
stus = [
    {"name":"zhangsan", "age":18},
    {"name":"lisi", "age":24},
    {"name":"wangwu", "age":10}
]
stus.sort(key = lambda x: x['name'])    # 按name排序
stus.sort(key = lambda x: x['age'])     # 按age排序
```

> 运行程序时传参数并返回list
```
# demo.py
import sys
print(sys.argv)

# 运行程序
python demo.py haha 1 2 3 44
```
## 5.文件操作
### 5.1.文件打开、关闭及定位
> 打开文件
`f = open('test.txt', 'w')`

|访问模式|说明|
|:---:|:---|
|r|只读，文件指针指向文件开头。默认打开模式|
|w|写入，文件存在时覆盖重写，文件不存在时创建文件|
|a|追加，文件存在时末尾追加，文件不存在时创建文件并写入|
|rb|只读，二进制格式打开，文件指针指向文件开头|
|wb|写入，二进制格式打开，文件存在时覆盖重写，文件不存在时创建文件|
|ab|追加，二进制格式打开，文件存在时末尾追加，文件不存在时创建文件并写入|
|r+|读写，文件指针指向文件开头|
|w+|读写，文件存在时覆盖重写，文件不存在时创建文件|
|a+|读写，文件存在时末尾追加，文件不存在时创建文件并写入|
|rb+|读写，二进制格式打开，文件指针指向文件开头|
|wb+|读写，二进制格式打开，文件存在时覆盖重写，文件不存在时创建文件|
|ab+|读写，二进制格式打开，文件存在时末尾追加，文件不存在时创建文件并写入|

> 读写文件
```
f.write("hwllo world...")
f.read(5) # 每次读取5个字节
f.readline() # 每次只读取一行数据
f.readlines() # 将整个文件一次读取，返回以一行的数据为元素的一个列表
```

> 关闭文件
`f.close()`

> 文件备份
```
#coding=utf-8
oldFileName = input("请输入需要拷贝的文件名字：")
oldFile = open(oldFileName, 'r')
if oldFile:
    # 提取文件的后缀
    fileFlagNum = oldFileName.rfind('.')
    if fileFlagNum > 0:
        fileFlag = oldFileName[fileFlagNum:] # 文件后缀名
    
    # 组织新的文件名
    newFileName = oldFileName[:fileFlagNum] + '[复件]' + fileFlag
    
    # 创建新的文件
    newFile = open(newFileName, 'w')
    
    # 把旧文件中数据一行一行的复制到新文件中
    for lineContent in oldFile.readlines():
        newFile.write(lineContent)
    
    # 关闭文件
    newFile.close()
    oldFile.close()
```
> 文件定位
1. tell() 定位当前位置
2. seek(offset, from)定位到指定位置
    + offset 偏移量，正数向右偏移，负数向左偏移
    + from 0表示文件开头，1表示当前位置，2表示文件末尾

### 5.2.文件重命名及删除
> 文件重命名
```
import os
os.rename("file1.txt", "newFile.txt")
```

> 删除文件
```
import os
os.remove("file.txt")
```

### 5.3.文件夹操作
```
import os
os.mkdir("dirName") # 创建文件夹
os.getcwd()         # 获取当前目录
os.chdir("../")     # 改变默认目录
os.listdir("./")    # 获取目录列表
os.rmdir("dirName") # 删除文件夹
```

### 5.4.批量修改文件名
```
#coding=utf-8
import os
funFlag = 1 # 1表示添加标志，2表示删除标志

folderName = "./renameDir/"

# 获取指定路径的所有文件名
dirList = os.listdir(folderName)

# 遍历出所有文件名字
for name in dirList:
    print(name)
    
    if funFlag == 1:
        newName = "[添加标志]-" + name
    elif funFlag == 2:
        num = len("[添加标志]-")
        newName = name[num:]
    print(newName)

    os.rename(folderName+name, folderName+newName)
```

## 6.面向对象
面向对象（object-oriented,简称OO）  
面向对象编程(Object Oriented Programming-OOP) 

### 6.1.类和对象

将具有相同功能的数据和代码进行封装 -> 函数
将具有相同属性和行为的函数进行封装 -> 类

> 类（class）的构成
1. 类名
2. 类属性
3. 类方法

> 定义类
```
class CName(object):
    """定义一个类"""
    
    # __new__至少要有一个参数cls，代表要实例化的类，在实例化时由Python解释器自动提供
    # __new__必须要有返回值，返回实例化出来的实例
    def __new__(cls):
        do ...
        return object.__new__(cls)
    
    # self是实例化出来的实例的引用
    # 初始化方法，创建对象后程序自动调用
    def __init__(self, name):
        # 给对象添加私有属性，更好的保护数据的安全性
        self.__name = name
    
    # 打印对象属性，默认打印对象在内存中的地址
    def __str__(self):
        return self.attr...
    
    # 变量保存对象引用时此对象记数自增，删除一个变量则记数自减
    # 当只有一个变量保存对象引用并删除该变量时，对象真正被删除
    # 析构方法，对象被删除时程序自动调用
    def __del__(self):
        do codes...
    
    # 对外访问私有属性的接口
    def getName(self):
        return self.__name
    # 对外修改私有属性的接口
    def setName(self, newName):
        self.__name = newName
    
    def method1():
        do codes...
    def method2(a, b, ...):
        do codes...
    ...
```

> 创建对象
```
# 创建一个对象
obj = CName()
# 给对象添加属性
obj.attr = "attribute"
# 修改对象属性
obj.attr = "newValue"
# 调用对象方法
obj.method1()
```

### 6.2.继承
```
class CName(object):
    "定义一般类"
    def method:
        do ...

class CName(AName):
    "单继承"
    def method:
        do ...

class CName(AName, BName):
    "多继承"
    def method:
        do...

# 查看类CName的对象搜索方法时的先后顺序
print(CName.__mro__)

# 调用父类方法
super().__init__(args)
```
- 不能通过对象直接访问私有属性，可以通过方法访问
- 不能通过对象直接访问私有方法
- 私有属性、方法不能被子类继承，也不能被访问
- 一般情况，私有属性、方法不对外公布，起到安全的作用

### 6.3.多态
```
class F1(object):
    def show(self):
        print('F1.show')

class S1(F1):
    def show(self):
        print('S1.show')

class S2(F1):
    def show(self):
        print('S2.show')

def fun(obj)
    print(obj.show())

s1_obj = S1()
fun(s1_obj)

s2_obj = S2()
fun(s2_obj)
```

### 6.4.类属性、实例属性

类属性是 类对象 拥有的属性，被 类对象 的 实例对象 共有，内存中只存在一份  
类属性必须通过类对象去引用然后进行修改  
实例对象引用修改时产生一个同名的实例属性，而不能修改类属性

### 6.5.类方法和静态方法

> 类方法

@classmethod 修饰的方法为类方法，第一个参数必须是类对象cls  
类方法可以修改类属性

> 静态方法

@staticmethod 修饰的方法为静态方法，不需要多定义参数  
静态方法必须通过类对象来引用类属性


类方法，可修改类属性，可查看类属性
实例方法，可修改实例属性，可访问类属性、实例属性  
静态方法，可修改实例属性或类属性，可访问类属性、实例属性

### 6.6.单例模式
```
class Singleton(object):
    __instance = None
    __firtst_init = False

    def __new__(cls, name, age):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, name, age):
        if not self.__firtst_init:
            self.name = name
            self.age = age
            Singleton.__firtst_init = True

a = Singleton("zhangsan", 19)
b = Singleton("lisi", 18)

print(id(a))
print(id(b))

a.age = 20
print(b.age)
```

## 7.异常
```
try:
    do...
except:
    # 重新抛出这个异常，触发默认的异常处理
    raise

try:
    do...
except NameError as result:
    print(result)

try:
    do...
except (NameErroe, IOError) as result:
    print(result)

try:
    do...
except Exception as result:
    print(result)
else:
    print("程序正常运行时输出")
finally:
    # 无论是否发生异常都必须执行的代码
    # 比如关闭文件，释放锁，返回数据库连接池
    do...
```

> raise引发一个自定义异常
```
class ShortInputException(Exception):
    "自定义异常类"
    def __init__(self, length, atleast):
        # super().__init__()
        self.length = length
        self.atleast = atleast

def main():
    try:
        s = input("请输入 --> ")
        if len(s) < 3:
            raise ShortInputException(len(s), 3)
    except ShortInputException as result:
        print("ShortInputException: 输入的长度是 %d,长度至少应是 %d"%(result.length, result.atleast))
    else:
        print('没有发生异常。')

main()
```

## 8.模块
## 8.1.模块介绍
Python中的模块（module）类似于C中的头文件和Java中的包  
Python中的module可以理解为一个工具包，加载进来就可以使用其中的工具（函数）

- import
- from ... import
- from ... import *
- import time as tt

> 定位module

1. 当前目录
2. shell变量PYTHONPATH下的每个目录
3. 默认目录。UNIX下默认路径：/usr/local/lib/python/

模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

## 8.2.模块制作
Python执行一个文件时有个变量__name__  
变量__name__在文件本身调用时显示__mian__  
变量__name__在其他文件import时显示调用文件的文件名  
因此__name__可以在文件中来执行测试代码而不被其他文件import时执行
> test.py
```
#coding=utf-8
# __all__变量指定from xxx import * 时可以导入的元素
__all__ = ["test1"]

def add(a, b):
    return a + b
def test1():
    print("-----test1函数-----")
def test2():
    print("-----test2函数-----")
print("__name__ is %s"%__name__)
if __name__ == "main":
    print('test coding...')
```
> main.py
```
#coding=utf-8
import test
result = test.add(11, 22)
print(result)
```













































