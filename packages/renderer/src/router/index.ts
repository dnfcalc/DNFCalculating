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
    component: () => import("../views/home/home.vue")
  },
  {
    path: "/character/:charactername",
    name: "character",
    component: () => import("../views/character/character.vue")
  }
]

const router = createRouter({
  routes,
  history: createWebHashHistory()
})

export default router
