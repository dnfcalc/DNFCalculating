export {}

declare global {
  interface Window {
    // Expose some Api through preload script
    fs: typeof import("fs")
    ipcRenderer: import("electron").IpcRenderer
    server: {
      statrServer: () => void
      stopServer: () => void
    }
    removeLoading: () => void
  }
}
