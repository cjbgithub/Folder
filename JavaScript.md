ECMAScript是一种脚本标准，明确了一个脚本编程语言的基本内容，包括关键字、语法、api标准等。

js（JavaScript）是ECMAScript的一个具体实现，并且扩展了DOM和BOM等。

# 1. JavaScript基础

```js
// 加载JavaScript的两种方式
<script></script>
<script src="***.js"></script>
// 默认type="text/javascript"
<script type="text/javascript"></script> 等价于 <script></script>
```

## 1.1 基本语法

1. 语法

​	JavaScript的每个语句以`;`结束，语句块用`{...}`。JavaScript不强制要求每条语句加`;`，浏览器引擎执行时会自动补上`;`，但是不加分号在某些情况下会改变程序的语义，导致运行结果与期望值不一致。

2. 注释

```js
// 1.单行注释
/*
2.多行注释
*/
```

3. 大小写

   **JavaScript严格区分大小写**

## 1.2 数据类型和变量

**1. 数据类型**（Number、字符串、布尔值、数组、对象、null/undefined）

+ Number

```js
123; // 整数123
0.456; // 浮点数0.456
1.2345e3; // 科学计数法表示1.2345x1000，等同于1234.5
-99; // 负数
NaN; // NaN表示Not a Number，当无法计算结果时用NaN表示
Infinity; // Infinity表示无限大，当数值超过了js的Number所能表示的最大值时，就表示为Infinity
```

+ 字符串

```js
// 1.单引号或者双引号括起来的任意字符，字符串不可变
var s = 'Test';
s[0]; // 'T'
s[0] = 'X';
alert(s); // s仍然为'Test'
// 2.字符串本身包含单双引号使用转义字符：\
\n换行，\t制表符，\\表示\本身，\x十六进制，\u表示一个Unicode字符
// 3.多行字符串：使用\n、ES6使用反引号`...`
// 4.ES6模版字符串：
var name = '小明';
var age = 20;
alert('你好, ' + name + ', 你今年' + age + '岁了!'); // 常规表示连接字符串
alert(`你好, ${name}, 你今年${age}岁了!`); // 使用模版字符串
// 5.字符串操作：toUpperCase、toLowerCase、substring（返回一个新的字符串）和indexOf
var s = 'Hello';
s.toUpperCase(); // 返回'HELLO'
var lower = s.toLowerCase(); // 返回'hello'并赋值给变量lower
s.substring(0, 3); // 从索引0开始到3（不包括3），返回'Hel'
s.substring(2); // 从索引2开始到结束，返回'llo'
s.indexOf('ello'); // 返回1
s.indexOf('hello'); // 没有找到指定的子串，返回-1
```

+ 布尔值

```js
// 1.直接使用true/false
// 2.比较运算：==、===、>、< ...
// 3.布尔运算：&&与、||或、!非
```

+ null/undefined

```js
// null表示一个空的值，undefined表示一个值未定义
```

+ 数组

```js
// 数组是一组按顺序排列的集合，集合的每个值称为元素。JavaScript的数组可以包括任意数据类型。索引起始值为0
[1, 2, 3.14, 'Hello', null, true]; // 推荐使用
new Array(1, 2, 3); // 创建了数组[1, 2, 3]
```

+ 对象

```js
// 对象是一组由键-值组成的无序集合，对象的键都是字符串类型，值可以是任意数据类型
var person = {
    name: 'Bob',
    age: 20,
    tags: ['js', 'web', 'mobile'],
    city: 'Beijing',
    hasCar: true,
    zipcode: null
};
// 获取对象属性：对象变量.属性名
person.name; // 'Bob'
person.zipcode; // null
```

**2. 比较运算符**

```js
// JavaScript允许对任意数据类型做比较
false == 0; // true
false === 0; // false
// 1.==比较，会自动转换数据类型再比较，很多时候，会得到非常诡异的结果（不推荐使用）
// 2.===比较，它不会自动转换数据类型，如果数据类型不一致，返回false，如果一致，再比较
// 3.NaN比较特殊，与其他值都不相等，包括NaN本身
NaN === NaN; // false
// 4.唯一能判断NaN的方法是通过isNaN()函数：
isNaN(NaN); // true
// 5.浮点数比较存在误差,要比较两个浮点数是否相等，只能计算它们之差的绝对值，看是否小于某个阈值
1 / 3 === (1 - 2 / 3); // false
Math.abs(1 / 3 - (1 - 2 / 3)) < 0.0000001; // true
```

