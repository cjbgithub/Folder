# 1. SFLI

## 1. Servlet

Servlet用于交互式地浏览和修改数据，生成动态WEB内容

1. 客户端发送请求至服务端
2. 服务器将请求信息发送至Servlet
3. Servlet生成动态响应内容并将其传给服务器
4. 服务器将响应内容返回给客户端

+ servlet：一般继承HttpServlet
+ 一般的，通用Servlet由javax.servlet.GenericServlet实现Servlet接口
+ javax.servlet.http.HttpServlet实现了专门用于响应HTTP请求的Servlet，处理get/post
+ web.xml配置servlet时如果加上load-on-start为1时，Web应用启动时候加载Servlet
+ Java 服务器页面 JSP 是 HttpServlet 的扩展，本质是Servlet
+ JSP 在首次被访问时被应用服务器转换为Servlet，在以后运行中容器直接调用Servlet

```java
// 0或者大于0时，表示容器在应用启动时就加载这个servlet
// 正数的值越小，启动该servlet的优先级越高
// 一个负数时或者没有指定时，则指示容器在该servlet被选择时才加载
<load-onstartup>1</load-on-startup>
```



## 2. Filter

​	Filter对用户请求进行加工预处理（过滤字符编码、判断权限重定向等），接着将请求交给Servlet进行处理并生成响应，最后Filter再对服务器响应进行后处理

+ Filter是实现了javax.servle.Filter接口的服务端程序
+ 在HttpServletRequest到达Servlet之前，拦截客户的HttpServletRequest
+ 根据需要检查HttpServletRequest，也可以修改HttpServletRequest头和数据
+ chain.doFilter()放行请求，执行前处理用户请求，执行后处理服务器响应
+ 在HttpServletResponse到达客户端之前，拦截HttpServletResponse
+ 根据需要检查HttpServletResponse，也可以修改HttpServletResponse头和数据
+ 多个匹配的Filter按照web.xml中配置的顺序来执行

种类：用户授权、日志、解码、改变XML内容、拦截多个请求或响应

**当Filter被调用，并且进入了Struts2的DispatcherFilter中后，Struts2会按照在Action中配置的Interceptor Stack中的Interceptor的顺序，来调用Interceptor**

## 3. Listener

​	通过listener可以监听web服务器中某一个执行动作，并根据其要求做出相应的响应，是在application，session，request创建消亡或者往其中添加修改删除属性时自动执行代码的功能组件。

​	spring总监听器在服务器启动时实例化bean对象

​	hibernate的session监听器监听session的活动和生命周期，负责创建，关闭session

+ 与servletContext有关的listner接口
  + ServletContextListener
  + ServletContextAttributeListener
+ 与HttpSession有关的Listner接口
  + HttpSessionListner
  + HttpSessionAttributeListener
  + HttpSessionBindingListener
  + HttpSessionActivationListener
+ 与ServletRequest有关的Listener接口
  + ServletRequestListner
  + ServletRequestAttributeListener

​	在application，session，request创建消亡或者往其中添加修改删除属性时自动执行代码的功能组件

## 4. Interceptor

​	面向切面编程，动态代理是拦截器的简单实现，基于JAVA的反射机制

​	在service或者一个方法执行前调用一个方法，或在其执行后调用一个方法

# 2. 加载

1. servlet一般继承HttpServlet，容器在服务器启动或接受到请求时加载
2. filter实现javax.Servlet.Filter接口，服务器启动时加载并初始化实例
3. listener实现javax.servlet.ServletContextListener 接口，服务器启动时加载
4. web.xml 的加载顺序是：context- param -> listener -> filter -> servlet 

+ servlet在业务处理之前进行控制
+ filter是线性的，可保持流程按照原来的方式进行或者主导流程
+ servlet，filter针对url，listener针对对象的操作，如session的创建、修改
+ interceptor在struts.xml中配置，针对action,当页面提交action时，进行过滤操作
+ 过滤器和拦截器的区别与联系
  + 拦截器是基于java反射机制的，而过滤器是基于函数回调的
  + 过滤器依赖与servlet容器，而拦截器不依赖与servlet容器
  + 拦截器只能对Action请求起作用，而过滤器则可以对几乎所有请求起作用
  + 拦截器可以访问Action上下文、值栈里的对象，而过滤器不能
  + 在Action生命周期中，拦截器可多次调用，而过滤器只能在容器初始化时被调用一次



