import { createApp } from 'vue'
import App from './App.vue'
import { pinia } from './store'
import router from './router'
import 'uno.css'
import './assets/style/app.scss'
// 在vue3渲染前开启api服务
window.server.statrServer()
// 延迟1秒加载，为了防止Python程序还没启动
setTimeout(() => {
  createApp(App)
    .use(pinia)
    .use(router)
    .mount('#app')
    .$nextTick(window.removeLoading)
}, 1000)

// console.log('fs', window.fs)
// console.log('ipcRenderer', window.ipcRenderer)

// Usage of ipcRenderer.on
// window.ipcRenderer.on("main-process-message", (_event, ...args) => {
//   console.log("[Receive Main-process message]:", ...args);
// });
