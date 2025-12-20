import { defineStore } from "pinia"

export const useAuthStore = defineStore("auth", {
  state: () => ({
    isAuthenticated: !!localStorage.getItem("access_token"),
  }),
  actions: {
    logout() {
      localStorage.removeItem("access_token")
      localStorage.removeItem("refresh_token")
      this.isAuthenticated = false
    },
  },
})
