import logging

import pathlib
import sys

from typing import Callable
from functools import wraps

###########################################################
#                         logging                         #
###########################################################
logFormatter = logging.Formatter(
    "%(asctime)s %(levelname)-5.5s [%(name)s] %(funcName)s:%(lineno)d: %(message)s"
)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.name = "DNFCalculating"

log_directory = "logs"
try:
    pathlib.Path(log_directory).mkdir(parents=True, exist_ok=True)
except PermissionError as err:
    print("创建日志目录logs失败，请确认是否限制了基础的运行权限")
    sys.exit(-1)


def try_except(show_exception_info=True,
               show_last_process_result=True,
               extra_msg="",
               return_val_on_except=None) -> Callable:
    def decorator(fun):
        @wraps(fun)
        def wrapper(*args, **kwargs):
            try:
                return fun(*args, **kwargs)
            except Exception as e:
                msg = f"执行{fun.__name__}({args}, {kwargs})出错了"
                if extra_msg != "":
                    msg += ", " + extra_msg
                # msg += check_some_exception(e, show_last_process_result)

                logFunc = logger.error
                if not show_exception_info:
                    logFunc = logger.debug
                logFunc(msg, exc_info=e)

                return return_val_on_except

        return wrapper

    return decorator
