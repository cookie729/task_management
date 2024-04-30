<!-- <script setup lang="ts">
import { ref } from "vue";
import Input from "./components/DynamicInput.vue";
import Radio from "./components/DynamicRadio.vue";
import Select from "./components/DynamicSelect.vue";

const currentComp = ref(Input);
const currentCompName = ref("Input");

const compList = [Input, Radio, Select];
const compNameList: string[] = ["Input", "Radio", "Select"];

let currentCompIndex = 0;
const switchComp = (): void => {
  currentCompIndex++;
  if (currentCompIndex >= 3) {
    currentCompIndex = 0;
  }
  currentComp.value = compList[currentCompIndex];
  currentCompName.value = compNameList[currentCompIndex];
};
</script>

<template>
  <p>コンポーネント名: {{ currentCompName }}</p>
  <KeepAlive>
    <component v-bind:is="currentComp" />
  </KeepAlive>
  <button v-on:click="switchComp">切り替え</button>
</template> -->

<script setup lang="ts">
import "uno.css";
const test = () => {
  console.log("1111");
};
</script>

<template lang="pug">
div.bg-black
  button(@click="test()") テスト
  p.bg-black こんにちは 
  p.text-blue こんにち
  p.text-red こんにち
  p.bg-red.text-white ｋｋｋｋｋ
    //- router-link(:to="{name:'taskadd'}").taskAddbox  ＋タスクを追加
</template>
<!-- <template>
  <div>
    <button @click="test()" テスト>
      <p class="bg-black">こんにちは</p>
      <p class="text-blue">こんにちは</p>
      <p class="bg-bink">こんにちは</p>
    </button>
  </div>
</template> -->

<style>
section {
  border: blue 1px solid;
  margin: 10px;
}
</style>
