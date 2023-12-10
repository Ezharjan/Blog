Linux应知应会
Ezharjan Linux
Linux Commands
Linux常用指令合集
Linux必备指令合集

<br>

---

# Linux Commands

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
srun -p gpu_batch --gres=gpu:GPU_COUNT python xxx
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


22. Linux无法删除文件夹 Device or resource busy，查看资源占用进程 lsof +d /local/ 显示目录占用的进程
```bash
lsof +d /YOUR_DIR_NAME/
kill -9 PID_FOUND_ABOVE
```

23. 查看Linux主机信息：
```sh
uname -a # 查看内核/操作系统/CPU信息
head -n 1 /etc/issue # 查看操作系统版本
cat /proc/cpuinfo # 查看CPU信息
hostname # 查看计算机名
lspci -tv # 列出所有PCI设备
lsusb -tv # 列出所有USB设备
lsmod # 列出加载的内核模块
env # 查看环境变量 资源
free -m # 查看内存使用量和交换区使用量
df -h # 查看各分区使用情况
du -sh # 查看指定目录的大小
grep MemTotal /proc/meminfo # 查看内存总量
grep MemFree /proc/meminfo # 查看空闲内存量
uptime # 查看系统运行时间、用户数、负载
cat /proc/loadavg # 查看系统负载 磁盘和分区
mount | column -t # 查看挂接的分区状态
fdisk -l # 查看所有分区
swapon -s # 查看所有交换分区
hdparm -i /dev/hda # 查看磁盘参数(仅适用于IDE设备)
dmesg | grep IDE # 查看启动时IDE设备检测状况 网络
ifconfig # 查看所有网络接口的属性
iptables -L # 查看防火墙设置
route -n # 查看路由表
netstat -lntp # 查看所有监听端口
netstat -antp # 查看所有已经建立的连接
netstat -s # 查看网络统计信息 进程
ps -ef # 查看所有进程
top # 实时显示进程状态 用户
w # 查看活动用户
id # 查看指定用户信息
last # 查看用户登录日志
cut -d: -f1 /etc/passwd # 查看系统所有用户
cut -d: -f1 /etc/group # 查看系统所有组
crontab -l # 查看当前用户的计划任务 服务
chkconfig –list # 列出所有系统服务
chkconfig –list | grep on # 列出所有启动的系统服务 程序
rpm -qa # 查看所有安装的软件包
```


24.  批量解压当前目录下所有的zip文件：
```bash
ls *.zip | xargs -n1 unzip
```

25. 将命令放到全局：
```bash
# 通过软连接的方式链接到/usr/bin/目录下
sudo ln -s /absolute/path/to/folder/contains/executable/file/ /usr/bin/name_to_execute
```


26. 查看所有的安装过的应用和它的包：
```bash
sudo dpkg –list
```

27.  彻底卸载某个包及其附属组件
```bash
sudo apt purge <package_name>
```


28.  Grant permission to all the users for files and folders recursively in this directory:
```bash
# - `0` indicates no permissions (`---`).
# - `1` indicates execute permission only (`--x`).
# - `2` indicates write permission only (`-w-`).
# - `3` indicates write and execute permissions (`-wx`).
# - `4` indicates read permission only (`r--`).
# - `5` indicates read and execute permissions (`r-x`).
# - `6` indicates read and write permissions (`rw-`).
# - `7` indicates read, write, and execute permissions (`rwx`).
sudo chmod -R 777 .
```


29. Extract a `*.tar.gz` file using `tar` command:
```bash
tar -zxvf filename.tar.gz -C /path/to/directory
```




<br>


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

