<template>
  <div>
    <el-input type="text" v-model="searchKeyword" @input="search"/>
    <ul>
      <li v-for="result in searchResults" :key="result.id">{{ result.name }}</li>
    </ul>
  </div>
</template>

<script>
import { ref, reactive, watch } from 'vue';

export default {
  setup() {
    const searchKeyword = ref('');
    const searchData = reactive([
      { id: 1, name: 'Apple' },
      { id: 2, name: 'Banana' },
      { id: 3, name: 'Orange' },
      { id: 4, name: 'Grapes' },
      { id: 5, name: 'Mango' },
    ]);
    const searchResults = ref([]);

    const search = () => {
      searchResults.value = searchData.filter((item) =>
        item.name.toLowerCase().includes(searchKeyword.value.toLowerCase())
      );
    };

    watch(searchKeyword, search);

    return {
      searchKeyword,
      searchResults,
    };
  },
};
</script>
