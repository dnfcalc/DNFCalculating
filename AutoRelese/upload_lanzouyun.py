import json
from lanzou.api import LanZouCloud
import os

# pip install lanzou-api
# https://github.com/zaxtyson/LanZouCloud-API

class Uploader:
    # 源码目录
    _folder_id_dnf_calc_code = "1989903"
    # 版本目录
    _folder_id_dnf_calc_publish = "1860455"

    def __init__(self, cookie):
        self.lzy = LanZouCloud()
        self.login_ok = self.lzy.login_by_cookie(cookie) == LanZouCloud.SUCCESS
        if self.login_ok:
            self._folder_dnf_calc_code = self.lzy.get_folder_info_by_id(self._folder_id_dnf_calc_code).folder
            self._folder_dnf_calc_publish = self.lzy.get_folder_info_by_id(self._folder_id_dnf_calc_publish).folder

    def upload_to_lanzouyun(self, filepath, target_folder):
        def on_uploaded(fid, is_file):
            if not is_file:
                return
            files = self.lzy.get_file_list(target_folder.id)
            self.lzy.move_file(fid, target_folder.id)

        # 上传到指定的文件夹中
        retCode = self.lzy.upload_file(filepath, -1, callback=self.show_progress, uploaded_handler=on_uploaded)
        if retCode != LanZouCloud.SUCCESS:
            # logger.error("上传失败，retCode={}".format(retCode))
            return False

        return True

    def show_progress(self, file_name, total_size, now_size):
        """显示进度的回调函数"""
        percent = now_size / total_size
        bar_len = 40  # 进度条长总度
        bar_str = '>' * round(bar_len * percent) + '=' * round(bar_len * (1 - percent))
        print('\r{:.2f}%\t[{}] {:.1f}/{:.1f}MB | {} '.format(
            percent * 100, bar_str, now_size / 1048576, total_size / 1048576, file_name), end='')
        if total_size == now_size:
            print('')  # 下载完成换行
    
    def clearOldVersion(self):
        # 清空版本目录
        path = self.lzy.get_file_list(self._folder_id_dnf_calc_code)
        for item in path:
            if item.name.startswith("源码"):                
                self.lzy.delete(item.id)
        path = self.lzy.get_file_list(self._folder_id_dnf_calc_publish)
        for item in path:
            if item.name.startswith("DNF计算器") or item.name.startswith("更新日志"): 
                self.lzy.delete(item.id)



if __name__ == '__main__':
    # upload_cookie.json 格式参考
    # {
    # 	"ylogin": "~~~~~~~",
    # 	"phpdisk_info": "~~~~~~~~~~~"
    # }
    with open("AutoRelese\\upload_cookie.json") as fp:
        cookie = json.load(fp)
    uploader = Uploader(cookie)   
    if uploader.login_ok:
        files = os.listdir("AutoRelese\\Publish")
        print(files)
        if len(files) > 0:
        # 删除文件
            uploader.clearOldVersion()
        # 添加文件
        for fileName in files:
            file = "AutoRelese\\Publish\\"+fileName
            if fileName.startswith("DNF计算器") or fileName.startswith("更新日志"):     
                uploader.upload_to_lanzouyun(file, uploader._folder_dnf_calc_publish)
            if fileName.startswith("源码"): 
                uploader.upload_to_lanzouyun(file, uploader._folder_dnf_calc_code)

