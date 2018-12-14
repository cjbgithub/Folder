# VUE笔记
Vue 的核心是一个允许采用简洁的模版语法来声明式的将数据渲染进DOM的系统
# 0.VUE基础配置
### 环境搭建
- node -v
- npm -v
- npm i -g cnpm --registry=https://registry.npm.taobao.org	->npm镜像
- cnpm i -g vue-cli
- vue -V
### 0.1.安装项目
- vue init webpack vue_project_name

	提示目录已存在，是否继续：Y  
	Project name（工程名）:回车  
	Project description（工程介绍）：回车  
	Author：作者名  
	Vue build（是否安装编译器）:回车  
	Install vue-router（是否安装Vue路由）：回车  
	Use ESLint to lint your code（是否使用ESLint检查代码，我们使用idea即可）：n  
	Set up unit tests（安装测试工具）：n  
	Setup e2e tests with Nightwatch（测试相关）：n  
	Should we run `npm install` for you after the project has been created? (recommended)：选择：No, I will handle that myself
### 0.2.初始化
- cd vue_project_name
- cnpm i
- cnpm run dev
- Ctrl+C退出运行
cnpm install -g live-server
### 0.3.配置idea

	File-Settings-Languages&Frameworks-JavaScript：修改JavaScript language version为ECMAScript 6，确认。
	File-Settings-Plugins：搜索vue，安装Vue.js。
	Run-Edit Configurations...：点击加号，选择npm，Name为Run，package.json选择你工程中的package.json，Command为run，Scripts为dev,然后就可以直接在idea中运行了。
**npm 是 nodejs 的包管理和分发工具。**

