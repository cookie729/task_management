<script setup lang="ts">
import { computed, ref } from "vue";

const number = ref(80);
const showOrNot = computed((): boolean => {
  let showOrNot = false;
  const rand = Math.round(Math.random() * 100);
  if (rand >= 50) {
    showOrNot = true;
  }
  return showOrNot;
});

const randomNumber = computed((): number => {
  return Math.round(Math.random() * 100);
});
</script>

<template>
  <section>
    <p v-if="number >= 50">条件に合致したので表示⓵</p>
    <p v-if="Math.round(Math.random() * 100) >= 50">条件に合致したので表示⓶</p>
    <p v-if="showOrNot">条件に合致したので表示⓷</p>
  </section>
  <section>
    <p>
      点数は {{ randomNumber }} 点で
      <span v-if="randomNumber >= 80">優です</span>
      <span v-else-if="randomNumber >= 70">良です</span>
      <span v-else-if="randomNumber >= 60">可です</span>
      <span v-else>付可です</span>
    </p>
  </section>
  <section>
    <p>
      点数は {{ randomNumber }} 点で
      <template v-if="randomNumber >= 80">
        で優です
        <span style="color: red">素晴らしい</span>
      </template>
      <template v-else-if="randomNumber >= 70">
        で良です
        <span style="color: orange">すごい</span>
      </template>
      <template v-else-if="randomNumber >= 60">
        で可です
        <span style="color: blue">そこそこ</span>
      </template>
      <template v-else>
        で不可です
        <span style="color: gray">残念</span>
      </template>
    </p>
  </section>
  <section>
    v-if を利用
    <p v-if="showOrNot">条件に合致したので表示</p>
  </section>
  <section>
    v-show を利用
    <p v-show="showOrNot">条件に合致したので表示</p>
  </section>

  <!--  
    条件が一致しなかった場合の実行結果
    v-show は style があたり非表示になる
    <section>
      v-if を利用
      <!v-if>
    </section>
    <section>
      v-show を利用
      <p style="display: none;">条件に合致したので表示</p>
    </section>
  -->
</template>
