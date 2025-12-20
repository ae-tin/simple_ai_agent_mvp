<template>
  <div class="login-container">
    <div class="login-card">
      <h1 class="title">AI Chatbot</h1>
      <p class="subtitle">
        Google 계정으로 로그인하고<br />
        AI 챗봇 서비스를 이용하세요
      </p>

      <button class="google-btn" @click="loginWithGoogle">
        <img
          src="https://developers.google.com/identity/images/g-logo.png"
          alt="Google"
        />
        Google로 로그인
      </button>
    </div>
  </div>
</template>

<script setup>
const loginWithGoogle = () => {
  window.location.href =
    "http://localhost:80/accounts/google/login/"
}
</script>

<style scoped>
.login-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
}

.login-card {
  width: 360px;
  padding: 40px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.title {
  font-size: 28px;
  font-weight: 700;
  margin-bottom: 8px;
}

.subtitle {
  font-size: 14px;
  color: #666;
  margin-bottom: 30px;
  line-height: 1.5;
}

.google-btn {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background: white;
  cursor: pointer;
  font-size: 14px;
  transition: background 0.2s;
}

.google-btn:hover {
  background: #f7f7f7;
}

.google-btn img {
  width: 18px;
  height: 18px;
}
</style>
