<script setup lang="ts">
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
</template>

<style>
section {
  border: blue 1px solid;
  margin: 10px;
}
</style>
