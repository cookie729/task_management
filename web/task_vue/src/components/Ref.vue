<script setup lang="ts">
import { ref, computed, reactive } from "vue";
const name = ref("田中太郎");

// 現在の日時を取得
const now = new Date();
// 現在の時刻の文字列を取得
const nowStr = now.toLocaleTimeString();
// 現在の時刻文字列をテンプレート変数として用意
let timeStr = nowStr;
// 同じく現在の時刻文字列をテンプレート変数として ref() で用意
const timeStrRef = ref(nowStr);
// 新しい時刻に変更する関数
function changeTime(): void {
  // 現在日時を取得
  const newTime = new Date();
  // 現在の時刻の文字列を取得
  const newTimeStr = newTime.toLocaleTimeString();
  // 現在の時刻の文字列をテンプレート変数 timeStr に格納
  timeStr = newTimeStr;
  // 現在の時刻文字列をテンプレート変数 timeStrRef に格納
  timeStrRef.value = newTimeStr;
}
// changeTime 関数を 1 秒ごとに実行
setInterval(changeTime, 1000);

// リアクティブなテンプレート変数をまとめて用意
const data = reactive({
  PI: 3.14,
  radius: Math.round(Math.random() * 10),
});
// 円の面積の算出プロパティを用意
const area = computed((): number => {
  return data.radius * data.radius * data.PI;
});
// 半径のテンプレート変数に新しい乱数を1秒ごとに格納
setInterval((): void => {
  data.radius = Math.round(Math.random() * 10);
}, 1000);
</script>

<template>
  <h1>こんにちは!{{ name }}さん!</h1>
  <p>現在時刻: {{ timeStr }}</p>
  <p>現在時刻(ref):{{ timeStrRef }}</p>
  <p>
    半径{{ data.radius }}の円の面積を円周率{{ data.PI }}で計算すると, {{ area }}
  </p>
  <p>{{ data.PI * data.radius * data.radius }}</p>
</template>