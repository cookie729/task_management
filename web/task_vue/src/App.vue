<script setup lang="ts">
import Ref from "./components/Ref.vue";
import Bind from "./components/VBind.vue";
import On from "./components/VOn.vue";
import Model from "./components/VModel.vue";
import If from "./components/VIf.vue";
import For from "./components/VFor.vue";
import Watch from "./components/Watcher.vue";
import LifeCycle from "./components/LifeCycle.vue";
import ReactiveFunc from "./components/ReactiveFunc.vue";
import OneSection from "./components/OneSection.vue";
import WithModel from "./components/WithModel.vue";
import OneInfo from "./components/OneInfo.vue";
import { ref, computed } from "vue";
import OneMember from "./components/OneMember.vue";

// const propsTitle = ref("発生した乱数");
// const rand = Math.round(Math.random() * 100);
// const propsContent = ref(rand);

// const weatherListInit = new Map<number, Weather>();
// weatherListInit.set(1, {
//   id: 1,
//   title: "今日の天気",
//   content: "今は1日中、晴れでしょう",
// });
// weatherListInit.set(2, {
//   id: 2,
//   title: "明日の天気",
//   content: "明日は1日中、雨でしょう",
// });
// weatherListInit.set(3, {
//   id: 3,
//   title: "明後日の天気",
//   content: "明後日は1日中、雪でしょう",
// });
// const weatherList = ref(weatherListInit);

// interface Weather {
//   id: number;
//   title: string;
//   content: string;
// }

const memberListInit = new Map<number, Member>();
memberListInit.set(33456, {
  id: 33456,
  name: "田中太郎",
  email: "bow@example.com",
  points: 35,
  note: "初回入会特典あり",
});
memberListInit.set(47783, {
  id: 33456,
  name: "鈴木次郎",
  email: "mue@example.com",
  points: 54,
});

const memberList = ref(memberListInit);
const totalPoints = computed((): number => {
  let total = 0;
  for (const member of memberList.value.values()) {
    total += member.points;
  }
  return total;
});

interface Member {
  id: number;
  name: string;
  email: string;
  points: number;
  note?: string;
}
</script>

<template>
  <!-- <h1>コンポーネント基礎</h1>
  <section>
    <h2>コンポーネント1個</h2>
    <OneSection />
  </section>
  <section>
    <h2>コンポーネントが複数</h2>
    <OneSection />
    <OneSection />
    <OneSection />
  </section>
  <section>
    <h1>コンポーネントの独立性</h1>
    <h2>v-model を含むコンポーネント</h2>
    <WithModel />
    <WithModel />
  </section> -->
  <!-- <Ref /> -->
  <!-- <Bind /> -->
  <!-- <On /> -->
  <!-- <Model /> -->
  <!-- <If /> -->
  <!-- <For /> -->
  <!-- <Watch /> -->
  <!-- <LifeCycle /> -->
  <!-- <ReactiveFunc /> -->
  <!-- <h1>Props 基礎</h1>
  <section>
    <h2>ループでコンポーネントを生成</h2>
    <OneInfo v-for="[id, weather] in weatherList" 
      v-bind:key="id"
      v-bind:title="weather.title"
      v-bind:content="weather.content"
    />
  </section> -->

  <section>
    <h1>会員リスト</h1>
    <p>全会員の保有ポイントの合計: {{ totalPoints }}</p>
    <OneMember
      v-for="[id, member] in memberList"
      v-bind:key="id"
      v-bind:id="id"
      v-bind:name="member.name"
      v-bind:email="member.email"
      v-bind:points="member.points"
      v-bind:note="member.note"
    />
  </section>
</template>

<style>
section {
  border: blue 1px solid;
  margin: 10px;
}
</style>
