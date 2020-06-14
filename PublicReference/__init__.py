#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------
# File      : logging
# DateTime  : 2020/6/10 0010 17:21
# Author    : Chen Ji
# Email     : fzls.zju@gmail.com
# -------------------------------
import logging
import pathlib
import sys
from datetime import datetime

from .common import *

###########################################################
#                         logging                         #
###########################################################
logFormatter = logging.Formatter("%(asctime)s %(levelname)-5.5s [%(name)s] %(funcName)s:%(lineno)d: %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.name = "DNFCalculating"

log_directory = "logs"
try:
    pathlib.Path(log_directory).mkdir(parents=True, exist_ok=True)
except PermissionError as err:
    print("创建日志目录logs失败，请确认是否限制了基础的运行权限")
    sys.exit(-1)

fileHandler = logging.FileHandler("{0}/{1}.log".format(log_directory, datetime.now().strftime('{}_%Y_%m_%d_%H_%M_%S'.format(logger.name))), encoding="utf-8")
fileHandler.setFormatter(logFormatter)
fileHandler.setLevel(logging.DEBUG)
logger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
consoleHandler.setLevel(logging.INFO)
logger.addHandler(consoleHandler)
