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

5. Run CMD as administrator:
   - Press Windows + R, type cmd in Run box, and press `Ctrl + Shift + Enter` to run Command Prompt as administrator.


6. Check the Hash code of a file using Powershell ([Reference](https://docs.precisely.com/docs/sftw/spectrum/ProductUpdateSummary/ProductUpdateSummary/source/about_sha256.html)):
```bash
Get-fileHash <file_name>
```

7. Other useful commands([Reference](https://www.youtube.com/watch?v=Jfvg3CS1X3A)):
```bash
ipconfig
ipconfig /all
findstr
ipconfig /release
ipconfig /renew
ipconfig /displaydns
ipconfig /renew
clip
ipconfig /flushdns
nslookup
cls
getmac /v
powercfg /energy
powercfg /batteryreport
assoc
chkdsk /f
chkdsk /r
sfc /scannnow
DISM /Online /Cleanup /CheckHealth
DISM /Online /Cleanup /ScanHealth
DISM /Online /Cleanup /RestoreHealth
tasklist
taskkill
netsh wlan show wlanreport
netsh interface show interface
netsh interface ip show address | findstr "IP Address"
netsh interface ip show dnsservers
netsh advfirewall set allprofiles state off
netsh advfirewall set allprofiles state on
ping
ping -t
tracert
tracert -d
netstat
netstat -af
netstat -o
netstat -e -t 5
route print
route add
route delete
shutdown /r /fw /f /t 0
```

<br>

<br>

<br>

作者：艾孜尔江