```
<div id="vue_det">
    <h1>site : {{site}}</h1>
    <h1>url : {{url}}</h1>
    <h1>{{details()}}</h1>
</div>
```
> [Vue从入门到精通视频教程](http://www.javaxxz.com/forum.php?mod=viewthread&tid=346769&highlight=vue)
> v-fot，v-text，v-html，v-on
> v-model，v-bind，v-pre，v-cloak，v-once
> v-directive，

```
<div v-if="flag">content</div>
<div v-show="flag">content</div>
<li v-for="item in items">{{ item }}</li>
<button v-on:click="event">content</button>
<button @click="event">content</button>
```
[Axios](https://www.kancloud.cn/yunye/axios/234845)
## 1.Vue指令
### 1.1. Hello World
#### 1.下载vue开发版本
[Vue开发版本](https://vuejs.org/js/vue.js)包含警告和调试，压缩后的为生产版本。[Vue.js教程](https://cn.vuejs.org/v2/guide/installation.html)
#### 2.项目结构
vue-test  
- assets(js/css)
- demo
- index.html
#### 3.初始化项目
`npm init`
#### 4.搭建服务
安装命令：`cnpm install -g live-server`  
运行命令：`live-server`
#### 5.helloworld.html
```
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script type="text/javascript" src="../assets/js/vue.js"></script>
    <title>Hello World</title>
</head>
<body>
<div id="app">
    {{ message }}
</div>

<script type="text/javascript">
    var app = new Vue({
        el: "#app",
        data: {
            message: "Hello Vue World!"
        }
    })
</script>
</body>
</html>
```
### 1.2.v-if，v-else，v-show
```
<body>
<div id="app">
    <div v-if="ok">加载</div>
    <div v-else>不加载</div>
</div>

<script type="text/javascript">
    var app = new Vue({
        el: "#app",
        data: {
            ok: true
        }
    })
</script>
</body>
```
----------

```
<body>
<div id="app">
    <div v-show="show">显示</div>
</div>

<script type="text/javascript">
    var app = new Vue({
        el: "#app",
        data: {
            show: true
        }
    })
</script>
</body>
```
- v-if：判断是否加载，可以减轻服务器的压力，在需要时加载。
- v-show：调整css dispaly属性，可以使客户端操作更加流畅。
### 1.3.v-for
#### 1.基本用法
```
<div id="app">
    <ul>
        <li v-for="array in arrays">{{ array }}</li>
    </ul>
</div>

<script type="text/javascript">
    var app = new Vue({
        el: "#app",
        data: {
            arrays: [1, 90, 12, 44, 23, 35, 53, 62, 80, 91, 89, 4, 100]
        }
    })
</script>
```
#### 2.排序

vue不允许修改定义好的数据源，因此要定义一个新的对象接收排完序的数据，并使用此对象进行v-for循环显示
```
<div id="app">
    <ul>
        <li v-for="array in sortArrays">{{ array }}</li>
    </ul>
</div>

<script type="text/javascript">
    var app = new Vue({
        el: "#app",
        data: {
            arrays: [1, 90, 12, 44, 23, 35, 53, 62, 80, 91, 89, 4, 100]
        },
        computed: {
            sortArrays: function () {
                return this.arrays.sort(sortNum);
            }
        }
    })

    function sortNum(a, b) {
        return a - b;
    }
</script>
```
#### 3.对象循环输出
```
<div id="app">
    <ul>
        <li v-for="(array, index) in sortStudents">{{ index }}:{{ array.name }}-{{ array.age }}</li>
    </ul>
</div>

<script type="text/javascript">
    var app = new Vue({
        el: "#app",
        data: {
            students: [
                {name: 'jspang', age: 32},
                {name: 'Panda', age: 30},
                {name: 'PanPaN', age: 21},
                {name: 'King', age: 45}
            ]
        },
        computed: {
            sortStudents: function () {
                return sortObj(this.students, 'age');
            }
        }
    })

    function sortObj(obj, key) {
        return obj.sort(function (a, b) {
            var x = a[key];
            var y = b[key];
            return x - y; // return (x < y ? -1 : (x > y ? 1 : 0));
        })
    }
</script>
```
### 1.4.v-text，v-html
```
<span v-text="message"></span>
<span v-html="message"></span>
```
v-text: 在JavaScript出错或者网络延迟时避免显示{{ message }}  
v-html: 输出HTML文本内容，不建议使用
### 1.5.v-on
v-on就是监听事件
```
<div id="app">
    {{ score }}<br>
    <button v-on:click="add">加分</button>
    <button @click="sub">减分</button>
    <input type="text" v-on:keyup.enter="onEnter" v-model="addscore">
    <input type="text" @keyup.13="onEnter" v-model="addscore">
</div>

<script type="text/javascript">
    var app = new Vue({
        el: '#app',
        data: {
            score: 0,
            addscore: ''
        },
        methods: {
            add: function () {
                this.score++;
            },
            sub: function () {
                this.score--;
            },
            onEnter: function () {
                this.score = this.score + parseInt(this.addscore);
            }
        }
    })
</script>
```
![键值表](https://github.com/cjbgithub/Folder/blob/master/keyboard.png)
### 1.6.v-model指令
v-model实现双向数据绑定
```
<div id="app">
    <input type="text" v-model="message">
    1.修饰符：lazy(延迟加载，失去焦点时改变值) number trim
    <input type="text" v-model.lazy="message">
    <input type="text" v-model.number="message">
    <input type="text" v-model.trim="message">
    2.文本框
    <textarea cols="30" rows="3" v-model="message"></textarea>
    3.多选按钮绑定一个值
    <input type="checkbox" id="id" v-model="isTrue">
    <label for="id">点击文字选中/取消</label>
    {{ isTrue }}
    4.多选绑定一个数组
    <input type="checkbox" id="id1" value="Jack" v-model="names">
    <label for="id1">Jack</label>
    <input type="checkbox" id="id2" value="Marray" v-model="names">
    <label for="id2">Marray</label>
    <input type="checkbox" id="id3" value="David" v-model="names">
    <label for="id3">David</label>
    {{ names }}
    5.单选按钮绑定数据
    <label><input type="radio" value="男" v-model="sex">男</label>
    <label><input type="radio" value="女" v-model="sex">女</label>
    {{ sex }}
</div>

<script type="text/javascript">
    var app = new Vue({
        el: "#app",
        data: {
            message: "show message",
            isTrue: "",
            names: [],
            sex: ""
        }
    })
</script>
```
### 1.7.v-bind指令
v-bind处理标签属性
```
<div id="app">
    <img v-bind:src="imgSrc" width="300px"/>
    <p><a :href="webUrl" target="_blank">bing网站</a></p>
    1.绑定class
    <div v-bind:class="className">1.绑定css样式</div>
    2.绑定css
    <p><label><input type="checkbox" v-model="isOk">改变布尔值</label>&emsp;data={{ isOk }}</p>
    <div :class="{classA:isOk}">2.判断绑定css样式</div>
    <div :class="isOk ? classA : classB">3.三元运算符绑定css样式</div>
    <div :class="[classA, classB]">4.数组绑定css样式</div>
    3.绑定Style
    <div :style="{color: color, fontSize: fontSize}">5.绑定Style</div>
    <div :style="styObj">6.用对象绑定Style</div>
</div>
<style>
    .classA {
        color: red;
    }
    .classB {
        font-size: 150%;
    }
</style>

<script type="text/javascript">
    var app = new Vue({
        el: "#app",
        data: {
            imgSrc: "https://tse1-mm.cn.bing.net/th?id=OET.e3e14ed6b1754b339d5e8ec4713abf71&w=272&h=135&c=7&rs=1&o=5&pid=1.9",
            webUrl: "http://www.bing.com",
            className: "classA",
            isOk: "",
            classA: "classA",
            classB: "classB",
            color: "green",
            fontSize: "20px",
            styObj: {
                color: "gray",
                fontSize: "30px"
            }
        }
    })
</script>
```
### 1.8.其他指令
v-pre：跳过Vue编译，直接输出  
v-cloak：Vue渲染整个DOM完成后才显示，以确保内容完整并样式好看  
v-once：在第一次DOM加载是进行渲染，渲染完成后视为静态内容，以后不再渲染  
```
<div id="app">
    <div v-pre>{{ message }}</div>
    <div v-cloak>渲染完成后，才显示！</div>
    <div v-once>第一次绑定的值:{{ message }}</div>
    <input type="text" v-model="message">
    <p>{{ message }}</p>
</div>

<script type="text/javascript">
    var app = new Vue({
        el: "#app",
        data: {
            message: "Hello Vue World!"
        }
    })
</script>
```
## 2.Vue全局API
Vue的全局API函数用来在构造器外部定义新的功能
### 2.1.Vue.directive自定义指令
#### 1.vue自定义指令中的三个参数
- el：指令绑定的对象，可以用来直接操作DOM
- binding：一个对象，包含指令的很多信息
- vnode：Vue编译生成的虚拟节点
#### 2.自定义指令的生命周期
自定义指令生命周期（钩子函数）：
- bind：只在第一次绑定时执行的操作
- inserted：被绑定元素插入父节点时调用
- update：被绑定元素所在模版更新时进行变化
- componentUpdated：被绑定元素所在模板完成一次更新周期时调用
- unbind：只绑定一次，指令与元素解绑时调用

自定义指令v-colordirective：
```
<script type="text/javascript">
    Vue.directive("colordirective", function (el, binding) {
        console.log(el);
        console.log(binding.name);
        console.log(binding.value);
        console.log(binding.expression);
        el.style = "color: " + binding.value;
    });
</script>
```

```
<div id="app">
    <div v-colordirective="color">{{ num }}</div>
    <p><button @click="add">ADD</button></p>
    <p><button onclick="unbind()">Unbind</button></p>
</div>

<script type="text/javascript">
    function unbind(){
        app.$destroy();
    }

    Vue.directive("colordirective", {
        bind: function (el, binding) {
            console.log("1 - bind");
            el.style = "color: " + binding.value;
        },
        inserted: function () {
            console.log("2 - inserted");
        },
        update: function () {
            console.log("3 - update");
        },
        componentUpdated: function () {
            console.log("4 - componentUpdated");
        },
        unbind: function () {
            console.log("5 - unbind");
        }
    });

    var app = new Vue({
        el: "#app",
        data: {
            num: 10,
            color: "red"
        },
        methods: {
            add: function () {
                this.num++;
            }
        }
    })
</script>
```
### 2.2.Vue.extend构造器的扩展
Vue.extend 返回的是一个“扩展实例构造器”,也就是预设了部分选项的Vue实例构造器。
```
<author></author>
<div id="author"></div>

<script type="text/javascript">
    // 自定义无参数标签
    var authorExtend = Vue.extend({
        template: "<p><a :href='url'>{{ name }}</a></p>",
        data: function () {
            return {
                name: "CJB",
                url: "http://www.baidu.com"
            }
        }
    });
    // 挂载扩展实例构造器
    new authorExtend().$mount("author");
    new authorExtend().$mount("#author");
</script>
```
### 2.3.Vue.set全局操作
Vue.set的作用是在构造器外部操作构造器内部的数据、属性或方法。

由于JavaScript的限制，VUE不能自动检测以下变动的数组：  
1.利用索引直接设置一个项时，Vue不会自动更新；  
2.修改数组长度时，Vue不会自动更新。
```
<div id="app">
    {{ count }}
    <ul>
        <li v-for="item in arrays">{{ item }}</li>
    </ul>
</div>

<p><button onclick="add()">add</button></p>

<script type="text/javascript">
    function add() {
        /* 操作数据 */
        // 1.用Vue.set改变
        Vue.set(outData, "count", 2);
        // 2.用Vue对象的方法添加
        app.count++;
        // 3.直接操作外部数据
        outData.count++;
        /* 操作数组 */
        Vue.set(app.arrays, 1, "dd");
    }

    var outData = {
        count: 1,
        arrays: ["aaa", "bbb", "ccc"]
    };

    var app = new Vue({
        el: "#app",
        data: outData
    });
</script>
```
### 2.4.Vue的生命周期
```
<div id="app">
    {{ count }}
    <p><button @click="add">add</button></p>
</div>
<button onclick="app.$destroy()">销毁</button>

<script type="text/javascript">
    var app = new Vue({
        el: "#app",
        data: {
            count: 1
        },
        methods: {
            add: function () {
                this.count++;
            }
        },
        beforeCreate: function () {
            console.log("1 - beforeCreated 初始化之后");
        },
        created: function () {
            console.log("2 - created 创建完成");
        },
        beforeMount: function () {
            console.log("3 - beforeMount 挂载之前");
        },
        mounted: function () {
            console.log("4 - mounted 被创建");
        },
        beforeUpdate: function () {
            console.log("5 - beforeUpdate 数据更新前");
        },
        updated: function () {
            console.log("6 - updated 被更新后");
        },
        actived: function () {
            console.log("7 - activate");
        },
        deactived: function () {
            console.log("8 - deactivated");
        },
        beforeDestroy: function () {
            console.log("9 - beforeDestroy 销毁之前");
        },
        destroyed: function () {
            console.log("10 - destroyed 销毁之后");
        }
    })
</script>
```
### 2.5.Template
#### 1.直接写在选项里的模版
```
<div id="app">
    {{ message }}
</div>

<script type="text/javascript">
    var app = new Vue({
        el: "#app",
        data: {
            message: "Hello Vue World!"
        },
        template: `<h1 style="color:red">我是选项模板</h1>`
    })
</script>
```
#### 2.写在template标签里面的模版
```
<div id="app">
    {{ message }}
</div>
<template id="demo1">
    <h2 style="color:red">我是template标签模板</h2>
</template>

<script type="text/javascript">
    var app = new Vue({
        el: "#app",
        data: {
            message: "Hello Vue World!"
        },
        template: "#demo1"
    })
</script>
```
#### 3.写在Script标签里面的模版
```
<div id="app">
    {{ message }}
</div>
<script type="x-template" id="demo2">
    <h2 style="color:red">我是script标签模板</h2>
</script>

<script type="text/javascript">
    var app = new Vue({
        el: "#app",
        data: {
            message: "Hello Vue World!"
        },
        template: "#demo2"
    })
</script>
```
### 2.6.Component
Component就是制作自定义标签（在HTML中是不存在的）。  
全局和局部是针对于不同构造器而言。  
组件注册的是一个标签，指令注册的是已有标签的一个属性。
```
<div id="app">
    <component1></component1>
    <component2></component2>
</div>

<script type="text/javascript">
    Vue.component("component1", {
        template: `<div style="color:red;">全局化注册的component1标签</div>`
    })

    var app = new Vue({
        el: "#app",
        components: {
            "component2": {
                template: `<div style="color:green;">局部化注册的component2标签</div>`
            }
        }
    })
</script>
```
### 2.7.Component组件的props属性设置
```
<div id="app">
    <panda v-bind:here="message" from-here="China"></panda>
</div>

<script type="text/javascript">
    var app = new Vue({
        el: "#app",
        data: {
            message: "SiChuan"
        },
        components: {
            "panda": {
                template: `<div style="color:red;">Panda from {{ here }} in {{ fromHere }}.</div>`,
                // 带'-'的属性比如'from-here'必须使用小驼峰命名法'fromHere'
                props: ["here", "fromHere"]
            }
        }
    })
</script>
```
### 2.8.Component父子组件
```
<div id="app">
    <component1></component1>
</div>

<script type="text/javascript">
    var city = {
        template: `<div style="color: red">子组件</div>`
    }
    
    var component1 = {
        template: `<div>Panda from China!<city></city></div>`,
        components: {
            "city": city
        }
    }

    var app = new Vue({
        el: "#app",
        components: {
            "component1": component1
        }
    })
</script>
```
### 2.9.Component加载多组件
```
<div id="app">
    <component v-bind:is="index"></component>
    <button @click="change">changeComponent</button>
</div>

<script type="text/javascript">
    var componentA = {template: `<div style="color: red">This is templateA</div>`}
    var componentB = {template: `<div style="color: green">This is templateB</div>`}
    var componentC = {template: `<div style="color: pink">This is templateC</div>`}

    var app = new Vue({
        el: "#app",
        data: {index: "componentA"},
        components: {
            "componentA": componentA,
            "componentB": componentB,
            "componentC": componentC
        },
        methods: {
            change: function () {
                if (this.index == "componentA") {
                    this.index = "componentB";
                } else if (this.index == "componentB") {
                    this.index = "componentC";
                } else {
                    this.index = "componentA";
                }
            }
        }
    })
</script>
```
## 3.Vue选项
### 3.1.PropsDaata Option 全局扩展的数据传递
1.在全局扩展里加入props进行接受；props: ["count"]  
2.传递时用propsData进行传递；propsData: {count: 12}  
3.用插值的形式写入模版。{{ count }}
```
<header></header>

<script type="text/javascript">
    var extendObj = Vue.extend({
        template: `<p>{{ message }} -- {{ count }}</p>`,
        data: function () {
            return {
                message: "Hello, I am Header!"
            }
        },
        props: ["count"]
    })

    new extendObj({propsData: {count: 12}}).$mount("header");
</script>
```
### 3.2.Computed Option
Computed的作用主要是对原数据进行改造输出（包括格式的编辑、大小写转换、顺序重排，添加符号...）。
```
<div id="app">
    <p>{{ newPrice }}</p>
    <ul>
        <li v-for="item in reverseNews">{{ item }}</li>
    </ul>
</div>

<script type="text/javascript">
    var newLists = [
        {title: "蜥蜴在光照下会去哪里", date: "2018/2/12"},
        {title: "贝克汉姆在白宫的演讲", date: "2018/3/29"},
        {title: "数据结构应用实例", date: "2018/4/23"},
        {title: "《明朝那些事儿》", date: "2018/4/22"},
        {title: "艺术与哲学家的区别", date: "2018/5/24"},
    ];

    var app = new Vue({
        el: "#app",
        data: {
            price: 12,
            newList: newLists
        },
        computed: {
            newPrice: function () {
                return this.price = "￥" + this.price + "元";
            },
            reverseNews: function () {
                return this.newList.reverse();
            }
        }
    })
</script>
```
### 3.3.Method Option
1.传递参数：  
- 在methods方法中声明：add: function(num){}  
- 调用方法时直接传递：<button @click="add(2)"></button>
```
<div id="app">
    <p>{{ score }}</p>
    <!--1.传递参数；2.$event参数；-->
    <p><button @click="add(2, $event)">score+=2</button></p>
    <!--3.native给组件绑定构造器里的原生事件；-->
    <p><btn  @click.native="add(3)"></btn></p>
</div>
<!--4.作用域外部调用构造器里面的方法。-->
<button onclick="app.add(5)">score+=5</button>

<script type="text/javascript">
    var btn = {
        template: `<button>组件ADD</button>`
    }
    var app = new Vue({
        el: "#app",
        data: {
            score: 1
        },
        components:{
          "btn": btn
        },
        methods: {
            add: function (num, event) {
                if (event != null) console.log(event);
                if (num != null) {
                    return this.score += num;
                } else {
                    return this.score++;
                }
            }
        }
    })
</script>
```
### 3.4.Watch Option
```
<div id="app">
    <p>温度：{{ temperature }}</p>
    <p>穿衣：{{ cloth }}</p>
    <p>
        <button @click="increase()">升温</button>
        <button @click="reduce()">降温</button>
    </p>
</div>

<script type="text/javascript">
    var clothes = ["羽绒服", "夹克", "短袖"];

    var app = new Vue({
        el: "#app",
        data: {
            temperature: 12,
            cloth: "夹克"
        },
        methods: {
            increase: function () {
                return this.temperature += 5;
            },
            reduce: function () {
                return this.temperature -= 4;
            }
        },
        watch: {
            temperature: function (newVal, oldVal) {
                if (newVal >= 26) {
                    this.cloth = clothes[2];
                } else if (newVal <= 0) {
                    this.cloth = clothes[0];
                } else {
                    this.cloth = clothes[1];
                }
            }
        }
    });

    app.$watch("temperature", function (newVal, oldVal) {
        newVal >= 26 ? this.cloth = clothes[2] : (newVal <= 0 ? this.cloth = clothes[0] : this.cloth = clothes[1]);
    });
</script>
```
### 3.5.Mixins
1.写好构造器后，需要增加方法或者临时的活动时使用的方法，使用混入会减少源代码的污染；  
2.公用方法，用混入的方法可减少代码量，实现代码重用。  
3.执行顺序：全局混入方法->局部混入方法->原生方法
```
<div id="app">
    <p>{{ score }}</p>
    <p><button @click="add">Add score</button></p>
</div>

<script type="text/javascript">
    var addLog = {
        updated: function () {
            console.log("执行混入方法,score值改变为" + this.score);
        }
    }

    Vue.mixin({
        updated: function () {
            console.log("执行全局混入的updated方法");
        }
    })

    var app = new Vue({
        el: "#app",
        data: {
            score: 12
        },
        methods: {
            add: function () {
                this.score++;
            }
        },
        updated: function () {
            console.log("执行原生的updated方法");
        },
        mixins: [addLog]
    })
</script>
```
### 3.6.Extends
```
<div id="app">
    <p>${ message }</p>
    <p><button @click="add">add</button></p>
</div>

<script type="text/javascript">
    var extendObj = {
        methods: {
            add: function () {
                console.log("add");
            }
        },
        updated: function () {
            console.log("扩展updated方法");
        }
    }

    var app = new Vue({
        el: "#app",
        data: {
            message: 11
        },
        methods: {
            add: function () {
                return this.message++;
            }
        },
        updated: function () {
            console.log("原生updated方法");
        },
        extends: extendObj,
        delimiters: ["${", "}"]
    })
</script>
```
## 4.实例和内置组件
### 4.1.实例属性
```
<script type="text/javascript" src="../../assets/js/jquery-3.3.1.min.js"></script>

<script type="text/javascript">
    var app = new Vue({
        el: "#app",
        data: {
            message: "Hello Vue World!"
        },
        mounted:function () {
            // 1.在Vue中使用jJQuery方法
            $("#app").html("我是jQuery!");
        },
        methods:{
            add: function () {
                console.log("调用Add方法");
            }
        }
    })

    // 2.实例调用自定义方法
    app.add();
</script>
```
### 4.2.实例方法
$mount()/$destroy()/$forceUpdated()/$nextTick()
```
<div id="app"></div>
<p>
    <button onclick="destroy()">destroy</button>
    <button onclick="reload()">reload</button>
    <button onclick="tick()">tick</button>
</p>

<script type="text/javascript">
    var extendObj = Vue.extend({
        template: `<div>{{ score }}</div>`,
        data: function () {
            return {
                score: 12
            }
        },
        mounted: function () {
            console.log("mounted");
        },
        destroyed: function () {
            console.log("destroyed");
        },
        updated: function () {
            console.log("updated");
        }
    })

    var vm = new extendObj().$mount("#app");

    function destroy() {
        vm.$destroy();
    }

    function reload() {
        vm.$forceUpdate();
    }

    function tick() {
        vm.score = "update message info";
        vm.$nextTick(function () {
            console.log("message更新完成后被调用");
        })
    }
</script>
```
### 4.3.实例事件
$on/$once/$emit/$off
```
<div id="app">
    {{ score }}
</div>
<p><button onclick="reduce()">reduce</button></p>
<p><button onclick="reduceOnce()">reduceOnce</button></p>
<p><button onclick="off()">OFF</button></p>
<script type="text/javascript">
    var app = new Vue({
        el: "#app",
        data: {
            score: 0
        },
        methods: {
            add: function () {
                this.score++;
            }
        }
    })

    app.$on("reduce", function () {
        this.score--;
        console.log("执行了reduce()方法");
    })

    app.$once("reduceOnce", function () {
        this.score--;
        console.log("只能执行一次");
    })

    function reduce() {
        app.$emit("reduce");
    }

    function reduceOnce() {
        app.$emit("reduceOnce");
    }

    function off() {
        app.$off("reduce");
        console.log("关闭reduce()方法");
    }
</script>
```
### 4.4.内置组件-slot
```
<div id="app">
    <temp>
        <span slot="url">{{ dataObj.url }}</span>
        <span slot="name">{{ dataObj.name }}</span>
        <span slot="favorite">跑步</span>
    </temp>
</div>
<template id="temp">
    <div>
        <p>网址：<slot name="url"></slot></p>
        <p>姓名：<slot name="name"></slot></p>
        <p>喜好：<slot name="favorite"></slot></p>
    </div>
</template>

<script type="text/javascript">
    var temp = {
        template: "#temp"
    }

    var app = new Vue({
        el: "#app",
        data: {
            dataObj: {
                url: "http://jspang.com",
                name: "大卫",
                favorite: "running"
            }
        },
        components: {
            "temp": temp
        }
    })
</script>
```