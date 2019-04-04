修改Windows默认安装路径：

regedit -> HKEY_LOCAL_MACHINE->SOFTWARE->Microsoft->Windows->CurrentVersion -> 修改ProgramFilesDir数值为D:\Program Files\Software



计算机保存信息的戒指：

+ 内部存储器
    - 寄存器
    - 高速缓冲存储器（Cache）
    - 主存储器
+ 外部存储器
    + 磁盘
        - 软盘（A、B）
        - 硬盘（C...）
            + 固态硬盘SSD
            + 机械硬盘HDD
    + 光盘
    + U盘

硬盘分区是对硬盘的一种格式化，然后才能用硬盘保存信息
+ 主分区（活动分区）C
+ 扩展分区 -> 逻辑分区

机械硬盘是由一个或多个铝制或玻璃纸的碟片组成，呈圆形  
机械硬盘读取数据是CAV(Constant Angular Velocity)，恒定角速度  
读取速度相同时间内读取外圈的数据比内圈的数据多，即外圈读取速度快  
正常分区一般C盘位于外圈，读取速度较快

在CPU在读取内存，内存不够时会根据内存情况调用虚拟内存（一般在C盘）