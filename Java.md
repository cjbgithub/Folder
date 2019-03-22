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

> 1. 基于字节流读写（byte）

```java
public static void main(String[] args) {
    // 1. 构建指定文件
    File file = new File("D:\\hello.txt");

    // 2. 根据文件创建文件的输出流，第二个参数表示追加内容
    try (FileOutputStream output = new FileOutputStream(file, true)) {
        // 3. 把内容转换成字符数组
        byte[] data = "add content".getBytes();
        // 4. 向文件写入内容
        output.write(data);
        // 5. 关闭输入流
    } catch (Exception e) {
        e.printStackTrace();
    }

    // 2. 根据文件创建文件的输入流
    try (FileInputStream input = new FileInputStream(file)) {
        // 3. 创建字符数组
        byte[] data = new byte[1024];
        // 4. 读取内容，放到字符数组
        input.read(data);
        System.out.println("文件内容：" + new String(data));
        // 5. 关闭输入流
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

> 2. 基于字符流读写（char）

```java
public static void main(String[] args) {
    // 1. 构建指定文件
    File file = new File("D:\\hello.txt");

    // 2. 根据文件创建文件的输出流，第二个参数表示追加内容
    try (Writer writer = new FileWriter(file, true)) {
        // 3. 把内容转换成字符数组
        char[] data = "add message".toCharArray();
        // 4. 向文件写入内容
        writer.write(data); // writer.write("messages");
        // 5. 关闭输入流
    } catch (Exception e) {
        e.printStackTrace();
    }

    // 2. 根据文件创建文件的输入流
    try (Reader reader = new FileReader(file)) {
        // 3. 创建字符数组
        char[] data = new char[1024];
        // 4. 读取内容，放到字符数组
        reader.read(data);
        System.out.println("文件内容：" + new String(data));
        // 5. 关闭输入流
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

## 3. 随机读取文件

RandomAccessFile

```java
public static void main(String[] args) {
    File file = new File("D:\\hello.txt");
    /**
    * model各个参数详解
    * r    代表以只读方式打开指定文件
    * rw   以读写方式打开指定文件
    * rws  读写方式打开，并对内容或元数据都同步写入底层存储设备
    * rwd  读写方式打开，对文件内容的更新同步更新至底层存储设备
    */
    try (RandomAccessFile raf = new RandomAccessFile(file, "r")) {
        // 获取文件初始位置，初始位置是0
        System.out.println("指针的初始位置：" + raf.getFilePointer());

        // 移动文件指针位置
        raf.seek(0);
        byte[] buff = new byte[1024];

        // 用于保存实际数据的字节数
        int hasRead = 0;

        // 循环读取
        while ((hasRead = raf.read(buff)) > 0) {
            // 打印读取的内容，并将字节转为字符串输入
            System.out.println(new String(buff,0,hasRead));
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

## 4. IO 复制文件

```java
public static void main(String[] args) {
    // 1. 构建源文件和目标文件
    File file = new File("D:\\hello.txt");
    File fileCopy = new File("D:\\hello-copy.txt");

    Reader reader = null;
    Writer writer = null;
    try {
        if (!fileCopy.exists()) {
            fileCopy.createNewFile();
        }
        // 2. 源文件创建输入流，目标文件创建输出流，追加内容
        reader = new FileReader(file);
        writer = new FileWriter(fileCopy, true);

        // 3. 创建字符数组
        char[] data = new char[1024];
        // 4. 循环读取源文件内容，写入目标文件
        int len = 0;
        while ((len = reader.read(data)) != -1) {
            System.out.println(data);
            writer.write(data, 0, len);
        }
    } catch (Exception e) {
        e.printStackTrace();
    } finally {
        try {
            // 5. 关闭源文件输入流，目标文件输出流
            if (reader != null) reader.close();
            if (writer != null) writer.close();
        } catch (IOException e1) {
            e1.printStackTrace();
        }
    }
}
```

## 5. IO 文件信息

```java
public static void main(String[] args) throws Exception {
    Path path = Paths.get("D:\\hello.txt");

    BasicFileAttributeView basecView = 
        Files.getFileAttributeView(path, BasicFileAttributeView.class);

    BasicFileAttributes ba = basecView.readAttributes();
    System.out.println("创建时间：" + new Date(ba.creationTime().toMillis()));
    System.out.println("最后访问时间：" + new Date(ba.lastAccessTime().toMillis()));
    System.out.println("最后修改时间：" + new Date(ba.lastModifiedTime().toMillis()));
    System.out.println("文件大小：" + ba.size());

    FileOwnerAttributeView ownerView = 
        Files.getFileAttributeView(path, FileOwnerAttributeView.class);
    System.out.println("文件所有者：" + ownerView.getOwner());
}
```

## 6. Buffered流

带有缓冲区的流读写时间加快，读写文件速度比字节流快，并且可以对源数据的某一部分反复读写

使用了包装者模式，构造此类对象时需要一个基本流对象：

```java
BufferedInputStream bin = new BufferedInputStream( new FileInputStream("XX"))
```





























