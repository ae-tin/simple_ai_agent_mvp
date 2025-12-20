import { createRouter, createWebHistory } from "vue-router"
import LoginView from "@/views/LoginView.vue"
import HomeView from "@/views/HomeView.vue"
import { useAuthStore } from "@/auth/auth.store"

const routes = [
  {
    path: "/login",
    component: LoginView,
  },
  {
    path: "/",
    component: HomeView,
    meta: { requiresAuth: true },
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()

  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next("/login")
    return
  }

  if (to.path === "/login" && authStore.isAuthenticated) {
    next("/")
    return
  }

  next()
})

export default router
