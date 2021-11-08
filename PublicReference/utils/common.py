#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------
# File      : common
# DateTime  : 2020/6/11 0011 16:43
# Author    : Chen Ji
# Email     : fzls.zju@gmail.com
# -------------------------------
import re
from typing import Iterable
from .log import *


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


def to_int(content, default=None):
    if re.match("^-?\d+$", content):
        return int(content)
    return default


# 将小数转换为百分比字符串的表示方式
def to_percent(num, digits=0):
    return str(int(round(num * 100, digits))) + "%"


# 将字符串数组批量格式化
def format_range(content: str, items: Iterable, *args, **kwargs):
    return list(map(lambda i: content.format(i, *args, **kwargs), items))
