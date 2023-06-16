<template>
  <div class="container">
    <meta name=referrer content=no-referrer>
    <div class="tags">
      <span
        v-for="tag in tags"
        :key="tag.id"
        :class="{ active: selectedTags.includes(tag.name) }"
        @click="toggleTag(tag.name)"
      >
        {{ tag.name }}
      </span>
    </div>

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
        <el-rate v-model="score" allow-half style="float: right" @click="assess" />
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
import { useStore } from 'vuex';
import { useRouter, useRoute } from 'vue-router';
import { StarFilled, Close } from '@element-plus/icons-vue'
import $ from 'jquery';
import { ElMessage } from 'element-plus';
import request from '@/utils/requests';

const store = useStore();
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
const selectedTags = ref([]);
const router = useRouter();
let movieDetailShow = ref(false);
const movies = reactive([]);
const storemovies = reactive([]);
const currentPage = ref(1);
const IsStore = ref('message')
const route = useRoute();
const movieid = route.params.id;
const movieId = ref();
let score = ref();

onMounted(
    () => {
      $.ajax({
        url: 'http://8.130.99.147:8000/api/get_all_data/',
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


      // console.log(movieid);
      if (movieid) {
        movieId.value = movieid;
        // filteredMoviesID();
        movieDetailShow.value = true;
      }
    }

)

const movieInfo = ref({
  show: false,
  movie: null,
});
const getMovieDetail = id => {
  // router.push(`/movies/${id}`);
  // console.log(id);
  movieId.value = id
  movieDetailShow.value = !movieDetailShow.value;
  console.log(movieId.value)
};
function CloseDetails(){
  movieDetailShow.value = !movieDetailShow.value;
  IsStore.value = 'message'
  score.value = 0;
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

function toggleTag(tagId) {
  if (selectedTags.value.includes(tagId)) {
    selectedTags.value = selectedTags.value.filter((name) => name !== tagId);
    // console.log(selectedTags);
  } else {
    selectedTags.value.push(tagId);
    // console.log(selectedTags);
  }
}

const assess = () => {
  if (!store.state.user.is_login) {
    ElMessage({
      message: '请先登录后再进行评分',
      type: 'warning',
    })
  } else {
    $.ajax({
      url: 'http://8.130.99.147:8000/api/assess/',
      type: 'POST',
      data: {
        movieid: movieId.value,
        score: score.value,
      },
      success: response => {
        if (response.result === 'success') {
          ElMessage({
            message: '评价成功',
            type: 'success',
          })
        } else {
          ElMessage({
            message: response.result,
            type: 'error',
          })
        }
      }
    })
    // console.log(movieId.value);
  }
  // console.log(score.value);
}
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
  // console.log(currentPage.value)
}
function toggleStore(){
  IsStore.value = IsStore.value === 'message' ? 'warning' : 'message';
  if (!store.state.user.is_login) {
    ElMessage({
      message: '请先登录后再收藏',
      type: 'warning',
    })
  }else {
    request({
        method: 'GET',
        url: 'api/storemovie?userid=' + store.state.user.userid + '&movieid=' + movieId.value
      }).then((res) => {
        if (res.data.data === 'success'){
          ElMessage({
            message: '收藏成功',
            type: 'success',
          })
          store.dispatch('update');
        }
      })
  }
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
  top: 0;
  left: 0;
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
