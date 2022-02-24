const port: number = 17173;
const child_process = require("child_process");

export default {
  /**
   * 开启python的api服务
   * @returns
   */
  StatrServer() {
    // TODO 启动python api 待改进 后续添加端口占用判断等
    child_process.exec(`python ../api/main.py ${port}`);
  },
  /**
   * 关闭python的api服务
   * @returns
   */
  StopServer() {
    // TODO
    
  },
};