[Reference1](https://zhuanlan.zhihu.com/p/356415669)
[Reference2](https://zhuanlan.zhihu.com/p/54903290)

<br>
<br>

# Conda (Anaconda) Commands


1. View existing Conda environment:
```bash
conda info --envs
conda env list
```

2. Create new environment
```bash
conda create -n ENV_NAME python=3.7 -y
```

3. Activate new environment on Windows:
```bash
activate ENV_NAME
```

4. Remove some installed environment:
```bash
conda remove -n ENV_NAME --all -y
```

4. If there are permissions failure while removing a conda environment, try:
```bash
sudo chown -R $USER:$USER PATH_TO_anaconda3
# OR: conda update -n base -c defaults conda
```


5. Clone one conda environment to another:
```bash
conda create -n new_env --clone template_env -y
```


6. Change Python version in current Conda environment:
```bash
conda install python=3.7
```

7. Use `conda activate env_name` command inside a bash file on Linux: 
```bash
eval "$(conda shell.bash hook)"
conda activate env_name
```

8. Create Conda environment via existing `environment.yml`:
```bash
conda env create -f environment.yml
```

9. Store configuration of the current Conda environment into a file.
```bash
conda env export > environment.yml
```

10.  Rename virtual environment:
```bash
conda rename -n old_name -d new_name 
```

 


<br>
<br>

[Download Andoconda](https://www.anaconda.com/)



<br>

# Tmux Commands

1. 安装 tmux ：
```bash

# Ubuntu 或 Debian
$ sudo apt-get install tmux

# CentOS 或 Fedora
$ sudo yum install tmux

```

2. 启动 tmux ：
```bash
tmux
```


3. 新建会话，使用编号区分会话，不太直观，更好的方法是为会话起名：
```bash
tmux
tmux new -s <session-name>
```

4. 分离会话，在 Tmux 窗口中，按下Ctrl+b d或者输入tmux detach命令，就会将当前会话与窗口分离：
```bash
tmux detach
```

5. 查看当前所有的 Tmux 会话：
```bash
tmux ls
```

6. 接入会话，重新接入某个已存在的会话：
```bash
# 使用会话编号
tmux attach -t 0

# 使用会话名称
tmux attach -t <session-name>
```

7. 杀死会话：
```bash
# 使用会话编号
tmux kill-session -t 0

# 使用会话名称
tmux kill-session -t <session-name>
```

8. 切换会话：
```bash
# 使用会话编号
tmux switch -t 0

# 使用会话名称
tmux switch -t <session-name>
```

9. 重命名会话：
```bash
tmux rename-session -t 0 <new-name>
```

10. 会话快捷键：
```txt
Ctrl+b d：分离当前会话。
Ctrl+b s：列出所有会话。
Ctrl+b $：重命名当前会话。
```


11. tmux 最简操作流程：
- 新建会话tmux new -s my_session。
- 在 Tmux 窗口运行所需的程序。
- 按下快捷键Ctrl+b d将会话分离。
- 下次使用时，重新连接到会话tmux attach-session -t my_session。

[点此查看更多tmux指令](https://www.ruanyifeng.com/blog/2019/10/tmux.html)。


<br>


# Git Commands

1. Git 暂存当前内容：
```bash
git stash save [stashMessage]
```

2. 取出之前储藏的修改：
```bash
git stash pop
```

3. 查看储藏记录列表：
```bash
git stash list
```

4. 取出指定index的储藏的修改到工作区中：
```bash
git stash apply stash@{index} 
```

5. 将指定index的储藏从储藏记录列表中删除：
```bash
git stash drop stash@{index}
```

6. 新建分支
```bash
git branch xxx (xxx填写你的分支名称)
```

7. 查看所有分支
```bash
git branch -a
```


8. 切换到某一分支
```bash
git checkout xxx (xxx填写要切换的分支名称）
```


9. 添加修改代码到缓存，注意最后的"."前面有个空格
```bash
git add .
```

10. 添加提交代码的备注
```bash
git commit -m "xxx" （xxx为本次提交代码的备注）
```

11. 提交代码到指定分支
```bash
git push origin xxx （xxx为要提交代码的分支名称）
```

12. 撤销所有本次未提交的修改（相当于Tortoise Git的revert按钮）：
```bash
git checkout . 
```

13. 恢复某个已修改的文件（撤销未提交的修改）：
```bash
git checkout file-name
```

14. 撤销某次操作，此次操作之前和之后的commit和history都会保留，并且把这次撤销（git revert是提交一个新的版本，将需要revert的版本的内容再反向修改回去，版本会递增，不影响之前提交的内容）：
```bash
 git revert HEAD                  # 撤销前一次 commit
 git revert HEAD^                   # 撤销前前一次 commit
 git revert commit-id
 #（比如：fa042ce57ebbe5bb9c8db709f719cec2c58ee7ff）撤销指定的版本，撤销也会作为一次提交进行保存。
```

15. 返回到某个节点，不保留本次所操作的修改：
```bash
git reset --hard HASH
```

16. 返回到某个节点，保留本次所操作的修改：
```bash
git reset --soft HASH
```

17. 把所有没有提交的修改暂存到stash里面（可用 git stash pop 恢复）：
```bash
git stash
```

18. 查看所有的历史版本：
```bash
git log
```

19. Copy a directory to another place:
```bash
cp -r source_directory destination_directory
```

20. Download only one folder of a large repository:
```bash
git clone -n git://path/to/the_repo.git --depth 1
cd the_repo
git checkout HEAD file_or_folder_name
```

21. Store Git credentials to avoid entering configuration everytime:
```bash
git config credential.helper store
```


<br>
<br>
<br>
<br>
<br>
<br>

作者：艾孜尔江
