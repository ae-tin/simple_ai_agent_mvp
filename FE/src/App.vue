<template>
  <router-view />
</template>

<script setup>
import { onMounted } from "vue"
import { useRoute, useRouter } from "vue-router"
import { useAuthStore } from "@/auth/auth.store"

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()

onMounted(() => {
  const access = route.query.access
  const refresh = route.query.refresh

  if (access && refresh) {
    localStorage.setItem("access_token", access)
    localStorage.setItem("refresh_token", refresh)
    authStore.isAuthenticated = true

    router.replace("/") // query 제거
  }
})
</script>
