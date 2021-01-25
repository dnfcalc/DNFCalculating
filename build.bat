@ECHO OFF

::修改console默认encoding为utf8，避免中文乱码
CHCP 65001

echo.
echo     此文件为自动编译计算器为exe程序脚本,需提前安装以下依赖
echo       - python
echo       - pyinstaller
echo       - PyQt5
echo     如需自动根据submit更新CHANGELOG并生成更新日志,需提前安装以下依赖
echo       - node.js
echo       - pandoc
echo     如需自动上传到蓝奏云,需要提前安装以下依赖
echo       - lanzou-api
echo.

pause

@REM 检查python

@REM for /f "tokens=2" %%h in ('python -h ^| findstr /C:"usage:"') do ^
@REM set PYVER2=%%h
@REM if "%PYVER2%" != "python" (@echo 未安装python)

echo.
echo [提示]: 开始发布版本
echo.

echo [提示]: 开始生成exe文件
::使用pyinstaller打包

RMDIR /S /Q logs
pyinstaller.exe -w AutoRelese\Package.spec

DEL /Q "AutoRelese\Publish\*.*"
DEL /Q "main.spec"
COPY /Y "dist\main.exe" "main.exe"
RMDIR /S /Q "build" "dist" "__pycache__" "logs" ".\Part\__pycache__" ".\PublicReference\__pycache__" ".\PublicReference\utils\__pycache__" ".\PublicReference\choise\__pycache__" ".\PublicReference\equipment\__pycache__"
for /d %%i in (ResourceFiles\*) do if exist "%%i\set" RMDIR /s /q "%%i\set"

echo [提示]: 生成结束

if exist AutoRelese\signtool.exe echo [提示]: 开始code signing
if exist AutoRelese\signtool.exe AutoRelese\signtool.exe sign /n "Open Source Developer, Xinhua Wang" /t http://time.certum.pl/ /fd sha256 /v main.exe
if exist AutoRelese\signtool.exe echo [提示]: code signing结束

if not exist AutoRelese\Publish MD AutoRelese\Publish

if exist AutoRelese\release_produce.js echo [提示]: 开始记录更新日志
if exist AutoRelese\release_produce.js node AutoRelese/release_produce.js
if exist AutoRelese\release_produce.js echo [提示]: 记录结束

if exist AutoRelese\bz.exe echo [提示]: 开始压缩打包版本
::复制生成的结果后删除临时文件
::rar压缩
if exist AutoRelese\bz.exe AutoRelese\bz.exe c -y -r -aoa -fmt:zip -l:9 "AutoRelese\publish\DNF计算器%Date:~5,2%.%Date:~8,2%.zip" "main.exe" "ResourceFiles"
if exist AutoRelese\bz.exe AutoRelese\bz.exe c -y -r -aoa -fmt:zip -l:9 "AutoRelese\publish\源码%Date:~5,2%.%Date:~8,2%.zip" "ResourceFiles" "main.py" "Part" "PublicReference" "README.md" "CHANGELOG.md" "requirements.txt" "LICENSE"
if exist AutoRelese\bz.exe AutoRelese\bz.exe rn "AutoRelese\publish\DNF计算器%Date:~5,2%.%Date:~8,2%.zip" "main.exe" "DNF计算器%Date:~5,2%.%Date:~8,2% 17173DNF.exe"
if exist AutoRelese\bz.exe DEL /Q "main.exe"
if exist AutoRelese\bz.exe echo [提示]: 打包结束

if exist AutoRelese\upload_cookie.json echo [提示]: 开始上传到网盘
if exist AutoRelese\upload_cookie.json python AutoRelese/upload_lanzouyun.py
if exist AutoRelese\upload_cookie.json echo [提示]: 上传结束

RMDIR /S /Q AutoRelese\Publish

echo.
echo [提示]: 发布结束
echo.


set /p var=任意键继续:
pause