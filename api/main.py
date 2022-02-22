# api docs:https://fastapi.tiangolo.com/zh/tutorial/first-steps/

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


if __name__ == '__main__':
    uvicorn.run(
        # 运行的 py 文件:FastAPI 实例对象
        app="main:app",
        # 访问url，默认 127.0.0.1
        host="127.0.0.1",
        # 访问端口，默认 8080,后续需要做端口检测是否被占用
        port=6969,
        # 热更新，有内容修改自动重启服务器
        reload=True,
        # 同 reload
        debug=True)
