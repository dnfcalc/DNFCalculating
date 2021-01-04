# `macOS`下使用`DNFCalculating`的相关说明

## 环境

- 依赖

&#160; &#160; &#160; &#160; 详见[`README.md`](./README.md)，必要的python包参见[`requirements.txt`](../requirements.txt)。

- 开发者使用的环境

&#160; &#160; &#160; &#160; macOS Big Sur 版本11.1
&#160; &#160; &#160; &#160; Python 3.8.3
&#160; &#160; &#160; &#160; pip 20.3.3


## 使用

&#160; &#160; &#160; &#160; 直接在`Finder`中双击`run_mac_version.command`即可运行。

&#160; &#160; &#160; &#160; 或者在`终端(Terminal)`中，执行命令`python3.8 main.py`即可运行。

## 更新日志

&#160; &#160; &#160; &#160; 1、更新了源码中文件路径部分的代码，以保证`Windows`和`macOS`均可正常打开。

&#160; &#160; &#160; &#160; 2、更新了`requirements.txt`中相关python包及版本。在源码中暂未用到`pypiw32`，故将其移除；`PyQt5 5.15.1`无法适配`macOS Big Sur`及更高版本，故将其更新为`PyQt5 5.15.2`。

## 开发者

&#160; &#160; &#160; &#160; ModnarShen 2021/01/04

