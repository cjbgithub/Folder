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
+ tuple(元祖)
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
|tuple(s)|将序列s转换为一个元祖|
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

## 3.字符串、列表、元祖、字典
### 3.1.字符串
字符串是用双引号（`a="hello"`）或单引号（`b='world'`）定义的数据  
字符串下表索引(index)：0 -> len(str)
> **切片`[起始位置：结束位置：步长]`**

切片是指对操作的对象截取其中的一部分的操作。字符串、列表、元组都支持切片操作。
> name="pythoncommand"的下标

|                      | p | y | t | h | o | n | c | o | m | m | a | n | d |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|index(0,...,len(str)-1)| 0 | 1 | 2 | 3 |  4|  5|  6|  7|  8|  9| 10| 11| 12|
|index(-len(str),...,-1)|-13|-12|-11|-10| -9| -8| -7| -6| -5| -4| -3| -2| -1|

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

|序号|名称|语法|描述|
|:---:|:---|:---|:---|
|1|find|`strings.find(str, start=0, end=len(strings))`|查找字符串并返回索引值，没有返回-1|
|2|index|`strings.index(str, start=0, end=len(strings))`|跟find()方法一样，没有时报异常|
|3|count|`strings.count(str, start=0, end=len(strings))`|查找字符串出现的次数|
|4|replace|`strings.replace(str1, str2, strings.count(str1))`|替换字符串，可指定替换次数|
|5|split|`strings.split(str=" ", 2)`|以指定分隔符切片字符串，可指定分割个数|
|6|capitalize|`strings.capitalize`|将字符串第一个字母大写|
|7|title|`strings.title()`|将字符串每一单词首字母大写|
|8|startswith|`strings.startswith(obj)`|检查字符串是否以obj开头，是则返回True，否则返回False|
|9|endswith|`strings.endswith(obj)`|检查字符串是否以obj结束，是则返回True，否则返回False|
|10|lower|`strings.lower()`|将字符串大写字母转换为小写字母|
|11|upper|`strings.upper()`|将字符串小写字母转换为大写字母|
|12|ljust|`strings.ljust(width)`|返回一个将原字符串左对齐，并使用空格扩充至长度width的新字符串|
|13|rjust|`strings.rjust(width)`|返回一个将原字符串右对齐，并使用空格扩充至长度width的新字符串|
|14|center|`strings.center(width)`|返回一个将原字符串居中对齐，并使用空格扩充至长度width的新字符串|
|15|lstrip|`strings.lstrip()`|返回一个将原字符串删除左边（开头）的空白字符的新字符串|
|16|rstrip|`strings.rstrip()`|返回一个将原字符串删除右边（结尾）的空白字符的新字符串|
|17|strip|`strings.strip()`|返回一个将原字符串删除两边的空白字符的新字符串|
|18|rfind|`strings.rfind(str, start=0, end=len(strings))`|类似于find()函数，从右边开始查找字符串|
|19|rindex|`strings.rindex(str, start=0, end=len(strings))`|类似于index()函数，从右边开始查找字符串|
|20|partition|`strings.partition(str)`|将字符串以str分割成三部分，str前，str和str后|
|21|rpartition|`strings.rpartition()`|类似于partition()函数，从右边开始|
|22|splitlines|`strings.splitlines()`|按照行分割，返回一个列表|
|23|isalpha|`strings.isalpha()`|如果字符串所有字符都是字母，返回True，否则返回False|
|24|isdigit|`strings.isdigit()`|如果字符串所有字符都是数字，返回True，否则返回False|
|25|isalnum|`strings.isalnum()`|如果字符串所有字符都是字母或数字，返回True，否则返回False|
|26|isspace|`strings.isspace()`|如果字符串只包含空格，返回True，否则返回False|
|27|join|`strings.join(str or set)`|返回字符串拼接构造出的新字符串|































