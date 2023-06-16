<template>
  <div class="personal-collection" v-if="check()">
    <div class="movies">
      <ul class="horizontal-list">
        <li v-for="movie in movies" :key="movie.id" style="height: 310px;width: 200px;">
          <div>
            <div class="movie-container" @click="getMovieDetail(movie.id)">
              <img :src=movie.image_url alt="" style="height: 270px;width: 186px; border-radius: 10px">
              <div style="font-size: 16px; font-weight: bolder; text-align: center">{{ movie.title }}</div>
              <el-button text style="font-size:30px" @click="getMovieDetail(movie.id);toggleStore();" :icon="StarFilled" :type="IsStore"/>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
  <div class="personal-collection" v-else>
    <div class="movies">
      <ul>
        <li v-for="movie in movies" :key="movie.id" >
          <el-card style="margin-bottom: 5px;">
            <el-row>
              <el-col :span="3">
                <img :src=movie.image_url alt="" style="height: 200px;width: 138px; border-radius: 10px">
                <div style="font-size: 16px; font-weight: bolder; text-align: center">{{ movie.title }}</div>
              </el-col>
              <el-rol :span="21" style="padding-left: 20px;">
                {{ movie.content }}
              </el-rol>
            </el-row>
          </el-card>
        </li>
      </ul>
    </div>
  </div>
</template>
<script>
import {onMounted, reactive, ref} from "vue";
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import $ from 'jquery';
import request from '@/utils/requests';
import { StarFilled } from '@element-plus/icons-vue';
import { ElMessage } from 'element-plus';
export default {
  name: 'PersonalStore',
  props: ['item'],
  setup(props) {
    const store = useStore();
    const route = useRoute();
    const movies = reactive([])
    const movieId = ref()
    const IsStore = ref('warning');
    // console.log(props);

    onMounted(() =>{
      // props.item = '我的收藏';
      // console.log(store.state.user.userid)
      // console.log(store.state.user.favor_movies)
      if (!store.state.user.is_login) {
        console.log(1)
      } else {
          // console.log(props.item);
        if (props.item) {
          getMovies(props.item);
        } else {
          getMovies('我的收藏');
        }
      }
    })

    const check = () => {
      return props.item === '我的收藏';
    }

      const getMovies = method => {
        // console.log(method);
        if (method === '我的收藏') {
          $.ajax({
            url: 'http://8.130.99.147:8000/api/personalmovie/',
            type: 'GET',
            data: {
              userid: store.state.user.userid,
              method: method,
            },
            success: response => {
              console.log(response);
              // console.log(response);
              // movies.value = {};
              movies.splice(0, movies.length);
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
        } else if (method == '我的评论') {
          $.ajax({
            url: 'http://8.130.99.147:8000/api/personalmovie/',
            type: 'GET',
            data: {
              userid: store.state.user.userid,
              method: method,
            },
            success: response => {
              console.log(response);
              // console.log(response);
              // movies.value = {};
              movies.splice(0, movies.length);
              // console.log(response);
              response.data.forEach(element => {
                movies.push({
                  id: element.movieid,
                  title: element.movie_title,
                  image_url: element.movie_photo,
                  content: element.content
                })
              })
            }
          })
        }
      }

      const getMovieDetail = id => {
        movieId.value = id
        // console.log(movieId.value)
      };

      function toggleStore(){
        // IsStore.value = IsStore.value === 'message' ? 'warning' : 'message';
        if (!store.state.user.is_login) {
          ElMessage({
            message: '请先登录后再取消收藏',
            type: 'warning',
          })
        }else {
          request({
              method: 'GET',
              url: 'api/unstoremovie?userid=' + store.state.user.userid + '&movieid=' + movieId.value
            }).then((res) => {
              if (res.data.data === 'success'){
                ElMessage({
                  message: '取消收藏成功',
                  type: 'success',
                })
                IsStore.value = 'warning'
                // store.dispatch('update');
              }
              getMovies(props.item);
            })
        }
    }

    return {
      movies,
      movieId,
      IsStore,
      getMovies,
      getMovieDetail,
      toggleStore,
      StarFilled,
      check,
    }
  }
}


</script>
<style scoped>
.personal-collection {
  /*padding-left: 10px;*/
  font-weight: bolder;
  font-size: 16px;
  /*background-color: #666666;*/
  /*cursor: pointer;*/
}

/*.personal-collection:hover {*/
/*  color: #00DC5A;*/
/*}*/

.movies {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  grid-gap: 16px;
  /*margin-left: 100px;*/
  /*background-color: #666666;*/
}

.movie-container {
  width: 186px;
  height: 303px;
  cursor: pointer;
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
</style>