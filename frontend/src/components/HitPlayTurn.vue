<template>
    <el-carousel :interval="3000" type="card" height="400px">
    <el-carousel-item v-for="(slide, index) in imagejpg" :key="index">
      <div class="carousel-item-content">
        <img :src="require(`@/assets/${slide}`)" alt="" class="carousel-image" />
      </div>
    </el-carousel-item>
  </el-carousel>
</template>
<script setup>
import { ref } from 'vue'
const imagejpg = ref(['头像.jpg', '头像.jpg', '头像.jpg', '头像.jpg', '头像.jpg', '头像.jpg','头像.jpg','头像.jpg','头像.jpg','头像.jpg','头像.jpg'])
</script>
<style scoped>
.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 200px;
  margin:0;
  text-align: center;
}
.carousel-item-content {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  margin: auto;
}

.carousel-image {
  margin: auto;
  width: 200px;
  height: 300px;
}
.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>