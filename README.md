## 简介

web:vue3+TS+electron+vite<br>
参考项目：https://github.com/caoxiemeihao/electron-vue-vite<br>
备选参考：https://github.com/umbrella22/electron-vite-template<br>
api:python+FastAPI

## 项目依赖安装

先安装好 python3.6 以上、node 16 以上

```
  git clone https://gitee.com/i_melon/dnfcalculating_110
  cd api
  pip install fastapi requests
  pip install uvicorn[standard]

  cd ..
  npm install -g pnpm

  如果依赖安装过慢，可设置镜像
  pnpm config set registry https://registry.npmmirror.com/
  或 
  pnpm install -g nrm 
  nrm use taobao

  pnpm install

```

## 项目运行

```
  pnpm dev
```

## 项目进展

### api

- [x] 基础结构
- [x] 全局异常处理
- [x] 跨域
- [ ] 交互 api 定义
- [ ] 主体逻辑
- [ ] 打包

### web

- [x] vue3 集成 electron
- [ ] 其他核心部分
