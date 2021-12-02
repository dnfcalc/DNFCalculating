from lanzou.api import LanZouCloud
from lanzou.api.types import *
from typing import List


class LZextends(LanZouCloud):
    def __init__(self):
        self.lzy = LanZouCloud()
        self.lzy._host_url = 'https://pan.lanzouo.com'
        self.lzy.available_domains = [
            'lanzouo.com',  # 2021-09-15 鲁ICP备15001327号-8
            'lanzouw.com',  # 2021-09-02 鲁ICP备15001327号-7
            'lanzoui.com',  # 2020-06-09 鲁ICP备15001327号-6
            'lanzoux.com',  # 2020-06-09 鲁ICP备15001327号-5
        ]