**3. 变量**

```js
// 1.变量在JavaScript中使用一个变量名表示，变量名是大小写英文、数字、$和_的组合，且不能用数字开头
// 2.变量名也不能是JavaScript的关键字
```

**4. strict模式**

```js
// 1.JavaScript中var声明的变量不是全局变量，但是不强制用var声明
// 2.不使用var声明的变量称为全局变量，引入多个JavaScript文件时，会由于多个变量冲突而引起错误
// 3.ECMAScript使用strict模式，修补上述JavaScript的设计缺陷，此模式下强制使用var声明变量
'use strict'; // 加在JavaScript代码首行，声明变量时未使用var将导致运行错误
```

## 1.3 数组

JavaScript的Array可以包含任意数据类型，并通过索引类访问每个元素

Array通过length属性访问数组的长度，直接给Array的length属性赋新值会改变数组大小，包括索引超出范围

indexOf() 来搜索一个指定的元素的位置

slice() 是对应String的substring()版本，截取Array的部分元素，然后返回一个新的Array

push()和pop() 用来操作Array的最后一个元素

unshfit()和shift() 用来操作Array的第一个元素，shift()删除第一个元素

sort() 可以对当前Array进行排序

reverse() 可以把Array反转

splice(start, sum, ele1, ...) 可以从指定索引开始删除sum个元素，然后从该位置添加若然元素

concat() 将两个Array连接并返回一个新的Array，即合并连个Array的元素

join() 将当前Array的每个元素用指定字符串连接起来，然后返回连接后的字符串

```js
// 输出 欢迎小明,小红,大军和阿黄同学！
'use strict';
var arr = ['小明', '小红', '大军', '阿黄'];
console.log(`欢迎${arr.slice(0,3).join(',')}和${arr[3]}同学！`);
```

## 1.4 对象

JavaScript用`{...}`表示一个对象，键值对以`xxx: xxx`形式申明，用`,`隔开，最后一个键值对不需要在末尾加`,`

属性是一个有效的变量名时，用`.`访问，如果包含特殊字符，必须用`''`括起来，并且用`['xxx']`来访问

`in`操作符可以检测对象是否拥有某一属性，但是这个属性有可能是继承得到的

`hasOwnProperty()`方法可以检测一个属性是否是对象自身拥有而不是继承得到的

## 1.5 Map和Set

JavaScript中对象的键必须是字符串

ES6规范引入了新的数据类型Map，其中的键除了字符串可以是其他数据类型

ES6规范引入了新的数据类型Set，是一组不重复key的集合，但是不存储value，即set中没有重复值

## 1.6 iterable

因为Map和Set无法使用下标遍历，ES6统一使用iterable类型，Array、Map、Set都属于iterable类型

`for...in`遍历Array实际上是在遍历Array对象，它的每一个索引被视为一个属性，手动给Array对象添加额外的属性后，`for...in`遍历会产生异常结果，因此iterable类型使用`for...of`遍历

```js
var a = ['A', 'B', 'C'];
a.name = 'Hello';
for (var x in a) {
    console.log(x); // '0', '1', '2', 'name'
}
for (var x of a) {
    console.log(x); // 'A', 'B', 'C'
}
```

iterable内置有forEach方法（ES5.1标准引入），它接受一个函数，每次迭代会自动回调该函数

```js
'use strict';
var a = ['A', 'B', 'C'];
a.forEach(function (element, index, array) {
    // element: 指向当前元素的值
    // index: 指向当前索引
    // array: 指向Array对象本身
    // Set没有索引，因此回调函数的前两个参数都是元素本身
    // Map的回调函数参数为(value, key, map)
    // JavaScript的函数调用不要求参数必须一致，因此可以忽略部分参数
    console.log(element + ', index = ' + index);
});

```

# 2. 函数

+ 函数作为参数--高阶函数
+ 函数作为返回值--闭包

## 2.1 定义函数

