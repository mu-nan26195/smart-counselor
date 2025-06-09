<script setup lang="ts">
import { Avatar, User } from '@element-plus/icons-vue'
</script>

<template>
  <header class="header">
    <div class="header-content">
      <div class="logo">
        <el-icon size="32" color="#409EFF">
          <Avatar />
        </el-icon>
        <h1>智能辅导员系统</h1>
      </div>
      <div class="user-info">
        <el-icon size="24">
          <User />
        </el-icon>
        <span>学生用户</span>
      </div>
    </div>
  </header>
</template>

<style lang="scss" scoped>
@use '../styles/variables.scss' as *;

.header {
  background-color: $primary-color;
  color: white;
  padding: 15px 0;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);

  .header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
  }

  .logo {
    display: flex;
    align-items: center;
    gap: 10px;

    h1 {
      font-size: 1.5rem;
      font-weight: 600;
      margin: 0;
    }
  }

  .user-info {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.9rem;
  }
}
</style>
