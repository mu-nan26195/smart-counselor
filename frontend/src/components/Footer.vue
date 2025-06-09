<script setup lang="ts">
</script>

<template>
  <footer class="footer">
    <div class="footer-content">
      <p>© 2023 智能辅导员系统 - 学生服务中心</p>
      <p>如有紧急问题，请联系学校辅导员办公室</p>
    </div>
  </footer>
</template>

<style lang="scss" scoped>
@use '../styles/variables.scss' as *;

.footer {
  background-color: $primary-color;
  color: white;
  padding: 15px 0;
  text-align: center;
  font-size: 0.9rem;

  .footer-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
  }

  p {
    margin: 5px 0;
  }
}
</style>