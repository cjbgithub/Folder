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















