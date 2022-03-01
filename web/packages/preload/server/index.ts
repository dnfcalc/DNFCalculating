const port: number = 17173
const child_process = require('child_process')

/**
 * 开启python的api服务
 * @returns
 */
export function statrServer() {
  // TODO 启动python api 待改进 后续添加端口占用判断等
  console.log('statrServer')
  if (process.platform == 'win32')
    child_process.exec(`python ../api/main.py ${port}`)
  else child_process.exec(`python3 ${__dirname}/../../../api/main.py ${port}`)
}

/**
 * 关闭python的api服务
 * @returns
 */
export function stopServer() {
  // TODO 关闭python api
  console.log('stopServer')
}
