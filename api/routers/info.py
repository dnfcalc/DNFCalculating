from datetime import datetime
import json
from typing import List
from fastapi import APIRouter
from h11 import Data
from pydantic import BaseModel
import requests
from utils.apiTools import reponse, Return

infoRouter = APIRouter()


class adventureinfo(BaseModel):
    职业系: str
    转职名称: str
    一次觉醒: str
    二次觉醒: str
    三次觉醒: str
    显示名称: str
    类名: str
    类名2: str
    序号: str
    作者: str
    时间: str
    备注: str


@infoRouter.get(path='/adventureinfo', response_model=Return[adventureinfo])
async def get_adventure_info():
    adventure_info = {}
    with open("api/ResourceFiles/adventure_info.json", encoding='utf-8') as fp:
        adventure_info = json.load(fp)
    return reponse(data=adventure_info)


class noteice(BaseModel):
    time: str
    info: str


@infoRouter.get(path='/notice', response_model=Return[noteice])
async def get_notice():
    notice = {}
    notice = requests.get(
        "https://i_melon.gitee.io/dnfcalculating/notice.json",
        timeout=2).json()
    return reponse(data=notice)


@infoRouter.get(path='/balcklist', response_model=Return)
async def get_balcklist():
    balcklist = {
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
    return reponse(data=balcklist)