<script setup lang="ts">
import { ref } from "vue";

const name = ref("たろう")
</script>


<template>
  <section>
    <p>{{ name }}さんですねっ</p>
    <iuput type="text" v-model="name" />
  </section>
</template>

<style scoped>
section {
  border: orange  1px dashed;
  margin: 10px;
}
</style>  

