<template>
    <el-carousel :interval="3000" type="card" height="400px">
    <el-carousel-item v-for="(movie, index) in hotMovie" :key="index">
      <div class="carousel-item-content">
        <img :src=movie alt="" class="carousel-image" style="width: 100%; height: 100%;"/>
      </div>
    </el-carousel-item>
  </el-carousel>
  <guess-likes/>
</template>
<script setup>
import GuessLikes from '@/components/GuessLikes';
import { reactive } from 'vue';
const hotMovie = reactive([
    'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg',
    'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2561716440.jpg',
    'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2578474613.jpg',
    'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p492406163.jpg',
    'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p1505392928.jpg',
]);

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