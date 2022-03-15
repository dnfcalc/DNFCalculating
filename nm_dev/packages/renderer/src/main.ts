import { createApp } from "vue"
import App from "./App.vue"
import { pinia } from "./store"
import router from "./router"

import "uno.css"

import "./assets/style/app.scss"

createApp(App)
  .use(pinia)
  .use(router)
  .mount("#app")
  .$nextTick(window.removeLoading)

// console.log('fs', window.fs)
// console.log('ipcRenderer', window.ipcRenderer)

// Usage of ipcRenderer.on
// window.ipcRenderer.on("main-process-message", (_event, ...args) => {
//   console.log("[Receive Main-process message]:", ...args);
// });