```js
// 1.function指出这是一个函数定义
// 2.add是函数的名称
// 3.(x, y)括号内列出函数的参数，多个参数以 , 分割
// 4.{...}之间的代码是函数体，可以包含若干语句，甚至可以没有任何语句
// 5.一旦执行到return语句，函数就执行完毕，将结果返回。没有return语句，函数执行完后返回undefined
function add(x, y) {return x+y;}
// 6.JavaScript的函数也是一个对象，上述定义的add()函数实际上是一个函数对象，add可视为指向该函数的变量
var add = function (x, y) {return x+y;};
// function (x) {...}是匿名函数，没有函数名，在将匿名函数赋值给变量时，需要在末尾加;，表示赋值语句结束
```

+ arguments

arguments只在函数内部起作用，并且指向当前函数的调用者传入的所有参数

+ rest

`...rest`用来在函数内部接受调用者传入的除函数定义的其余参数

## 2.2 变量作用域与解构赋值

+ 变量作用域

在函数体内部用var声明的变量其作用域为整个函数体

函数嵌套时，内部函数可以访问外部函数定义的变量

JavaScript函数定义会扫描整个函数体的语句，将所有声明的变量“提升”到函数顶部，赋值位置不变

不在任何函数内部定义的变量就具有全局作用域

JavaScript默认又一个全局对象window，全局作用域的变量实际上被绑定到window的一个属性

```js
'use strict';

var course = 'Learn JavaScript';
alert(course); // 'Learn JavaScript'
alert(window.course); // 'Learn JavaScript'

function foo() {
    alert('foo');
}
foo(); // 直接调用foo()
window.foo(); // 通过window.foo()调用
```

以上说明，JavaScript实际上只有一个全局作用域，任何变量（函数也视为变量），如果没有在当前函数作用域中找到，就继续往上查找，最后在全局作用域中也没有找到，则包ReferenceError错误

全局变量会绑定到window上，不同的JavaScript文件定义相同的全局变量会造成冲突，可以将所有变量和函数绑定到一个全局变量中来解决冲突问题

```js
// 唯一的全局变量MYAPP:
var MYAPP = {};

// 其他变量:
MYAPP.name = 'myapp';
MYAPP.version = 1.0;

// 其他函数:
MYAPP.foo = function () {
    return 'foo';
};
```

JavaScript的变量作用域实际上是函数内部，for循环等语句块中无法定义具有局部作用域的变量

ES6使用新关键字`let`代替`var`来声明一个块级作用域的变量

```js
'use strict';

function foo() {
    var sum = 0;
    for (let i=0; i<100; i++) {
        sum += i;
    }
    // SyntaxError:
    i += 1;
}
```

`var`和`let`声明的是变量，ES6使用新关键字`const`来定义常量，常量不可修改。`let`与`const`都具有块级作用域

```js
'use strict';

const PI = 3.14;
PI = 3; // 某些浏览器不报错，但是无效果！
PI; // 3.14
```

+ 解构赋值

解构赋值就是对多个变量同时赋值

```js
'use strict';
// 对数组元素进行解构赋值时，多个变量需要用{...}括起来
var [x, y, z] = ['hello', 'JavaScript', 'ES6'];
// 解构赋值忽略某些元素
let [, , z] = ['hello', 'JavaScript', 'ES6'];
// 使用解构赋值快速获取对象的指定属性
var person = {
    name: '小明',
    age: 20,
    gender: 'male',
    passport: 'G-12345678',
    school: 'No.4 middle school'
};
var {name, age, passport} = person;
// 使用的变量名和属性名不一致时使用如下语法
let {name, passport:id} = person;
// 解构赋值使用默认值
var {name, single=true} = person;
// 解构赋值获取对象属性时，如果对象属性不存在，变量将被赋值为undefined
// 和引用一个不存在的属性获得undefined一致
// {...}={...}结构赋值时，JavaScript引擎会把前一个{...}语句当作快处理，=不再合法，因此需要()括起来
function buildDate({year, month, day, hour=0, minute=0, second=0}) {
    return new Date(year+'-'+month+'-'+day+' '+hour+':'+minute+':'+second);
}
buildDate({ year: 2017, month: 1, day: 1 }); // Sun Jan 01 2017 00:00:00 GMT+0800 (CST)
buildDate({ year: 2017, month: 1, day: 1, hour: 20, minute: 15 });
// Sun Jan 01 2017 20:15:00 GMT+0800 (CST)
```

## 2.3 方法

绑定到对象上的函数称为方法，方法内部使用关键字`this`来指向当前对象

在以方法模式调用函数时，`this`指向被调用对象：`obj.xxx()`的形式调用

