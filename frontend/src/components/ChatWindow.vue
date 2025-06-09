<script setup>
import { ref, onMounted, nextTick } from 'vue'
import axios from 'axios'
import { ElInput, ElButton, ElScrollbar, ElIcon } from 'element-plus'
import { Position, ArrowRight } from '@element-plus/icons-vue'

const messages = ref([
  {
    text: '您好，我是智能辅导员系统，请问有什么可以帮助您的吗？',
    sender: 'bot',
    timestamp: new Date()
  }
])

const userInput = ref('')
const isLoading = ref(false)
const scrollbarRef = ref(null)

const sendMessage = async () => {
  if (!userInput.value.trim() || isLoading.value) return

  const question = userInput.value.trim()
  messages.value.push({
    text: question,
    sender: 'user',
    timestamp: new Date()
  })
  
  userInput.value = ''
  isLoading.value = true
  
  try {
    const response = await axios.post('http://localhost:5000/api/chat', {
      question: question
    })
    
    if (response.data.code === 200) {
      messages.value.push({
        text: response.data.data.answer,
        sender: 'bot',
        timestamp: new Date()
      })
    } else {
      messages.value.push({
        text: '抱歉，我暂时无法回答这个问题',
        sender: 'bot',
        timestamp: new Date()
      })
    }
  } catch (error) {
    console.error('API请求失败:', error)
    messages.value.push({
      text: '网络错误，请稍后再试',
      sender: 'bot',
      timestamp: new Date()
    })
  } finally {
    isLoading.value = false
    scrollToBottom()
  }
}

const scrollToBottom = () => {
  nextTick(() => {
    if (scrollbarRef.value) {
      scrollbarRef.value.setScrollTop(scrollbarRef.value.wrapRef.scrollHeight)
    }
  })
}

onMounted(() => {
  scrollToBottom()
})
</script>

<template>
  <div class="chat-container">
    <el-scrollbar ref="scrollbarRef" height="65vh" class="messages-container">
      <div v-for="(message, index) in messages" :key="index" :class="['message', message.sender]">
        <div class="message-content">
          <div class="message-text" v-html="message.text.replace(/\n/g, '<br>')"></div>
          <div class="message-time">
            {{ message.timestamp.toLocaleTimeString() }}
          </div>
        </div>
      </div>
      <div v-if="isLoading" class="message bot">
        <div class="message-content">
          <div class="loading-text">正在思考中...</div>
        </div>
      </div>
    </el-scrollbar>
    
    <div class="input-area">
    <el-input
      v-model="userInput"
      placeholder="请输入您的问题..."
      @keyup.enter="sendMessage"
      :disabled="isLoading"
      class="custom-input"
      clearable
    />
    <el-button 
      type="primary" 
      @click="sendMessage"
      :loading="isLoading"
      class="send-button"
    >
      发送
    </el-button>
  </div>
  </div>
</template>

<style lang="scss" scoped>
@use '../styles/variables.scss' as *;
@use "sass:color";

.chat-container {
  width: 100%;       /* 宽度占满父容器 */
  max-width: 400px;  /* 固定最大宽度（可调整） */
  margin: 0 auto;    /* 居中显示 */
  height: 80vh;      /* 固定高度（可调整） */
  display: flex;
  flex-direction: column;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.messages-container {
  padding: 20px;
  flex: 1;
  overflow-y: auto;
  
  .message {
    margin-bottom: 15px;
    display: flex;
    
    &.user {
      justify-content: flex-end;
      
      .message-content {
        background-color: $primary-color;
        color: white;
        border-radius: 12px 12px 0 12px;
      }
    }
    
    &.bot {
      justify-content: flex-start;
      
      .message-content {
        background-color: #f5f7fa;
        color: #333;
        border-radius: 12px 12px 12px 0;
      }
    }
    
    .message-content {
      max-width: 70%;  /* 限制消息宽度 */
      padding: 10px 15px;
      word-break: break-word;  /* 强制换行 */
      white-space: pre-wrap; 
      box-shadow: 0 1px 2px rgb(255, 255, 255);
      
      // .message-text {
      //   line-height: 1.5;
      //   word-break: break-word; /* 确保长单词也会换行 */
      //   white-space: pre-wrap; /* 保留换行符和空格 */
      //   overflow-wrap: break-word; /* 确保长单词或URL会换行 */
      // }
      
      .message-time {
        font-size: 0.75rem;
        color: #999;
        margin-top: 4px;
        text-align: right;
      }
      
      .loading-text {
        color: #666;
        font-style: italic;
      }
    }
  }
}
.input-area {
  padding: 16px;
  background: white;
  display: flex;
  gap: 12px;
  align-items: center;
  border-top: 1px solid #f0f0f0;

  :deep(.custom-input) {
    flex: 1;
    
    .el-input__wrapper {
      padding: 16px 20px;
      height: 56px;
      border-radius: 28px;
      box-shadow: none;
      background: white;
      border: 1px solid #dcdfe6;
      transition: all 0.3s ease;
      font-size: 16px;

      &:hover {
        border-color: #c0c4cc;
      }

      &.is-focus {
        border-color: $primary-color;
        box-shadow: 0 0 0 1px $primary-color inset;
      }
    }
  }

  .send-button {
    width: auto;
    height: 56px;
    padding: 0 24px;
    border-radius: 28px;
    background-color: $primary-color;
    color: white;
    font-size: 16px;
    font-weight: 500;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 8px;

    &:hover {
      background-color: color.adjust($primary-color, $lightness: 8%);
      transform: translateY(-2px);
    }

    &:active {
      transform: scale(0.96);
      transform: translateY(0);
    }

    .el-icon {
      font-size: 18px;
    }
  }
}
</style>