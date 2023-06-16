<template>
  <div class="container">
    <meta name=referrer content=no-referrer>
    <div class="tags">
      <span
        v-for="tag in tags"
        :key="tag.id"
        :class="{ }"
        @click="toggleTag(tag.name)"
      >
        {{ tag.name }}
      </span>
    </div>

    <div class="movies">
      <ul class="horizontal-list">
        <li v-for="movie in movies" :key="movie.id" style="height: 310px;width: 200px;">
          <div>
            <div class="movie-container">
              <img :src=movie.image_url alt="" style="height: 270px;width: 186px; border-radius: 10px">
              <div style="font-size: 16px; font-weight: bolder; text-align: center">{{ movie.title }}</div>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { onMounted, reactive, ref } from 'vue';
import $ from 'jquery';

const movies = reactive([]);
const movie = ref()
const tags = ref([
  { id: 1, name: '动作' },
  { id: 2, name: '喜剧' },
  { id: 3, name: '剧情' },
  { id: 4, name: '爱情' },
  { id: 5, name: '科幻' },
  { id: 6, name: '动画' },
  { id: 7, name: '悬疑' },
  { id: 8, name: '惊悚' },
  { id: 9, name: '恐怖' },
  { id: 10, name: '纪录片' },
  { id: 11, name: '短片' },
  { id: 12, name: '情色' },
  { id: 13, name: '音乐' },
  { id: 14, name: '歌舞' },
  { id: 15, name: '家庭' },
  { id: 16, name: '儿童' },
  { id: 17, name: '传记' },
  { id: 18, name: '历史' },
  { id: 19, name: '战争' },
  { id: 20, name: '犯罪' },
  { id: 21, name: '西部' },
  { id: 22, name: '奇幻' },
  { id: 23, name: '冒险' },
  { id: 24, name: '灾难' },
  { id: 25, name: '武侠' },
  { id: 26, name: '古装' },
  { id: 27, name: '运动' },
  { id: 28, name: '黑色电影' },
  // 其他标签...
]);

onMounted(() => {
  $.ajax({
    url: 'http://8.130.99.147:8000/api/rank/',
    type: 'GET',
    data: {
      tag: 'all',
    },
    success: response => {
      response.data.forEach(element => {
        movies.push({
          title: element.fields.movie_title,
          image_url: element.fields.img_url,
        });
      });
    }
  })
})

function toggleTag(tagId) {
  movie.value = tags.value.find(item => item.name === tagId);
  // console.log(movie.value.name);
  $.ajax({
    url: 'http://8.130.99.147:8000/api/rank/',
    type: 'GET',
    data: {
      tag: movie.value.name,
    },
    success: response => {
      // Object.assign(movies, {})
      movies.splice(0, movies.length)
      response.data.forEach(element => {
        movies.push({
          title: element.fields.movie_title,
          image_url: element.fields.img_url,
        });
      });
      // console.log(movies);
    }
  })
}


</script>

<style scoped>
.tags {
  margin-bottom: 16px;
  text-align: center;
}

.tags span {
  display: inline-block;
  padding: 8px 16px;
  margin-right: 8px;
  background-color: #eee;
  cursor: pointer;
}

.tags span.active {
  background-color: #333;
  color: #fff;
}

.movies {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  grid-gap: 16px;
  margin-left: 100px;
}

.movie-container {
  width: 186px;
  height: 303px;
}

.horizontal-list {
  display: flex;
  list-style: none;
  padding: 0;
  flex-wrap: wrap;
}

.horizontal-list li {
  margin-right: 10px;
  margin-top: 20px;
}

.movie-detail {
  border-radius: 10px;
  background-color: #2F3138;
  cursor: pointer;
}

.tag-item {
  padding: 2px;
  display: inline;
  background-color: #3B3D44;
  font-size: 13px;
  color: #8E7944;
}

.actor-item {
  color: #818284;
  margin: 5px auto auto 4px;
  font-size: 14px;
  display: inline;
}

.tag-item:first-child {
  margin-left: 4px;
}

.container {
  position: relative;
}
</style>