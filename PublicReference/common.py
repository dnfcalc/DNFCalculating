#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------
# File      : common
# DateTime  : 2020/6/11 0011 16:43
# Author    : Chen Ji
# Email     : fzls.zju@gmail.com
# -------------------------------

import platform

if platform.system() == "Windows":
    import win32api
    import win32con


def notify_error(logger, message):
    if logger is not None:
        logger.error(message)
    if platform.system() == "Windows":
        win32api.MessageBox(0, message, "出错啦", win32con.MB_ICONWARNING)


# 格式化时间为比较美观的格式
def format_time(ftime):
    days, remainder = divmod(ftime, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    remaining_time_str = ""
    if days > 0:
        remaining_time_str += "{}d".format(int(days))
    if days > 0 or hours > 0:
        remaining_time_str += "{:02}h".format(int(hours))
    if hours > 0 or minutes > 0:
        remaining_time_str += "{:02}m".format(int(minutes))
    remaining_time_str += "{:02.2f}s".format(seconds)

    return remaining_time_str
