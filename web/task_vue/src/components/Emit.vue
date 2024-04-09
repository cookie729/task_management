<script setup lang="ts">
interface Props {
  rand: number;
}

// 1
interface Emits {
  // 2 event 又は e とすることが多い
  (event: "createNewRand"): void;
}

defineProps<Props>();
// 3
const emit = defineEmits<Emits>();

// 4
const onNewRandButtonClick = (): void => {
  // 5
  emit("createNewRand");
};
</script>

<template>
  <section class="box">
    <p>子コンポーネントで乱数を表示: {{ rand }}</p>
    <!-- 6 -->
    <button v-on:click="onNewRandButtonClick">新たな乱数を発生</button>
  </section>
</template>

<style scoped>
.box {
  border: green 1px solid;
  margin: 10px;
}
</style>
