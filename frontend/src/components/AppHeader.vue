<template>
  <el-header class="header" style="overflow: visible;">
    <el-menu mode="horizontal" router>
      <a href="/" class="logo" style="margin-top: auto; margin-bottom: auto; margin-right: 20px">
        <el-avatar style="margin-top: auto; margin-bottom: auto; margin-right: 20px" src='data:image/jpeg;base64,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' />
      </a>
      <el-menu-item index="/" class="title">黄哥说电影</el-menu-item>
      <el-sub-menu index="2" v-if="0">
        <template #title>Workspace</template>
      </el-sub-menu>
      <el-menu-item index="/MovieSearch">MovieSearch</el-menu-item>
      <el-menu-item index="/rank">高分榜</el-menu-item>
<!--      <el-menu-item>-->
<!--        <div>-->
<!--          <el-input type="text" v-model="input" @input="search"/>-->
<!--          <ul>-->
<!--            <li v-for="result in searchResults" :key="result.id">{{ result.name }}</li>-->
<!--          </ul>-->
<!--        </div>-->
<!--      </el-menu-item>-->
      <el-menu-item index="">
        <el-input v-model="movieName" class="w-50 m-2 search" placeholder="电影名"  style="margin-bottom: 0">
          <template #append>
            <el-icon class="el-input__icon" @click="getMovie"><Search /></el-icon>
          </template>
<!--          <ul>-->
<!--            <li v-for="result in searchResults" :key="result.id">{{ result.name }}</li>-->
<!--          </ul>-->
        </el-input>
      </el-menu-item>
      <el-menu-item v-if="!$store.state.user.is_login" style="margin-left: 400px;" @click="login">
        登陆/注册
      </el-menu-item>
      <el-popover placement="top-start" :width="200" v-else>
        <template #reference>
          <el-avatar style="margin: auto" src='https://upload.wikimedia.org/wikipedia/zh/thumb/e/ea/Shanks.JPG/420px-Shanks.JPG' />
        </template>
        <template #default>
          <div class="demo-rich-conent" style="display: flex; gap: 16px; flex-direction: column">
            <el-avatar :size="60" src='https://upload.wikimedia.org/wikipedia/zh/thumb/e/ea/Shanks.JPG/420px-Shanks.JPG' style="margin-bottom: 8px; margin: auto" />
          </div>
          <el-menu router>
            <el-menu-item  @click="getPersonal()" style="cursor: pointer">个人中心</el-menu-item>
            <el-menu-item @click="logout">退出登录</el-menu-item>
          </el-menu>
        </template>
      </el-popover>
    </el-menu>
  </el-header>
</template>

<script setup>
import { ref, watch, reactive } from 'vue';
import { Search } from '@element-plus/icons-vue';
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';
import $ from 'jquery';

const store = useStore();
const router = useRouter();
const movieName = ref('');
let is_login = ref(false);


const avatar = 'data:image/jpeg;base64,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';
const searchResults = ref([]);
const searchData = reactive([
      { id: 1, name: 'Apple' },
      { id: 2, name: 'Banana' },
      { id: 3, name: 'Orange' },
      { id: 4, name: 'Grapes' },
      { id: 5, name: 'Mango' },
    ]);
// const search = () => {
//       searchResults.value = searchData.filter((item) =>
//         item.name.toLowerCase().includes(input.value.toLowerCase())
//       );
//       console.log(input.value)
//       console.log(searchResults.value)
//     };
//
// watch(input, search);

const getPersonal = () => {
  console.log(store.state.user);
  router.push({ name: 'personal', params: {id: store.state.user.userid}});
}

const login = () => {
  router.push({ path: '/login'});
}

const logout = () => {
  store.dispatch('logout');
}

const getMovie = () => {
  $.ajax({
    url: 'http://8.130.99.147:8000/api/getmovie/',
    type: 'GET',
    data: {
      title: movieName.value,
    },
    success: response => {
      router.push({ name: 'search', params: {id: response.data[0].fields.movie_id}});
      // console.log(response);
    }
  });
}

</script>

<style scoped>
.title {
  font-size: 18px;
}

.search {
  margin-top: 12px;
}

.header {
   position: sticky;
  top: 0;
  background-color: #fff;
  z-index: 1;
}
</style>