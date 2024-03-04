@echo off
setlocal

rem 设置仓库所在的目录
set "repoDir=D:\Github"

rem 设置输出文件路径
set "outputFile=D:/remote_urls.md"

rem 清空输出文件
echo. > "%outputFile%"

rem 遍历目录获取所有仓库名称
for /d %%G in ("%repoDir%\*") do (
    echo Updating repository: %%~nxG
    cd "%%G"
    git pull
    echo.
    
    rem 执行 git remote -v 命令，并将包含 "https://xxx.git" 的内容追加到输出文件中
    git remote -v | findstr "https://*" >> "%outputFile%"
)

endlocal
pause