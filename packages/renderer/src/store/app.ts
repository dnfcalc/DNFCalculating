import { defineStore } from "pinia"

interface AppState {
  title: string
  id?: number
}

export const useAppStore = defineStore("app", {
  state(): AppState {
    return {
      title: "DNF计算器搭配计算器 & Colg",
      id: undefined
    }
  },
  actions: {
    minimize() {
      window.ipcRenderer.invoke("minimize-win")
    },
    close() {
      window.ipcRenderer.invoke("close-win")
    }
  }
})
