import type { Router } from "vue-router"

export default function openURL(router: Router, url: string, args: {}) {
  try {
    window.ipcRenderer.invoke("open-win", {
      url: url,
      ...args
    })
  } catch (err) {
    let routerURL = router.resolve({
      path: url
    })
    window.open(routerURL.href, "_blank")
    // router.push(url)
  }
}
