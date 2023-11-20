<template>
  <div>
    <h1>LogIn</h1>
    <form @submit.prevent="logIn">
      <label>Username : </label>
      <input type="text" v-model.trim="username"><br>
      <label>Password : </label>
      <input type="password" v-model.trim="password"><br>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}

</script>

<style>

</style>
