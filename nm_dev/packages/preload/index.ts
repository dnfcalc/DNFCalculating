import fs from "fs"
import { app, BrowserWindow, contextBridge, ipcRenderer } from "electron"
import { domReady } from "./utils"
import { useLoading } from "./loading"
import { statrServer, stopServer } from "./server"
import { join } from "path"

const { appendLoading, removeLoading } = useLoading()

;(async () => {
  await domReady()

  appendLoading()
})()

// --------- Expose some API to the Renderer process. ---------
// contextBridge.exposeInMainWorld("fs", fs);
contextBridge.exposeInMainWorld("removeLoading", removeLoading)
contextBridge.exposeInMainWorld("newWindow", newWindow)
contextBridge.exposeInMainWorld("server", {
  statrServer: statrServer,
  endServer: stopServer
})
contextBridge.exposeInMainWorld("ipcRenderer", withPrototype(ipcRenderer))

// `exposeInMainWorld` can't detect attributes and methods of `prototype`, manually patching it.
function withPrototype(obj: Record<string, any>) {
  const protos = Object.getPrototypeOf(obj)

  for (const [key, value] of Object.entries(protos)) {
    if (Object.prototype.hasOwnProperty.call(obj, key)) continue

    if (typeof value === "function") {
      // Some native APIs, like `NodeJS.EventEmitter['on']`, don't work in the Renderer process. Wrapping them into a function.
      obj[key] = function (...args: any) {
        return value.call(obj, ...args)
      }
    } else {
      obj[key] = value
    }
  }
  return obj
}

function newWindow(path: string, width: number = 500, height: number = 500) {
  const newW = new BrowserWindow({
    title: "Main window",
    width: width,
    height: height,
    resizable: false,
    webPreferences: {
      preload: join(__dirname, "../preload/index.cjs"),
      webSecurity: false
    }
  })

  if (app.isPackaged || process.env["DEBUG"]) {
    newW.loadFile(join(__dirname, `../renderer/index.html${path}`))
  } else {
    // 🚧 Use ['ENV_NAME'] avoid vite:define plugin
    const url = `http://${process.env["VITE_DEV_SERVER_HOST"]}:${process.env["VITE_DEV_SERVER_PORT"]}${path}`

    newW.loadURL(url)
    // newW.webContents.openDevTools()
  }
}
