<template>
  <el-row class="container">
    <el-col :span="8">
      <div class="personal-info">
        <el-avatar :size="60" src="https://upload.wikimedia.org/wikipedia/zh/thumb/e/ea/Shanks.JPG/420px-Shanks.JPG" style="margin-bottom: 8px; margin: auto" />
        <span class="username">{{ user.username }}</span>
        <div class="personal-collection">
          收藏
        </div>
      </div>
    </el-col>
    <el-col :span="16">
      <personal-store/>
    </el-col>
  </el-row>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import $ from 'jquery';
import { reactive, onMounted} from 'vue';
import PersonalStore from '@/views/PersonalStore.vue'

const store = useStore();
const route = useRoute();
const userid = route.params.id;
const user = reactive({
  username: '',
  photo: '',
  favor_tags: [],
  favor_movies: [],
})

onMounted(() => {
  console.log(userid);
  $.ajax({
    url: 'http://8.130.99.147:8000/api/getinfo/',
    type: 'GET',
    data: {
        user_id: userid,
    },
    headers: {
        "Authorization": "Bearer " + store.state.user.access,
    },
    success: response => {
        // console.log(response);
        user.username = response.username;
        user.photo = response.photo;
        user.favor_tags = response.favor_tags;
        user.favor_movies = response.favor_movies;
    }
  })
  console.log(store.state.user.favor_movies);
})
</script>

<style scoped>
.personal-info {
  margin-left: 100px;
}

.username {
  display: inline-block;
  height: 70px;
  /*align-items: center;*/
  vertical-align: middle;
  margin-left: 10px;
  font-size: 16px;
  font-weight: bolder;
}



</style>