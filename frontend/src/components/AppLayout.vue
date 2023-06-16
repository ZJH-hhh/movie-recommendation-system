<template>
  <div class="common-layout">
    <el-container>
      <AppHeader />
      <el-main class="main">
        <RouterView/>
      </el-main>
      <el-footer></el-footer>
    </el-container>
  </div>
</template>


<script setup>
import AppHeader from '@/components/AppHeader.vue'


</script>

<style scoped>
.main {
  overflow-y: auto;
}
</style>