@ECHO OFF

::修改console默认encoding为utf8，避免中文乱码
CHCP 65001

echo.
echo [提示]: 开始发布版本
echo.

echo [提示]: 开始生成exe文件
::使用pyinstaller打包
pyinstaller.exe --hidden-import pkg_resources.py2_warn  --noconsole -F -i ./ResourceFiles/img/logo.ico "main.py"

echo [提示]: 生成结束

if not exist Bulid\Publish MD Bulid\Publish

echo [提示]: 开始压缩打包版本
::复制生成的结果后删除临时文件
DEL /Q "Bulid\Publish\*.*"
DEL /Q "main.spec"
COPY /Y "dist\main.exe" "main.exe"
RMDIR /S /Q "build" "dist" "__pycache__" "logs" ".\Part\__pycache__" ".\PublicReference\__pycache__"
::rar压缩
Bulid\Rar.exe a "Bulid\publish\DNF计算器%Date:~5,2%.%Date:~8,2%.zip" "main.exe" "ResourceFiles"

Bulid\Rar.exe a "Bulid\publish\源码%Date:~5,2%.%Date:~8,2%.zip" "ResourceFiles" "main.py" "Part" "PublicReference"

DEL /Q "main.exe"
echo [提示]: 打包结束

echo [提示]: 开始记录更新日志
node Bulid/release_produce.js

::pandoc将md转换为docx
pandoc -s CHANGELOG.md -o "Bulid\publish\更新日志%Date:~5,2%.%Date:~8,2%.docx"

echo [提示]: 记录结束

@REM if exist upload_lanzouyun.py echo [提示]: 开始上传到网盘
@REM if exist upload_lanzouyun.py python upload_lanzouyun.py
@REM if exist upload_lanzouyun.py echo [提示]: 上传结束

echo.
echo [提示]: 发布结束,发布包参见Publish文件夹
echo.


set /p var=任意键继续: