## Servlet
CGI（Common Gateway Interface，公共网关接口）  
Servlet(Server Applet),全称Java Servlet，服务端程序。只要用于交互式地浏览和修改数据。

从原理上讲，Servlet可以响应任何类型的请求，但绝大多数情况下Servlet只用来扩展基于HTTP协议的Web服务器。

> 生命周期

1. 客户端请求Servlet
2. 加载Servlet类到内存
3. 实例化并调用init()方法初始化该Servlet
4. service()（ doGet()、doPost()、doHead()、doPut()、doTrace()、doDelete()、doOptions() ）
5. destroy()

> Server通常提供一个管理的选项，用于在Server启动时强制装载和初始化特定的Servlet

1. 第一个客户端请求到达Server
2. Server调用Servlet的init()方法，只初始化一次（只有一个对象）
   + web.xml <servlet> <load-on-startup> type:Integer 值越小优先级越高
3. 一个客户端请求到达Server
4. Server创建一个请求对象，用来处理客户端请求
5. Server创建一个响应对象，用来响应客户端请求
6. Server激活Servlet的service()方法或其他方法，传递请求和响应对象作为参数
7. service()方法获取请求对象信息，处理请求，访问其他资源获取需要的信息
8. service()方法是使用响应对象的方法，将响应传回Server，最终到达客户端
9. 重复执行 3-8 的步骤
10.Server关闭，调用Servlet的destroy()方法

Servlet没有main()方法，由容器调用，有生命周期：init()和destroy()，运行在服务器端

## JSP
JSP(Java Servlet Pages)

项目分层
1. 数据层：data layer
2. 业务层：business layer
3. 表现层：presentation layer

Servlet输出HTML是一句一句的输出，而JSP不用  
Servlet针对于business layer功能强大，对于presentation layer很不方便  
所有的数据计算、数据分析、数据库连接处理属于business layer，存放在Java Beans中
JSP主要为了方便写presentation layer而设计，只存放输出HEML网页的部分，通过调用Java Beans实现两层的整合  

采用组件（JSP+BEANS）可解决单纯使用JSP时的缺点：
1.大量用户点击时效率很低，容易达到SCRIPT的功能上限
2.business layer和presentation layer混在一起，修改不方便，代码不能复用

## 规范
1. 简化开发
2. 便于部署
3. 支持Web2.0原则

Servlet3.0：
Pluggability可插入性
Asynchronous Processing 异步处理 AJAX

常见Servlet容器（提供Servlet功能的服务器）：Tomcat、Jetty、JBoss、Weblogic Server...





































