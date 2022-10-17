---
title: 解决conda装虚拟Python环境联网失败问题
date: 2022-10-17 10:09:53
categories:
- 答疑
---


<h6 align="center">Editor: Alexander Ezharjan<h6>

1. 使用 `conda create -n carla python=3.7` 命令安装虚拟环境出错，说网络连接异常，经久查询未果：
![在这里插入图片描述](https://img-blog.csdnimg.cn/0af662487e2c48f7baaf3f323d1dbc73.png)

2. 在终端输入下面这些：
```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes
```

3. 走进 `C:/Users/USER_NAME/.condarc`，删除内部的 `-defaults` 选项，保存退出；
![在这里插入图片描述](https://img-blog.csdnimg.cn/3d4a61eddb84466586e14749939fd41c.png)



4. 重新运行 `conda create -n carla python=3.7` 指令即可。

<br>

<br>
<br>


作者：艾孜尔江·艾尔斯兰
