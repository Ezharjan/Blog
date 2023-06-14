
1. 清除登陆系统成功的记录

```bash
echo > /var/log/wtmp //此文件默认打开时乱码，可查到ip等信息

last //此时即查不到用户登录信息
```


2. 清除登陆系统失败的记录

```bash
echo > /var/log/btmp //此文件默认打开时乱码，可查到登陆失败信息

lastb //查不到登陆失败信息
```



 

3. 清除历史执行命令

```bash
history -c //清空历史执行命令

echo > ./.bash_history //或清空用户目录下的这个文件即可
```




4. 导入空历史记录

```
vi /root/history //新建记录文件

history -c //清除记录 

history -r /root/history.txt //导入记录 

history //查询导入结果
```

_使用举例如下_
```bash
vi /root/history

history -c 

history -r /root/history.txt 

history 

echo > /var/log/wtmp  

last

echo > /var/log/btmp

lastb 

history -c 

echo > ./.bash_history

history

echo > /var/log/wtmp

last

echo > /var/log/btmp

history -c

echo > ./.bash_history 

vi /root/history

history -c

history -r /root/history.txt

history -cw
```
 

 

 

 

5. 查询linux服务器有哪些IP在连接

```bash
netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n
```

 

6. 敲一下w，即可看到当前在线人数
```bash
w
```

7. 查看磁盘剩余空间

```bash
df -hl
```

7. 查看每个根路径的分区大小

```bash
df -h
```
8. 返回该目录的大小

```bash
du -sh [目录名]
```

9. 返回该文件夹总M数
```bash
du -sm [文件夹]
```

10. 查看指定文件夹下的所有文件大小（包含子文件夹）
```bash
du -h [目录名]
```

11. 将某个命令输出的信息写入文件

```bash
ls > ./lsInfo.txt
```

12. 查看某个端口的进程ID：
```bash
netstat -nap | grep 端口号
```

13. 杀死指定的进程ID：
```bash
kill -9 进程ID
```

14. vim show line number:
```bash
set nu #show
set nonu #hide
vim ~/.vimrc ##add 'set nu' to this file to show the line number permanently
```


15. Use nohup to run the commands in background:
```bash
nohup (your commands here) & echo "your remark here" > nohup.out &
cat nohup.out #view the process of background running command
```


16. Create soft link to current folder:
```bash
ln -s /absolute/path/to/file.txt shortcut_name
```

17. SSH add public key into the server to avoid entering password everytime:
- 找到本机的id_ras.pub文件
- 将id_ras.pub的内容复制到服务器中
- 服务器中需要被改动的文件是 ~/.ssh/authorized_keys
- vi ~/.ssh/authorized_keys



18. 使用slrum集群运行指令在GPU上：
```bash
srun -p gpu_batch --gres=gpu:ID_OF_GPU python xxx
```

19. See the size of the folder:
```bash
du -sh /path/to/folder
```


20. 查看正在执行`main.py`的后台进程（排除grep自身被查出的情况）：
```bash
ps -aux|grep main.py| grep -v grep
```

21. 获取正在执行的`main.py`的后台进程（排除grep自身被查出的情况）的进程号/进程ID：
```bash
ps -aux|grep main.py| grep -v grep | awk '{print $2}'
```


<br>
<br>
<br>
<br>
<br>
<br>

作者：艾孜尔江



# Slurm Commands

1. 显示每个节点上可用的GPU数量、当前使用的GPU数量、节点状态以及其他相关信息:
```bash
sinfo -o "%10N %10G %10c %10D %10T %20F" --Node | grep gpu

##节点状态
#alloc	    idle	   mix	        down      drain
#节点在用	节点可用	部分占用	节点下线	节点故障
```

2. 详细地了解每个作业占用的GPU，可以使用以下命令，该命令将显示每个作业的ID、作业名称、用户名、状态、内存使用量、GPU数量以及其他相关信息。：
```bash
squeue -o "%.7i %.9P %.8j %.8u %.2t %.10M %.6D %R"

##作业状态
#R	        PD	        CG	        CD
#正在运行	正在排队	即将完成	已完成
```

<br>
<br>

[Reference](https://zhuanlan.zhihu.com/p/356415669)