from lanzou.api import LanZouCloud
from lanzou.api.types import *
from typing import List


class LZextends():
    def __init__(self):
        self.lzy = LanZouCloud()
        self.lzy._host_url = 'https://pan.lanzouo.com'

    @staticmethod
    def _all_possible_urls(url: str) -> List[str]:
        """蓝奏云的主域名有时会挂掉, 此时尝试切换到备用域名"""
        available_domains = [
            'lanzouo.com',  # 鲁ICP备15001327号-8, 2021-09-15
            'lanzouw.com',  # 鲁ICP备15001327号-7, 2021-09-02
            'lanzoui.com',  # 鲁ICP备15001327号-6, 2020-06-09, SEO 排名最低
            'lanzoux.com',  # 鲁ICP备15001327号-5, 2020-06-09
            'lanzous.com'  # 主域名, 备案异常, 部分地区已经无法访问
        ]
        return [url.replace('lanzous.com', d) for d in available_domains]
