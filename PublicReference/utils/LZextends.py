from lanzou.api import LanZouCloud
from lanzou.api.types import *
from typing import List


class LZextends():
    def __init__(self):
        self.lzy = LanZouCloud()

    def get_folder_info_by_url(self, share_url, dir_pwd='') -> FolderDetail:
        for possiable_url in self.all_possiable_urls(share_url):
            folder_info = self.lzy.get_folder_info_by_url(
                possiable_url, dir_pwd)
            if folder_info.code != LanZouCloud.SUCCESS:
                # logger.debug(f"请求{possiable_url}失败，将尝试下一个")
                continue

            return folder_info

        return FolderDetail(LanZouCloud.FAILED)

    def down_file_by_url(self,
                         share_url,
                         pwd='',
                         save_path='./Download',
                         *,
                         callback=None,
                         overwrite=False,
                         downloaded_handler=None) -> int:
        for possiable_url in self.all_possiable_urls(share_url):
            retCode = self.lzy.down_file_by_url(
                possiable_url,
                pwd,
                save_path,
                callback=callback,
                overwrite=overwrite,
                downloaded_handler=downloaded_handler)
            if retCode != LanZouCloud.SUCCESS:
                # logger.debug(f"请求{possiable_url}失败，将尝试下一个")
                continue

            return retCode

        return LanZouCloud.FAILED

    def all_possiable_urls(self, lanzouyun_url: str) -> List[str]:
        old_domain = 'wwx.lanzoui'
        return [
            lanzouyun_url,

            # lanzouyun_url.replace(old_domain, 'wwx.lanzoui'),
            lanzouyun_url.replace(old_domain, 'wws.lanzoui'),
            lanzouyun_url.replace(old_domain, 'pan.lanzoui'),
            lanzouyun_url.replace(old_domain, 'www.lanzoui'),
            lanzouyun_url.replace(old_domain, 'wwx.lanzoux'),
            lanzouyun_url.replace(old_domain, 'wws.lanzoux'),
            lanzouyun_url.replace(old_domain, 'pan.lanzoux'),
            lanzouyun_url.replace(old_domain, 'www.lanzoux'),
            lanzouyun_url.replace(old_domain, 'wwx.lanzous'),
            lanzouyun_url.replace(old_domain, 'wws.lanzous'),
            lanzouyun_url.replace(old_domain, 'pan.lanzous'),
            lanzouyun_url.replace(old_domain, 'www.lanzous'),
        ]
