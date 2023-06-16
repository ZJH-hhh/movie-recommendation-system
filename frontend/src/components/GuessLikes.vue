<template>
  <div class="example-pagination-block">
    <div class="example-demonstration"><el-button type="primary">Primary</el-button>
    <div class="movies">
      <ul class="horizontal-list">
        <li v-for="movie in filteredMovies.slice((currentPage - 1) * 12, currentPage * 12)" :key="movie.id"  @mouseenter="showMovieInfo(movie)" @mouseleave="hideMovieInfo()" style="height: 310px;width: 200px;">
          <el-menu v-if="movieInfo.show && movieInfo.movie === movie">
            <div class="movie-detail" @click="getMovieDetail(movie.id)" style="height: 330px; overflow: hidden; text-overflow: ellipsis;">
              <video autoplay controls width="200" style="border-radius: 8px 8px 0px 0px">
                <source :src=movie.trailer_url type="video/mp4">
              </video>
<!--              <div style="background-color: aqua;">-->
                <div style="font-size: 16px; font-weight: bolder; margin: auto auto 5px 4px; color: white">{{ movie.title }}</div>
                <ul class="tag-list">
                  <li v-for="tag in movie.tag_list" class="tag-item">{{ tag }}</li>
                </ul>
<!--                <div style="color: #818284; margin: 5px auto auto 4px; font-size: 14px;">演员</div>-->
                <ul class="actor-list">
                  <li v-for="actor in movie.actor_list.slice(0, 2)" class="actor-item">{{ actor }}</li>
                </ul>
                <div style="color: #818284; margin: 5px auto auto 4px; font-size: 14px;">{{ movie.introduction }}</div>
              </div>

<!--            </div>-->
          </el-menu>
          <div v-else>
            <div class="movie-container">
              <img :src=movie.image_url alt="" style="height: 270px;width: 186px; border-radius: 10px">
              <div style="font-size: 16px; font-weight: bolder; text-align: center">{{ movie.title }}</div>
            </div>
          </div>
      </li>
      </ul>
    </div>
    </div>
    <div :class="{ 'blur': movieDetailShow}"></div>
    <el-card class="box-card overlay-card" v-if="movieDetailShow && filteredMoviesID">
      <div class="card-container">
        <div class="title-img">
          <img
          :src=filteredMoviesID.image_url
          class="flex-item"
          />
          <div class="introduction-container">
            <span class="introduction"> {{ filteredMoviesID.introduction }}</span>
          </div>
          <el-button text style="font-size:30px; position: absolute; top: 10px; right: 10px" :icon="Close" @click="CloseDetails"/>
        </div>
        <el-button text style="font-size:30px" @click="toggleStore" :icon="StarFilled" :type="IsStore"/>
        <div class="comment-container">
          <span class="comment" v-for="comment in filteredMoviesID.comment_list">{{ comment }}</span>
        </div>
      </div>
    </el-card>
    <div class="background"></div>
    <el-pagination layout="prev, pager, next" :total="1000" @current-change="handleCurrentChange"/>
  </div>
</template>
<script setup>
import { ref, computed, onMounted, reactive } from 'vue';
import { useRouter } from 'vue-router';
import $ from 'jquery';
import { StarFilled, Close } from '@element-plus/icons-vue'


const selectedTags = ref([]);
const router = useRouter();
let movieDetailShow = ref(false);
const movies = reactive([]);
const currentPage = ref(1);
const movieId = ref()
const IsStore = ref('message')
onMounted(
    () => {
      $.ajax({
        url: 'http://8.130.99.147:8000/api/recommend/',
        success: response => {
          // console.log(response);
          response.data.forEach(element => {
            movies.push({
              id: element.fields.movie_id,
              title: element.fields.movie_title,
              actor_list: element.fields.actor_list,
              image_url: element.fields.img_url,
              tag_list: element.fields.movie_type_list,
              region: element.fields.movie_regions_list,
              movie_url: element.fields.movie_url,
              trailer_url: element.fields.trailer_url,
              comment_list: element.fields.comment_list,
              introduction: element.fields.introduction,
            })
          })
        }
      })
    }
)

const movieInfo = ref({
  show: false,
  movie: null,
});

const getMovieDetail = id => {
  // router.push(`/movies/${id}`);
  movieId.value = id
  movieDetailShow.value = !movieDetailShow.value;
  // movieDetailShow.value = true;
};
function CloseDetails(){
  movieDetailShow.value = !movieDetailShow.value
}
function toggleStore(){
  IsStore.value = IsStore.value === 'message' ? 'warning' : 'message';
}
const filteredMovies = computed(() => {
  if (selectedTags.value.length === 0) {
    return movies;
  }
  return movies.filter((movie) =>
          selectedTags.value.every((tag) => movie.tag_list.includes(tag))
  );
});
const filteredMoviesID = computed(() => {
  if (movieId.value) {
    return movies.find(movie => movie.id === movieId.value);
  }
  return null;
});

function showMovieInfo(movie) {
  movieInfo.value.movie = movie;
  movieInfo.value.show = true;
  // console.log(movieInfo.value.show, movieInfo.value.movie.id)
}
function  hideMovieInfo() {
  movieInfo.value.show = false;
  // console.log(movieInfo.value.show)
}
function handleCurrentChange(val) {
  currentPage.value = val
  console.log(currentPage.value)
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

.overlay-card {
  position: absolute;
  top: 250px;
  left: 200px;
  z-index: 9999;
  margin: 20px 20px 20px 200px;
  width: 650px;
  backdrop-filter: blur(10px); /* 调整模糊程度 */
  background-color: rgba(255, 255, 255, 0.5); /* 调整背景颜色和透明度 */
}

.title-img {
  display: flex;
  align-items: center;
}
.comment-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: left;
  text-align: left;
}

.comment {
  background-color: #f2f2f2;
  padding: 10px;
  margin: 10px;
  border-radius: 5px;
  font-size: 14px;
}
.introduction-container {
  margin-left: 20px;
}
.introduction {
  font-size: 14px;
  color: #333;
  margin-left: 50px;
}
.blur {
  backdrop-filter: blur(10px); /* 虚化效果 */
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* 背景颜色和透明度 */
  z-index: 0;
  transition: backdrop-filter 0.3s; /* 添加过渡效果 */
}

</style>
