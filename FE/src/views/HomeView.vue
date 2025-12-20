<template>
  <div class="chat-container">
    <!-- Header -->
    <header class="chat-header">
      <h2>AI Chatbot</h2>
      <button class="logout-btn" @click="logout">로그아웃</button>
    </header>

    <!-- Chat messages -->
    <div class="chat-messages">
      <div
        v-for="(msg, idx) in messages"
        :key="idx"
        :class="['message', msg.role]"
      >
        {{ msg.content }}
      </div>
    </div>

    <!-- Input -->
    <form class="chat-input" @submit.prevent="sendMessage">
      <input
        v-model="input"
        placeholder="메시지를 입력하세요..."
      />
      <button type="submit">전송</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue"
import api from "@/api/axios"
import { useAuthStore } from "@/auth/auth.store"
import { useRouter } from "vue-router"

const router = useRouter()
const authStore = useAuthStore()

const input = ref("")
const messages = ref([
  { role: "bot", content: "안녕하세요! 무엇을 도와드릴까요?" },
])

const sendMessage = async () => {
  if (!input.value.trim()) return

  const userMessage = input.value
  messages.value.push({ role: "user", content: userMessage })
  input.value = ""

  try {
    const res = await api.post("/chat/", {
      message: userMessage,
    })

    messages.value.push({
      role: "bot",
      content: res.data.reply,
    })
  } catch (e) {
    messages.value.push({
      role: "bot",
      content: "오류가 발생했습니다.",
    })
  }
}

const logout = () => {
  authStore.logout()
  router.push("/login")
}
</script>

<style scoped>
.chat-container {
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.chat-header {
  padding: 16px;
  background: #1f2937;
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logout-btn {
  background: transparent;
  border: 1px solid #ccc;
  color: white;
  padding: 6px 12px;
  border-radius: 6px;
  cursor: pointer;
}

.chat-messages {
  flex: 1;
  padding: 16px;
  overflow-y: auto;
  background: #f3f4f6;
}

.message {
  max-width: 70%;
  padding: 10px 14px;
  margin-bottom: 10px;
  border-radius: 12px;
  font-size: 14px;
}

.message.user {
  background: #2563eb;
  color: white;
  margin-left: auto;
}

.message.bot {
  background: white;
  color: #111;
  margin-right: auto;
}

.chat-input {
  display: flex;
  padding: 12px;
  border-top: 1px solid #ddd;
}

.chat-input input {
  flex: 1;
  padding: 10px;
  border-radius: 8px;
  border: 1px solid #ddd;
}

.chat-input button {
  margin-left: 8px;
  padding: 10px 16px;
  border: none;
  border-radius: 8px;
  background: #2563eb;
  color: white;
  cursor: pointer;
}
</style>
