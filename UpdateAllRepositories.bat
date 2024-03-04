@echo off
setlocal

rem 设置仓库所在的目录
set "repoDir=D:\Github"

rem 遍历目录获取所有仓库名称
for /d %%G in ("%repoDir%\*") do (
    echo Updating repository: %%~nxG
    cd "%%G"
    git pull
    echo.
)

endlocal

pause