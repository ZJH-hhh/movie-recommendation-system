<template>
  <el-row class="container">
    <el-col :span="6">
      <div class="personal-info">
        <el-avatar :size="60" src="https://upload.wikimedia.org/wikipedia/zh/thumb/e/ea/Shanks.JPG/420px-Shanks.JPG" style="margin-bottom: 8px; margin: auto" />
        <span class="username">{{ user.username }}</span>
        <div v-for="(item, index) in items" :key="index" class="psn-items" @click="getItem(item)">
          {{ item }}
        </div>
      </div>
    </el-col>
    <el-col :span="18">
      <personal-store :item="item_name" :key="item_name"/>
    </el-col>
  </el-row>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import $ from 'jquery';
import { reactive, onMounted, ref } from 'vue';
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
let item_name = ref('');
const items = reactive(['我的收藏', '我的评论']);

const getItem = item => {
  // console.log(item_name.value);
  item_name.value = item;
}

onMounted(() => {
  item_name.value = '我的收藏';
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
  // console.log(store.state.user.favor_movies);
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

.psn-items {
  /*padding-left: 10px;*/
  font-weight: bolder;
  font-size: 16px;
  /*background-color: #666666;*/
  cursor: pointer;
  padding: 5px 10px;
}

.psn-items:hover {
  color: #00CC4C;
}

</style>