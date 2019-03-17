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
# 实例99乘法表（i<=9为打印9行，j<=i为每行打印i次，\t为制表符）
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
```
# for循环
name = "dabusidexiaoqiang"
for x in name:
    print("-----")
    if x == 'u':
        continue
    if x == "i":
        break
    print(x)

# while循环
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









































