# Winows Commands

有时候在Windows中开启一些软件不免会出现软件卡崩的情况，尤其是有些软件在出现故障的时候不自动关闭而是一直弹窗，像个病毒一样，这时候我们不得不去使用Windows的Task Manager找到该应用程序并将其关掉，但是在Task Manager中查找非常耗时耗眼力，下面的Windows常用命令行就为解决这一需求而撰写。

<br>

1. List out the running process:
```bash
Tasklist
Tasklist /fo table
```

2. Find or grep the running task with its name: 
```bash
Taskkill | FIND "script.php"
```

3. Kill the task with its name:
```bash
Taskkill /IM "process name" /F
```

4. Kill a process by its PID:
```bash
Taskkill /F /PID pid_number
```


<br>

<br>

<br>

作者：艾孜尔江
