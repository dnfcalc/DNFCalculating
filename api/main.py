# api docs:https://fastapi.tiangolo.com/zh/tutorial/first-steps/

import json
from fastapi import FastAPI, Request
import uvicorn
import sys
import os
from routers.info import infoRouter
from utils.apiTools import register_exception, register_cors

app = FastAPI()

# 全局的异常处理
register_exception(app)
# 跨域支持
register_cors(app)

# 路由添加注册
app.include_router(infoRouter, prefix="/info", tags=['杂项信息接口'])

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
