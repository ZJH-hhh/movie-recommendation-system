<template>
  <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <span>Card name</span>
        <el-button class="button" text>Operation button</el-button>
      </div>
    </template>
    <div v-for="o in 4" :key="o" class="text item">{{ 'List item ' + o }}</div>
  </el-card>
</template>

<script setup>
import { useRoute } from 'vue-router';
import $ from 'jquery';
import { reactive, onMounted } from 'vue'
const route = useRoute();
const movieId = route.params.id
const movies = reactive([]);
console.log(movieId)

onMounted(
    () => {
      $.ajax({
        url: 'http://8.130.99.147:8000/api/get_data_by_id?id=' + movieId,
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
      console.log((movies))
    }
)
</script>

<style scoped>
. container {
  display: flex;
}

li {
  display: flex;
}
</style>