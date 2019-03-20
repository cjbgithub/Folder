spring @Autowired @Resource
相同点：
1. 装配bean，都可以写在字段上，或者方法上
2. 

不同点：
@Autowired
1. 属于Spring
2. 默认按类型装配，默认情况下必须要求依赖对象必须存在
3. null值：@Autowired(required=false) 



@Resource
1. @Resource为JSR-250标准的注释，属于J2EE
2. 默认安装名称进行装配，当找不到与名称匹配的bean时才按照类型进行装配


