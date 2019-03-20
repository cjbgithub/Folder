# Java线程

## 应用程序&进程
Java中，一个应用程序对应一个JVM实例（JVM进程），名字默认java.exe/javaw.exe
Java采用单线程编程模式，默认只创建一个线程，通常称为主线程
在JVM实例创建时还有垃圾回收线程等其他线程

## Java创建线程
1. 继承Thread类
```java
# 1. 重写run()方法，在run()方法中定义执行的任务
class MyThread extends Thread {
    private String name;
    
    public MyThread(String name) {
        this.name = name;
    }

    @Override
    public void run() {
        System.out.println("Name：" + name + "\t子线程ID：" + Thread.currentThread().getId());
    }
}

# 2. 创建线程，调用**start()**方法启动线程
public class Test {
    public static void main(String[] args)  {
        System.out.println("主线程ID：" + Thread.currentThread().getId());
        MyThread thread1 = new MyThread("thread1");
        thread1.**start**();
        MyThread thread2 = new MyThread("thread2");
        thread2.**run**();
    }
}

# 3. 输出结果
[out]主线程ID：1
[out]Name：thread2	子线程ID：1
[out]Name：thread1	子线程ID：11
```
上述结果表明
* 1.继承Thread类再调用run()方法等同于调用普通方法，在主线程运行
* 2.创建线程不会阻塞主线程的后续运行：调用普通方法run()先执行，然后调用start()方法创建线程

2. 实现Runnable接口
```java
# 1. 实现Runnable接口
class MyRunnable implements Runnable {
    public MyRunnable() {}

    @Override
    public void run() {
        System.out.println("子线程ID：" + Thread.currentThread().getId());
    }
}

# 2. 创建线程
public class Test {
    public static void main(String[] args) {
        System.out.println("主线程ID：" + Thread.currentThread().getId());
        MyRunnable runnable = new MyRunnable();
        Thread thread = new Thread(**runnable**);
        thread.start();
    }
}
```

> 总结：1.覆写run()方法；2.创建线程；
1. extends Thread -> new Thread() -> start()
2. implements Runnable -> new Thread(runnable) -> start()

## Java创建进程
1. ProcessBuilder.start()
```java
import java.io.IOException;
import java.util.Scanner;

public class Test {
    public static void main(String[] args) throws IOException {
        ProcessBuilder pb = new ProcessBuilder("cmd", "/c", "ipconfig/all");
        Process process = pb.start();
        Scanner scanner = new Scanner(process.getInputStream());

        while (scanner.hasNextLine()) {
            System.out.println(scanner.nextLine());
        }
        scanner.close();
    }
}
```

2. Runtime.exec()
```java
import java.io.IOException;
import java.util.Scanner;

public class Test {
    public static void main(String[] args) throws IOException {
        String cmd = "cmd " + "/c " + "ipconfig/all";
        Process process = Runtime.getRuntime().exec(cmd);
        Scanner scanner = new Scanner(process.getInputStream());

        while (scanner.hasNextLine()) {
            System.out.println(scanner.nextLine());
        }
        scanner.close();
    }
}
```

> 底层调用：ProcessBuilder.start()



# 2. Java IO

## 1. Java IO 分类

Java IO 读写文件的IO流分为两大类：

> 1. 基于字节流读写基类InputStream和OutputStream，读写二进制文件

- FileInputStream extends InputStream
- FileOutputStream extends OutputStream

> 2. 基于字符流读写基类Reader和Writer，读写文本文件

* FileReader extends InputStreamReader (extends Reader)
* FileWriter extends OutputStreamWriter (extends Writer)

## 2. Java IO 读写

> 1. 基于字节流读写

```java

```







> 2. 基于字符流读写





## 3. 随机读取文件

RandomAccessFile











