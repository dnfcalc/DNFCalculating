# 使用次数统计脚本
import os
import platform
import threading
import uuid
from functools import wraps
from typing import Any, Callable, Tuple
from urllib.parse import quote_plus
from .config import currentVersion
import sys

import requests

from .log import logger, try_except

# ---------------- 需要自行调整的配置 --------------------------------
# Google Analytics 统计代码的UA，在 https://analytics.google.com/ 申请新的ua，具体流程可百度
GA_TRACKING_ID = "UA-212229431-1"
# ua名称，自定义
USER_AGENT = "DNFCalculating"
# 应用名称，自定义
APP_NAME = "DNFCalculating"
# 网址域名，自定义
DOCUMENT_HOSTNAME = "dnf-calculating.com"
# 版本号，可以使用现在的版本变量
APP_VERSION = currentVersion

# ---------------- 枚举定义 --------------------------------
GA_API_URL = "https://www.google-analytics.com/collect"

GA_REPORT_TYPE_EVENT = "event"
GA_REPORT_TYPE_PAGE_VIEW = "page_view"

# ---------------- utils --------------------------------


def async_call(cb, *args, **params):
    threading.Thread(target=cb, args=args, kwargs=params, daemon=True).start()


def get_cid():
    return "{}-{}".format(platform.node(), uuid.getnode())


def get_resolution() -> str:
    width, height = get_screen_size()
    return f"{width}x{height}"


def get_screen_size() -> Tuple[int, int]:
    """
    :return: 屏幕宽度和高度
    """
    if not is_windows():
        return 1920, 1080

    import win32api
    width, height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
    return width, height


def is_windows() -> bool:
    return platform.system() == "Windows"


# ---------------- 接口封装 --------------------------------


def increase_counter(name: Any = "",
                     ga_type=GA_REPORT_TYPE_EVENT,
                     ga_category="",
                     ga_misc_params: dict = None):
    if "main.py" in sys.argv[0]:
        return
    name = str(name)

    if name == "":
        raise AssertionError("increase_counter name not set")

    async_call(increase_counter_sync_google_analytics, name, ga_type,
               ga_category, ga_misc_params)


@try_except(show_exception_info=False)
def increase_counter_sync_google_analytics(name: str, ga_type: str,
                                           ga_category: str,
                                           ga_misc_params: dict):
    #  上报谷歌分析 v3
    logger.debug(f"report to google analytics v3, name = {name}")

    if ga_type == GA_REPORT_TYPE_EVENT:
        if ga_category == "":
            # 如果ga_category为空，则尝试从name中解析，假设name中以/分隔的第一个部分作为ga_category
            parts = name.split('/', 1)
            if len(parts) == 2:
                ga_category, name = parts
            else:
                ga_category = "counter"
        track_event(ga_category, name, ga_misc_params)
    elif ga_type == GA_REPORT_TYPE_PAGE_VIEW:
        track_page(name, ga_misc_params)
    else:
        logger.error(f"unknow ga_type={ga_type}")


# ---------------- Google Analytics 上报脚本 --------------------------------

# note: 查看数据地址 https://analytics.google.com/analytics/web/#/
# note: 当发现上报失败时，可以将打印的post body复制到 https://ga-dev-tools.web.app/hit-builder/ 进行校验，看是否缺了参数，或者有参数不符合格式
# note: 参数文档 https://developers.google.com/analytics/devguides/collection/protocol/v1/parameters

headers = {
    "user-agent": USER_AGENT,
}

common_data = {
    'v': '1',  # API Version.
    'tid': GA_TRACKING_ID,  # Tracking ID / Property ID.
    'cid': get_cid(
    ),  # Anonymous Client Identifier. Ideally, this should be a UUID that is associated with particular user, device, or browser instance.
    'ua': USER_AGENT,
    'an': APP_NAME,
    'av': APP_VERSION,
    'ds': 'app',
    'sr': get_resolution(),
}


@try_except(show_exception_info=False)
def track_event(category: str,
                action: str,
                label=None,
                value=0,
                ga_misc_params: dict = None):
    if ga_misc_params is None:
        ga_misc_params = {}

    data = {
        **common_data,
        't': 'event',  # Event hit type.
        'ec': category,  # Event category.
        'ea': action,  # Event action.
        'el': label,  # Event label.
        'ev': value,  # Event value, must be an integer
        **ga_misc_params,  # 透传的一些额外参数
    }

    res = requests.post(GA_API_URL, data=data, headers=headers, timeout=10)
    logger.debug(f"request body = {res.request.body}")


@try_except(show_exception_info=False)
def track_page(page: str, ga_misc_params: dict = None):
    if ga_misc_params is None:
        ga_misc_params = {}

    page = quote_plus(page)
    data = {
        **common_data,
        't': 'pageview',  # Event hit type.
        'dh': DOCUMENT_HOSTNAME,  # Document hostname.
        'dp': page,  # Page.
        'dt': "",  # Title.
        **ga_misc_params,  # 透传的一些额外参数
    }

    res = requests.post(GA_API_URL, data=data, timeout=10)
    logger.debug(f"request body = {res.request.body}")


# ---------------- test --------------------------------


def test():
    increase_counter("test_event", GA_REPORT_TYPE_EVENT)
    increase_counter("test_page_view", GA_REPORT_TYPE_PAGE_VIEW)

    # track_event("example", "test")
    track_page("/example/test_quote")

    os.system("PAUSE")


if __name__ == '__main__':
    test()
