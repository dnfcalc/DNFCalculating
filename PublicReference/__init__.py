#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------
# File      : logging
# DateTime  : 2020/6/10 0010 17:21
# Author    : Chen Ji
# Email     : fzls.zju@gmail.com
# -------------------------------

from .utils.common import *
import multiprocessing
from datetime import datetime

process_name = multiprocessing.current_process().name
time_str = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
only_need_main_process_log = True
if not only_need_main_process_log or "MainProcess" in process_name:
    fileHandler = logging.FileHandler("{0}/{1}_{2}_{3}.log".format(
        log_directory, logger.name, process_name, time_str),
                                      encoding="utf-8")
    fileHandler.setFormatter(logFormatter)
    fileHandler.setLevel(logging.DEBUG)
    logger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
consoleHandler.setLevel(logging.INFO)
logger.addHandler(consoleHandler)
