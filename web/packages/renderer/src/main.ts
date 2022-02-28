import { createApp } from "vue";
import App from "./App.vue";

// 在vue3渲染前开启api服务
window.server.statrServer();

createApp(App).mount("#app").$nextTick(window.removeLoading);

// console.log('fs', window.fs)
// console.log('ipcRenderer', window.ipcRenderer)

// Usage of ipcRenderer.on
// window.ipcRenderer.on("main-process-message", (_event, ...args) => {
//   console.log("[Receive Main-process message]:", ...args);
// });
