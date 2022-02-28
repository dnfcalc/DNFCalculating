# api docs:https://fastapi.tiangolo.com/zh/tutorial/first-steps/

import json
from fastapi import FastAPI
import uvicorn
import requests
import sys
import os
from utils.types import *

app = FastAPI()

@app.get("/adventureinfo")
async def get_adventure_info(response_model=GenericResponse[List[object]]):
    adventure_info = {}
    with open("api/dataFiles/adventure_info.json", encoding='utf-8') as fp:
        adventure_info = json.load(fp)
    return {
      "code":0,
      "msg":"",
      "data":adventure_info
    }


@app.get("/balcklist")
async def get_balcklist(response_model=GenericResponse[List[object]]):
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
    return {
      "code":0,
      "msg":"",
      "data":balcklist
    }


@app.get("/message")
async def get_notice(response_model=GenericResponse[str]):
    notice = {}
    try:
        notice = requests.get(
            "https://i_melon.gitee.io/dnfcalculating/notice.json",
            timeout=2).json()
    except Exception as error:
        return {
          "code":-1,
          "msg":str(error),
          "data":[]
        }
    return {
      "code":0,
      "msg":"",
      "data":notice
    }


if __name__ == '__main__':
    port = 17173
    try:
        port = int(sys.argv[1])
    except:
        pass
    print(os.getppid())
    uvicorn.run(
        # 运行的 py 文件:FastAPI 实例对象
        app="main:app",
        # 访问url，默认 127.0.0.1
        host="127.0.0.1",
        # 访问端口，默认 8080,后续需要做端口检测是否被占用
        port=port,
        # 热更新，有内容修改自动重启服务器
        reload=True,
        # 同 reload
        debug=True)