# 3. 运行原理

Filter控制器、表单映射POJO、验证逻辑写在Action中、OGNL

添加Jar包依赖+配置web.xml+配置struts.xml（将多个Action封装为package）+DTD约束

> 运行流程

1. 请求发送给StrutsPrepareAndExecuteFilter
2. StrutsPrepareAndExecuteFilter询问ActionMapper：该请求是否是一个Struts2请求
3. 若是Struts2请求，则StrutsPrepareAndExecuteFilter把请求的处理交给ActionProxy
4. ActionProxy通过Configuration Mapper询问框架配置文件，确定需要调用的Action类及Action方法
5. ActionProxy创建一个ActionInvocation的实例并进行初始化
6. ActionInvocation实例在调用Action的过程前后，涉及到相关拦截器的调用
7. Action执行完毕，ActionInvocation负责根据struts.xml中的配置找到对应的返回结果。调用结果的execute方法，渲染结果（可使用Struts2框架中的标签）。
8. 执行各个拦截器invocation.invoke()之后的代码
9. 把结果发送到客户端

# 4. 配置文件

> sturts-default.xml

```xml
<struts>
	// package:struts把不同的Action组织成不同的包
    // name:每个package有一个标识，可被其他package引用
    // namespace:默认为"/"，自定义值需要加到相关URI字符串中
	<package name="struts-default" abstract="true">
		<result-types>
            <result-type name="" class=""/>
        </result-types>
        <interceptors>
        	<interceptor name=" " class=" "/>
        	<interceptor-stack name="basicStack">
                <interceptor-ref name=" "/>
            </interceptor-stack>
        </interceptors>
        <default-interceptor-ref name="defaultStack"/>
        <default-class-ref class="com.opensymphony.xwork2.ActionSupport" />
    </package>
</struts>
```

> // struts.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE struts PUBLIC
    "-//Apache Software Foundation//DTD Struts Configuration 2.0//EN"    
    "http://struts.apache.org/dtds/struts-2.0.dtd">
<struts>
    // extends:对sturts-default.xml文件中定义的struts-default包进行扩展
	<package name=" " abstract="true" extends=" ">
		<interceptors>
			<interceptor name=" " class=" "/>
			<interceptor-stack name=" ">
				<interceptor-ref name=" "/>
				<interceptor-ref name=" ">
					<param name=" ">...</param>
				</interceptor-ref>
			</interceptor-stack>
		</interceptors>
		<default-interceptor-ref name="wssip-defaultStack"/>
		<global-results>
			<result name="login" type="redirect">/login.jsp</result>
		</global-results>
		<global-exception-mappings>
			<exception-mapping result=" " exception=" " />
		</global-exception-mappings>
	</package>
	<!-- 一体化平台公用Action定义 -->
	<include file="com/wondersgroup/yq/yqAction.xml" />
	<constant name="struts.action.extension" value="xhtml,,json"/>
</struts>
```

> yqAction.xml

```xml
<struts>
	<package name="/yq" extends="shyb-default" namespace="/yq">
        // action元素嵌套在package内部，表示一个struts请求
        // 每个Action都有一个name属性，该属性与用户请求servletPath之间存在着一一对应关系
        // class是可选属性，默认为com.opensymphony.xwork2.ActionSupport,Method默认值为execute
		<action name="doYqPlaceOrderIndex" class="linkAction">
            // result元素的name属性建立result与Action返回值之间的映射，默认值是success
            // type指定结果类型，必须是在当前包或者是当前包父包里注册过的结果类型，默认值dispathcer
			<result name="success" type="dispatcher">xxx.jsp</result>
		</action>
		<action name="doYqPlaceOrderSave" class="yqPlaceOrderAction" />
	</package>
</struts>

// type="dispatcher"默认结果类型，其默认参数为location
// dispatcher将控制权转发给指定资源，或用redirect重定向到外部资源
-----
<result name="success">xxx.jsp</result>
等同于
<result name="success">
    <param name="location">xxx.jsp</param>
</result>
-----
// redirect:location/parse
<result name="success" type="redirect">
    <param name="location">/xx.jsp?name=${name}</param>
