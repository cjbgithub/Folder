# SpringBoot

springboot是J2EE的一站式解决方案



1. 开发环境

- jdk
- maven
- idea
- springboot

2. 环境配置

- Maven：idea路径，settingxml->jdk+path
- IDEA：properties文件编码：File Encoding

3. 注解

```java

@EnableAutoConfiguration  自动配置
@AutoConfigurationPackage  自动配置包
@Import(EnableAutoConfigurationImportSelector.class)  导入组件
@
```

4. 配置文件

``` java
*application.properties/*application.yml
@Component + @ConfigurationProperties
1. @ConfigurationProperties(prefix = "prefix") : 将属性文件中prefix下面的所有属性与类中属性一一绑定
2. 使用@ConfigurationProperties功能的必须是容器中的组件

配置文件处理器：进行提示 - dependency:spring-boot-configration-processor

@ConfigurationPeoperties适合较多属性
@Value适合较少属性
```

YAML语法：

- 同级属性任意空格对齐；键值对一个空格分割
- 大小写敏感；双引号不转义、单引号转义
- 数组（List、Set）与 对象（Map 属性和值 键值对） 分行内写法和行外写法





# Project Demo

springboot+mybatis+redis(pageHelper+Mybatis Generator)

> Dependence

Web+Mybatis+JDBC+MySQL/Oracle

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.2.5.RELEASE</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.wondersgroup.test</groupId>
    <artifactId>wssuap-demo</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>wssuap-demo</name>
    <description>Demo project for Wssuap</description>

    <properties>
        <java.version>1.8</java.version>
    </properties>
    
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.mybatis.spring.boot</groupId>
            <artifactId>mybatis-spring-boot-starter</artifactId>
            <version>2.1.1</version>
        </dependency>
        <dependency>
            <groupId>com.oracle.ojdbc</groupId>
            <artifactId>ojdbc8</artifactId>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
            <exclusions>
                <exclusion>
                    <groupId>org.junit.vintage</groupId>
                    <artifactId>junit-vintage-engine</artifactId>
                </exclusion>
            </exclusions>
        </dependency>
        <dependency>
            <groupId>com.github.pagehelper</groupId>
            <artifactId>pagehelper-spring-boot-starter</artifactId>
            <version>1.2.13</version>
        </dependency>
    </dependencies>
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>

```













































