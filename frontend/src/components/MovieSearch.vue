<template>
  <div>
    <meta name=referrer content=no-referrer>
    <div class="tags">
      <span
        v-for="tag in tags"
        :key="tag.id"
        :class="{ active: selectedTags.includes(tag.id) }"
        @click="toggleTag(tag.id)"
      >
        {{ tag.name }}
      </span>
    </div>

    <div class="movies">
      <ul class="horizontal-list">
        <li v-for="movie in filteredMovies" :key="movie.id"  @mouseenter="showMovieInfo(movie)" @mouseleave="hideMovieInfo()" style="height: 310px;width: 200px;">
          <el-menu v-if="movieInfo.show && movieInfo.movie === movie">
            <div class="movie-detail">
              <video autoplay controls width="200" style="border-radius: 8px 8px 0px 0px">
                <source src="https://vt1.doubanio.com/202306081433/fb54117ebb1c932d9b9829c3f955b1a2/view/movie/M/402590258.mp4" type="video/mp4">
              </video>
<!--              <div style="background-color: aqua;">-->
                <div style="font-size: 16px; font-weight: bolder; margin: auto auto 5px 4px; color: white">电影名</div>
                <ul class="tag-list">
                  <li class="tag-item">剧情</li>
                  <li class="tag-item">犯罪</li>
                </ul>
                <div style="color: #818284; margin: 5px auto auto 4px; font-size: 14px;">演员</div>
                <div style="color: #818284; margin: 5px auto auto 4px; font-size: 14px;">简介</div>
              </div>

<!--            </div>-->
          </el-menu>
          <div v-else>
            <div class="movie-container">
              <a :href="'/movies/' + movie.id"><img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg" alt=""
                                                    style="height: 270px;width: 186px; border-radius: 10px"></a>
            </div>
            <div>{{ movie.title }}</div>
          </div>
      </li>
      </ul>
    </div>
  </div>
</template>
<script setup>
import { ref,computed } from 'vue';
const tags = ref([
  { id: 1, name: '动作' },
  { id: 2, name: '喜剧' },
  { id: 3, name: '剧情' },
  // 其他标签...
]);
const selectedTags = ref([]);
const movies = ref([
  { id: 1, title: '电影A', tags: [1, 2] },
  { id: 2, title: '电影B', tags: [2, 3] },
  { id: 3, title: '电影C', tags: [1, 3] },
  { id: 4, title: '电影D', tags: [1, 2, 3] },
  { id: 5, title: '电影E', tags: [1, 2] },
  { id: 6, title: '电影F', tags: [1, 2, 3] },
  { id: 7, title: '电影G', tags: [1] },
  { id: 8, title: '电影H', tags: [2] },
  { id: 9, title: '电影I', tags: [3] },
]);

const movieInfo = ref({
  show: false,
  movie: null,
});

const filteredMovies = computed(() => {
  if (selectedTags.value.length === 0) {
    return movies.value;
  }
  return movies.value.filter((movie) =>
          selectedTags.value.every((tag) => movie.tags.includes(tag))
  );
});

function toggleTag(tagId) {
  if (selectedTags.value.includes(tagId)) {
    selectedTags.value = selectedTags.value.filter((id) => id !== tagId);
  } else {
    selectedTags.value.push(tagId);
  }
}

function showMovieInfo(movie) {
  movieInfo.value.movie = movie;
  movieInfo.value.show = true;
  console.log(movieInfo.value.show, movieInfo.value.movie.id)
}
function  hideMovieInfo() {
  movieInfo.value.show = false;
  console.log(movieInfo.value.show)
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
}

.tag-item {
  padding: 2px;
  display: inline;
  background-color: #3B3D44;
  font-size: 13px;
  color: #8E7944;
}

.tag-item:first-child {
  margin-left: 4px;
}
</style>