</result>
// redirectAction:actionName/namespace
<result name="success" type="redirectAction">
    <param name="actionName">Login</param>
    <param name="namespace">/</param>
</result>
// chain:actionName/namespace/method前一个Action将控制权转发给后一个Action，状态依然保留
<result name="success" type="redirectAction">
    <param name="actionName">Login</param>
    <param name="namespace">/</param>
</result>
```

> type类型

```xml
<result-types>
    <result-type name="chain" class="...ActionChainResult"/>
    <result-type name="dispatcher" class="...ServletDispatcherResult" default="true"/>
    <result-type name="freemarker" class="...FreemarkerResult"/>
    <result-type name="httpheader" class="...HttpHeaderResult"/>
    <result-type name="redirect" class="...ServletRedirectResult"/>
    <result-type name="redirectAction" class="...ServletActionRedirectResult"/>
    <result-type name="stream" class="...StreamResult"/>
    <result-type name="velocity" class="...VelocityResult"/>
    <result-type name="xslt" class="...XSLTResult"/>
    <result-type name="plainText" class="...PlainTextResult" />
    <result-type name="postback" class="...PostbackResult" />
</result-types>
```

# 5. ActionContext

> 访问Web资源

- 与Servlet API解耦
  - com.opensymphony.xwork2.ActionContext
  - org.apache.struts2.interceptor.ApplicationAware
  - org.apache.struts2.interceptor.RequestAware
  - org.apache.struts2.interceptor.SessionAware
- 与Servlet API耦合
  - org.apache.struts2.ServletActionContext
  - 实现XxxAware接口

Struts2将HttpServletRequest、HttpSession、ServletContext封装成Map对象保存

ActionContext是Action执行的上下文对象，其中保存了Action执行所需要的所有对象

+ public Map getSession()             获取HttpSession的Map对象
+ public Map getApplication()      获取ServletContext的Map对象
+ public Map getParameters()      获取参数对象Map对象

+ pubic Object get(Object key)      将request作为参数传递，获取HttpServletRequest的Map对象

> 通配符映射

```xml
// 1. 匹配Book_add.action/Author_add.action...
<package name="struts-app3" namespace="/app3" extends="shyb-default">
    <action name="*_add" class="com.admin.app.Book" method="add">
        <result>/WEB-INF/jsp/book.jsp</result>
    </action>
</package>
// 1. {0}匹配整个URI、{1}匹配第一个子串、{2}匹配第二个子串
<package name="struts-app3" namespace="/app3" extends="shyb-default">
    <action name="Book_add" class="com.admin.app.Book" method="add">
        <result>/WEB-INF/jsp/Book.jsp</result>
    </action>
    <action name="Author_add" class="com.admin.app.Author" method="add">
        <result>/WEB-INF/jsp/Author.jsp</result>
    </action>
    --等价于--
    <action name="*_add" class="com.admin.app.{1}" method="add">
        <result>/WEB-INF/jsp/{1}.jsp</result>
    </action>
-------------
    <action name="Book_add" class="com.admin.app.Book" method="add">
        <result>/WEB-INF/jsp/Book.jsp</result>
    </action>
    <action name="Aothor_delete" class="com.admin.app.Aothor" method="delete">
        <result>/WEB-INF/jsp/Aothor.jsp</result>
    </action>
    --等价于--
    <action name="*_*" class="com.admin.app.{1}" method="{2}">
        <result>/WEB-INF/jsp/{1}.jsp</result>
    </action>
</package>
```

# 6. OGNL

JSP页面可以利用OGNL(Object-Graph Navigation Language：对象-图导航语言)访问到ValueStack中的对象属性，默认访问ValueStack.ObjectStack的内容，加上前缀字符 # 可以访问ValueStack.ContextMap中的值

Struts2将包装HttpServletRequest对象后的org.apache.struts2.dispatcher.StrutsRequestWrapper对象传到页面上，而这个类重写了getAttribute()方法，因此在页面可以访问ValueStack中对象的属性



ParamsPrepareParamsStack拦截器栈

1. params拦截器首先给action中的相关参数赋值，如id
2. prepare拦截器执行prepare方法，prepare方法中会根据参数，如id，去调用业务逻辑，设置model对象
3. modelDriven拦截器将prepare中创建的model对象压入ValueStack
4. params拦截器再将参数赋值给model对象
5. action的业务逻辑执行



































