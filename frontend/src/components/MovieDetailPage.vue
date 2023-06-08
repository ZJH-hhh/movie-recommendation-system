<template>
  <h1>{{ movieId }}</h1>
</template>
<script setup>
  import { useRoute } from 'vue-router';
  const route = useRoute();
  const movieId = route.params.id
  console.log(movieId)
</script>
<style></style>