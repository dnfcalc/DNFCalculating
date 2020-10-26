@ECHO OFF

:: 修改console默认encoding为utf8，避免中文乱码
CHCP 65001

echo.
echo [提示]: 开始发布版本
echo.

echo [提示]: 开始生成exe文件
:: 使用pyinstaller打包
pyinstaller.exe --hidden-import pkg_resources.py2_warn  --noconsole -F -i ./ResourceFiles/img/logo.ico "main.py"

echo [提示]: 生成结束

if not exist Publish MD Publish

echo [提示]: 开始压缩打包版本
:: 复制生成的结果后删除临时文件
COPY /Y "dist\main.exe" "\publish\main.exe"
RMDIR /S /Q "build" "dist" "__pycache__" "logs" ".\Part\__pycache__" ".\PublicReference\__pycache__"
DEL /Q ".\Publish\*.*"
DEL /Q "main.spec"

Rar.exe a ".\publish\DNF计算器%date:~8,2%.%date:~11,2%.zip" "\publish\main.exe" "ResourceFiles"

Rar.exe a ".\publish\%date:~8,2%.%date:~11,2%.zip" "ResourceFiles" "main.py" "Part" "PublicReference"

DEL /Q "\publish\main.exe"
echo [提示]: 打包结束

echo [提示]: 开始记录更新日志
node release_produce.js

pandoc -s CHANGELOG.md -o ".\publish\更新日志%date:~8,2%.%date:~11,2%.docx"

echo [提示]: 记录结束

echo.
echo [提示]: 发布结束,发布包参见Publish文件夹
echo.

set /p var=任意键继续: