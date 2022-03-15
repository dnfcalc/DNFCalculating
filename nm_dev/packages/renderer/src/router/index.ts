import { createRouter, createWebHashHistory } from "vue-router"
import type { RouteRecordRaw } from "vue-router"

const routes: RouteRecordRaw[] = [
  {
    path: "/",
    redirect: "/home"
  },
  {
    path: "/home",
    name: "home",
    component: () => import("@/pages/home/home.vue")
  },
  {
    path: "/character/:name",
    name: "character",
    meta: {
      title: "角色"
    },
    component: () => import("@/pages/character/character.vue")
  },
  {
    path: "/panel/custom_selection",
    name: "custom_selection",
    component: () => import("@/pages/panel/custom_selection.vue")
  }
]

if (import.meta.env.DEV) {
  //用于组件展示的页面
  routes.push({
    path: "/show",
    name: "show",
    meta: {
      title: "组件展示"
    },
    component: () => import("@/pages/show.vue")
  })
}

const router = createRouter({
  routes,
  history: createWebHashHistory()
})

export default router
