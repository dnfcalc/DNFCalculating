export default function openURL(router: any, url: string, args: {}) {
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
