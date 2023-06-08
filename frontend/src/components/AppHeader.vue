<template>
  <el-header>
    <el-menu mode="horizontal" router>
      <a href="/" class="logo" style="margin-top: auto; margin-bottom: auto; margin-right: 20px">
        <el-avatar style="margin-top: auto; margin-bottom: auto; margin-right: 20px" :src="require('@/assets/头像.jpg')" />
      </a>
      <el-menu-item index="/" class="title">黄哥说电影</el-menu-item>
      <el-sub-menu index="2">
        <template #title>Workspace</template>
      </el-sub-menu>
      <el-menu-item index="/MovieSearch">MovieSearch</el-menu-item>
      <el-menu-item index="/4">Orders</el-menu-item>
      <el-menu-item index="/2">
        <el-input v-model="input" class="w-50 m-2 search" placeholder="Type something">
          <template #append>
            <el-icon class="el-input__icon"><search /></el-icon>
          </template>
        </el-input>
      </el-menu-item>
      <el-popover placement="top-start" :width="200">
        <template #reference>
          <el-avatar style="margin: auto" :src="require('@/assets/头像.jpg')" />
        </template>
        <template #default>
          <div class="demo-rich-conent" style="display: flex; gap: 16px; flex-direction: column">
            <el-avatar :size="60" :src="require('@/assets/头像.jpg')" style="margin-bottom: 8px; margin: auto" />
          </div>
          <el-menu router>
            <el-menu-item index="/2" @click="test" style="cursor: pointer">个人中心</el-menu-item>
            <el-menu-item index="">退出登录</el-menu-item>
          </el-menu>
        </template>
      </el-popover>
    </el-menu>
  </el-header>
</template>

<script setup>
import { ref } from 'vue';
import { Search } from '@element-plus/icons-vue'
import $ from 'jquery';
const input = ref('')

const test = () => {
  $.ajax({
    url: 'http://8.130.99.147:8000/api/test/',
    success: response => {
      console.log(response);
    }
  })
}
</script>

<style scoped>
.title {
  font-size: 18px;
}

.search {
  margin-top: 12px;
}
</style>