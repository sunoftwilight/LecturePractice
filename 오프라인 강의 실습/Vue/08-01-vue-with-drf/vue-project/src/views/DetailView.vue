<template>
  <h1>Detail</h1>
  <div>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성 시간 : {{ article?.created_at }}</p>
    <p>수정 시간 : {{ article?.updated_at }}</p>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import router from '../router';

const route = useRoute()
const store = useCounterStore()

const article = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
  })
    .then((res) => {
      // console.log(res.data)
      article.value = res.data
      router.push({ name: 'DetailView', params: { id: res.data.id }})
    })
    .catch((err) => {
      console.log(err)
    })
})
</script>

<style>

</style>
