@ECHO OFF

:: 修改console默认encoding为utf8，避免中文乱码
CHCP 65001

echo.
echo [提示]: 开始打包
echo.


:: 使用pyinstaller打包
pyinstaller.exe --hidden-import pkg_resources.py2_warn  --noconsole -F "main.py"

:: 复制生成的结果后删除临时文件
COPY /Y "dist\main.exe" "main.exe"
RMDIR /S /Q "build" "dist" "__pycache__"
DEL /Q "main.spec"


echo.
echo [提示]: 打包结束
echo.