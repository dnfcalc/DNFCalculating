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
    component: () => import("@/pages/character/character.vue")
  }
]

const router = createRouter({
  routes,
  history: createWebHashHistory()
})

export default router