在以函数模式调用函数时，`this`指向全局对象window

```js
function getAge() {
    var y = new Date().getFullYear();
    return y - this.birth;
}

var xiaoming = {
    name: '小明',
    birth: 1990,
    age: getAge
};

xiaoming.age(); // 25, 正常结果
getAge(); // NaN

var fn = xiaoming.age; // 先拿到xiaoming的age函数
fn(); // NaN
```

ECMA规定在strict模式下，函数的`this`指向undefined

```js
'use strict';

var xiaoming = {
    name: '小明',
    birth: 1990,
    age: function () {
        var that = this; // 在方法内部一开始就捕获this
        function getAgeFromBirth() {
            var y = new Date().getFullYear();
            return y - that.birth; // 用that而不是this
        }
        return getAgeFromBirth();
    }
};

xiaoming.age(); // 25
```

+ `apply(obj, [])`第一个参数将`this`指向对象，第二个参数将参数打包成Array再传入
+ `call(obj, arg1, ...)`第一个参数将`this`指向对象，第二个参数将参数按顺序传入

普通函数调用通常把`this`绑定为`null`

+ 装饰器

```js
'use strict';

var count = 0;
var oldParseInt = parseInt; // 保存原函数

window.parseInt = function () {
    count += 1;
    return oldParseInt.apply(null, arguments); // 调用原函数
};
```

## 2.4 高阶函数

将另一个函数作为参数的函数叫做高阶函数

+ map()

作用于数组的每一个元素做运算，比如x的平方

+ reduce()

将数组的每个元素做累积运算，比如累加

+ filter()

将数组的元素按照条件过滤掉

+ sort()

`sort()`默认按照ASCII码进行排序，数字排序2在10后面，字符串排序Go在ap后面（小写子码在大写字母后）

```js
'use strict';
// 数组元素首字母大写
function normalize(arr) {
    return arr.map(function(x){return x[0].toUpperCase()+x.slice(1).toLowerCase()});
}
// 数组元素求积
function product(arr) {
    return arr.reduce(function(x, y){return x*y});
}
// 数组元素去重
var r = arr.filter(function (element, index, self) {
    return self.indexOf(element) === index;
});
// 按数字大小正常排序
var arr = [10, 20, 1, 2];
// 1.正常写法：x<y:-1 x>y:1 x=y:0
arr.sort(function (x, y) {
    if (x < y) {return -1;}
    if (x > y) {return 1;}
    return 0;
});
// 2.简写（只适用于数字）
arr.sort(function (x, y) {return x-y}); // [1, 2, 10, 20]
// 3.反序排列
arr.sort(function (x, y) {return y-x}); // [20, 10, 2, 1]
// 字符串忽略大小写按字母排序：先统一大写（或小写），再排序
var arr = ['Google', 'apple', 'Microsoft'];
arr.sort(function (s1, s2) {
    x1 = s1.toUpperCase();
    x2 = s2.toUpperCase();
    return x1>x2 ? 1 : (x1<x2 ? -1 : 0);
});// ['apple', 'Google', 'Microsoft']
```

## 2.5 闭包

函数中将另一个函数定义作为结果返回的函数叫做闭包

```js
// 定义匿名函数
function(){}
// 定义并执行匿名函数
(function(){})()
// 使用闭包：内部函数定义时并没有执行
function () {
    var arr = [];
    for (var i=1; i<=3; i++) {
        console.log(i);
        arr.push(function () {
            console.log(i*i);
            return i * i;
        });
    }
}
(function () {
    var arr = [];
    for (var i=1; i<=3; i++) {
        console.log(i);
        arr.push(function () {
            console.log(i*i);
            return i * i;
        }(i));
    }
})()
```





























# 3. 标准对象



# 4. 面向对象编程



# 5. 浏览器



# 6. jQuery



# 7. 错误处理



# 8. userscore



# 9. Node.js





# 10. ECMAScript 6

1. **变量提升**（hoisting）：var 会将变量声明提升到当前作用域顶部，赋值位置不变

2. **let** 在**块级作用域**（语句块之外无法访问，变量声明不会变量提升）内声明变量
3. 同级作用域内禁止重复声明变量
4. 常量（constant）：**const**声明并初始化。不可更改（对象属性可修改），是块级声明。const 阻止对变量绑定的修改，不阻止对成员值的修改
5. 
6. 









































































