<script setup lang="ts">
import { ref } from "vue";

const randValue = ref("まだです");
const onButtonClick = (): void => {
  const rand = Math.round(Math.random() * 10);
  randValue.value = String(rand);
};

const mousePointerX = ref(0);
const mousePointerY = ref(0);
const onImgMouseMove = (event: MouseEvent): void => {
  mousePointerX.value = event.offsetX;
  mousePointerY.value = event.offsetY;
};

const pBgColor = ref("white");
const onPClick = (bgColor: string): void => {
  pBgColor.value = bgColor;
};

const pMsg = ref("イベント前（ここをクリック!）");
const pBgColorEvent = ref("white");
const onPClickWithEvent = (bgColor: string, event: MouseEvent): void => {
  pBgColorEvent.value = bgColor;
  pMsg.value = event.timeStamp.toString();
};

const msg = ref("未送信");
const onFormSubmit = (): void => {
  msg.value = "送信されました";
};

const msg1 = ref("まだです");
const onEnterKey = (): void => {
  msg1.value = "エンターキーが押下されました";
};
const onRightButtonClick = (): void => {
  msg1.value = "ボタンが右クリックされました";
};
const onShiftClick = (): void => {
  msg1.value = "シフトを押しながらクリックされました";
};
</script>

<template>
  <section>
    <button v-on:click="onButtonClick">クリック!</button>
    <!-- クリックの結果がランダムに表示される -->
    <p>クリックの結果: {{ randValue }}</p>
  </section>
  <section>
    <img
      src="../assets/logo.svg"
      alt="Vue のロゴ"
      width="200"
      v-on:mousemove="onImgMouseMove"
    />
    <p>ポインタの位置: x={{ mousePointerX }}; y={{ mousePointerY }}</p>
  </section>
  <section>
    <p
      v-on:click="onPClick('red')"
      v-bind:style="{ backgroundColor: pBgColor }"
    >
      ここをクリックすると背景色が変わります。
    </p>
  </section>
  <section>
    <!-- $event →イベントオブジェクトを引数として自動的に渡してくれるのは、引数を省力してメソッド名のみを記述した場合 -->
    <p
      v-on:click="onPClickWithEvent('green', $event)"
      v-bind:style="{ backgroundColor: pBgColorEvent }"
    >
      {{ pMsg }}
    </p>
  </section>
  <section>
    <form action="#" v-on:submit.prevent="onFormSubmit">
      <input type="text" required />
      <button type="submit">送信</button>
    </form>
    <p>{{ msg }}</p>
  </section>
  <section>
    <p>{{ msg1 }}</p>
    <input type="text" v-on:keydown.enter="onEnterKey"><br>
    <button v-on:click.right="onRightButtonClick">右クリック</button>
    <button v-on:click.shift="onShiftClick">シフトを押しながらクリック</button>
  </section>
</template>
