import json
import sys
import requests
import os

os.chdir(sys.path[0])


def get_adventure_info():
    adventure_info = {}
    with open("../configFiles/adventure_info.json", encoding='utf-8') as fp:
        adventure_info = json.load(fp)
    return adventure_info


def get_notice():
    notice = {}
    notice = requests.get(
        "https://i_melon.gitee.io/dnfcalculating/notice.json",
        timeout=2).json()
    return notice


def get_blacklistlist():
    blacklistlist = {
        "2190155ee92d17e8cc3b0c9892fd5ac7": {
            "reason": "https://tieba.baidu.com/p/7624625617 不好意思 是计算器配不上你"
        },
        "99a2f094ef7daa0d53525b0f2474c0ea": {
            "reason": "https://bbs.colg.cn/thread-8355814-1-1.html 带??节奏"
        },
        "1ba5ea8fa16964666f0c0a85e89c3e96": {
            "reason":
            "https://bbs.colg.cn/thread-8358088-1-1.html 带节奏能请先把龙虎啸等级和其他计算搞清楚"
        },
        "2e3d28298db82f8b23dc9fa6aac14b6d": {
            "reason":
            "https://bbs.colg.cn/thread-8358088-1-1.html 带节奏能请先把龙虎啸等级和其他计算搞清楚"
        },
        "f8b3cf5c269c97a8d6d2d97ecf769a06": {
            "reason": "屠戮直播带节奏"
        },
        "761cf5dbd2e3d07e8eaaf1dc99ebc49b": {
            "reason": "https://bbs.colg.cn/thread-8382566-1-1.html"
        }
    }
    # 同步获取服务上的黑名单
    return blacklistlist