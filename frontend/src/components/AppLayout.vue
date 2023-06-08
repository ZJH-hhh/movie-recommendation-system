<template>
  <div class="common-layout">
    <el-container>
      <AppHeader />
      <el-main>
        <RouterView/>
      </el-main>
      <el-footer></el-footer>
    </el-container>
  </div>
</template>


<script setup>
import AppHeader from '@/components/AppHeader.vue'


</script>

<style></style>