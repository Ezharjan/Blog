1. **切割MP3，按时间准确切割**
 ```
ffmpeg -i F:\源.mp3 -ss 00:20:00 -to 02:30:05 F:\目标文件.mp3
 ```


2. **MTS到MP4**

_说明：（-b 4m：码率是4M；-s 1280*720：这个是设定视频大小。这2个参数其实可以删掉）_

```
ffmpeg -i F:\源.mts -b 4M -s 1280*720 F:\结果.mp4
```


3. **MP4到WMV**

```
ffmpeg -i f:\视频.mp4 -b 4M f:\out.wmv
```

4. **MP4图像旋转** 

_说明：主要参数： -vf "transpose=1" ，这里等于1是顺时针90度旋转；如果用手机录制的时候录反了，则执行2次这个操作就正过来了_

```
ffmpeg -i f:\o.mp4 -vf "transpose=1" f:\o2.mp4
```


5. **MP4到MP4改尺寸**

```
ffmpeg -i G:\源.mp4 -b 4M -s 640*340 g:\OUT.mp4
```

6. **MP4到MP4改尺寸加水印**  

_说明：1: -vf "movie=logo.png [logo];[in][logo] overlay=10:20 [out]" 这里面的是加水印的参数，logo.png是我自己做的PNG水印，大小_
_300*100,10:20是水印的位置，为了方便，就把logo.png拷贝到FFMPEg的bin目录下(必须放，加路径就失败)，这样不用再加路径了 ;2: -b 2M 是用2M压缩率; 3: -s 640*340 意思是图像分辨率改为640*340。_

```
ffmpeg -i G:\源.mp4 -vf "movie=logo.png [logo];[in][logo] overlay=10:20 [out]" -b 2M -s 640*340 g:\OUT.mp4
```


7. **快速剪切某段视频作为输出**

_说明：上面截取 H:\源.mpg 这个视频，从第0秒开始，到23分20秒，这样一段，保存到G:\out.mp4，注意参数必须是 -c copy ，这样执行起来特别快，也就不到半分钟就搞定。_

```
ffmpeg -i H:\源.mpg -ss 0:0:0 -to 0:23:20 -c copy G:\OUT.MP4
```

8. **该编码为H265,让MP4瘦身2/3，1G的MP4可以压缩到300M**

```
ffmpeg -i 源.MP4 -vcodec libx265 -acodec copy F:\OUT.MP4
```


9. **WAV转换格式到amr**

```
ffmpeg -i test.wav -acodec libamr_nb -ab 12.2k -ar 8000 -ac 1 wav2amr.amr
```

10. **提取视频中的声音保存成一个mp3**

```
ffmpeg -i 源.mp4 输出.mp3
```


11. **要实现批量转换，可以直接用这个批处理文件**

```
for %%i in (*.mkv) do ffmpeg.exe -i "%%i" -vcodec copy -acodec copy "%%~ni.mp4"
```

12. **合并多个MP4为一个**

_方法一_

```
ffmpeg -i INPUT1.MP4 -i INPUT2.MP4 -f FORMAT -acodec AUDIOCODEC -vcodec VIDEOCODEC -sameq OUTPUT.MP4
```


_方法二_

（1） 先创建一个文本文件 `filelist.txt`， 内容如下:(注意input1、2、3是你的文件的名字，都在该目录下)

```
file 'input1.mp4'
file 'input2.mp4'
file 'input3.mp4'
```


（2） 以上是这个文本文件的内容，保存后，在命令行执行

```
ffmpeg -f concat -i filelist.txt -c copy output.mp4
```


13. **下载直播流**

```
FFmpeg -i xxxxxxxxx.m3u8 -c copy out.mp4
```

14. **FFmpeg将MP4转换为M3U8**

（1）  直接将MP4文件转成m3u8：

```bash
ffmpeg -i demo.mp4 -hls_time 10 -hls_list_size 0 -hls_segment_filename ene_%05d.ts ene.m3u8
```



（2） 如果已经是ts文件了,则只需要执行下方命令即可:

```bash
 ffmpeg -i demo.ts -c copy -map 0 -f segment -segment_list playlist.m3u8 -segment_time 10 output%03d.ts
```


（3） 将大量分割成ts文件的视频片段全部转换成mp4视频片段 --- 直接上批处理脚本:

```bash
for %%a in ("D:\VideoProjects\NewDemo\*.ts") do ffmpeg -i "%%a"   -vcodec copy -vcodec copy -f mp4 "D:\VideoProjects\NewDemo\NewMP4\%%~na.mp4"
pause
```

（4） 上面的  ffmpeg -i test.ts -acodec copy -vcodec copy -f mp4 test.mp4  是将ts文件转换为mp4文件的意思，再在其之上套了一层for循环，%%a就是每个文件，转换命令最末尾的%%~na是将文件保持原来的文件名的情况下进行输出，存放到指定文件夹的意思。



15. **mp4视频转flv**
```bash
ffmpeg -i test.mp4 -acodec copy -vcodec copy -f flv test.flv 
```

16. **将本地指定的demo.ts文件进行推流**

```bash
 ffmpeg -re  -i demo.ts  -c copy -f mpegts   udp://127.0.0.1:1997
```

17. **强制把输出视频文件帧率改为 24 fps**
```bash
ffmpeg -i input.avi -r 24 output.avi
```


18. **对视频每个一秒截一个图并存在本地**

```bash
ffmpeg -i out.mp4 -f image2 -vf fps=fps=1 out%d.png
```


19. **每隔20秒截一个图**

```bash
ffmpeg -i out.mp4 -f image2 -vf fps=fps=1/20 out%d.png
```


20. **将视频转换为图片，一帧一图**

```bash
ffmpeg -i out.mp4 out%4d.png
```

21. **分割视频，截取视频的指定部分（下放例子是截图前20分59秒），输出out.mp4文件**
```bash
ffmpeg -ss 00:00:00 -i src.mp4 -c copy -t 00:20:59 out.mp4
```

1.  **加速整个视频（含音频）到2倍速**
```
ffmpeg -i input.mkv -filter_complex "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]" -map "[v]" -map "[a]" output.mkv
```



23.  **使用ffmpeg去除视频中的音频**
```
ffmpeg -i .\\input.mp4 -map 0:0 -vcodec copy out.mp4
```

24. **Trim a video**[More](https://shotstack.io/learn/use-ffmpeg-to-trim-video/):
```
ffmpeg -i input.mp4 -ss 00:05:20 -t 00:10:00 -c:v copy -c:a copy output1.mp4
```


25.  Merge audio with video the file - 合并视频和声音，合并视频和音频 [[Ref](https://juejin.cn/s/ffmpeg%20%E5%90%88%E5%B9%B6%E9%9F%B3%E9%A2%91%E5%92%8C%E8%A7%86%E9%A2%91)] ：
```
ffmpeg -i video.mp4 -i audio.mp3 -c copy -map 0:v:0 -map 1:a:0 output.mp4
```

26.  调整音频速率（输入必须得是MP4）:
```
ffmpeg -i input.mp4 -filter:a "atempo=2.0" -vn output.mp3
```


<br><br><br><br>


<br> <a href="https://www.jianshu.com/p/91727ab25227" target="_blank">主要参考</a>
<br> <a href="https://ffmpeg.org/ffmpeg.html" target="_blank">官网</a>
<br> <a href="https://zhuanlan.zhihu.com/p/97914917" target="_blank">视频剪辑参考</a>


<br>

<br>

<br>
