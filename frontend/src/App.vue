<script setup lang="ts">
import { ref } from 'vue'
import Header from './components/Header.vue'
import ChatWindow from './components/ChatWindow.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <div class="app-container">
    <Header />
    <main class="main-content">
      <ChatWindow />
    </main>
    <Footer />
  </div>
</template>

<style lang="scss">
@use './styles/variables.scss' as *;

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background-color: $background-color;
  font-family: 'Helvetica Neue', Arial, sans-serif;
}

.main-content {
  flex: 1;
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}
</style>
