<script setup lang="ts">
import { ref } from "vue";

const inputNameModel = ref("双方向");

const inputNameBind = ref("しんちゃん");
const inputNameOn = ref("名無し");
const onInputName = (event: Event): void => {
  const element = event.target as HTMLInputElement;
  inputNameOn.value = element.value;
};

const inputName2Way = ref("双方向");
const onInputName2Way = (event: Event): void => {
  const element = event.target as HTMLInputElement;
  inputName2Way.value = element.value;
};

const inputTextarea = ref("テキストエリアへの入力文字。\n 改行も加える");
const memberType = ref(1);
const memberTypeSelect = ref(1);
const isAgreed = ref(false);
const isAgreed01 = ref(0);
const selectedOS = ref([]);
const selectedOSSelect = ref([]);

const trimedText = ref("");
</script>

<template>
  <div>
    <section>
      <input type="text" v-model="inputNameModel" />
      <p>{{ inputNameModel }}</p>
    </section>
  </div>
  <div>
    <section>
      <input type="text" v-bind:value="inputNameBind" />
    </section>
    <br />
    <section>
      <input type="text" v-on:input="onInputName" />
      <p>{{ inputNameOn }}</p>
    </section>
  </div>
  <div>
    <section>
      <input
        type="text"
        v-bind:value="inputName2Way"
        v-on:input="onInputName2Way"
      />
      <p>{{ inputName2Way }}</p>
    </section>
  </div>
  <div>
    <textarea v-model="inputTextarea"></textarea>
    <p>{{ inputTextarea }}</p>
    <br />
    <section>
      <label>
        <input
          type="radio"
          name="memberType"
          value="1"
          v-model="memberType"
        />通常会員
      </label>
      <label>
        <input
          type="radio"
          name="memberType"
          value="2"
          v-model="memberType"
        />特別会員
      </label>
      <label>
        <input
          type="radio"
          name="memberType"
          value="3"
          v-model="memberType"
        />優良会員
      </label>
      <br />
      <p>選択されたラジオボタン: {{ memberType }}</p>
    </section>
    <br />
    <section>
      <select v-model="memberTypeSelect">
        <option value="1">通常会員</option>
        <option value="2">特別会員</option>
        <option value="3">優良会員</option>
      </select>
      <br />
      <p>選択されたリスト: {{ memberTypeSelect }}</p>
    </section>
    <br />
    <section>
      <label><input type="checkbox" v-model="isAgreed" />同意する</label>
      <p>同意の結果: {{ isAgreed }}</p>
    </section>
    <section>
      <label>
        <input
          type="checkbox"
          v-model="isAgreed01"
          true-value="1"
          false-value="0"
        />同意する
      </label>
      <p>同意の結果: {{ isAgreed01 }}</p>
    </section>
    <section>
      <label
        ><input type="checkbox" v-model="selectedOS" value="1" />macOS</label
      >
      <label>
        <input type="checkbox" v-model="selectedOS" value="2" />Windows
      </label>
      <label
        ><input type="checkbox" v-model="selectedOS" value="3" />Linux</label
      >
      <label><input type="checkbox" v-model="selectedOS" value="4" />iOS</label>
      <label>
        <input type="checkbox" v-model="selectedOS" value="5" />Android
      </label>
      <p>選択されたOS: {{ selectedOS }}</p>
    </section>
    <section>
      <select v-model="selectedOSSelect" multiple>
        <option value="1">macOS</option>
        <option value="2">Windows</option>
        <option value="3">Linux</option>
        <option value="4">iOS</option>
        <option value="5">Android</option>
      </select>
      <p>選択されたOS: {{ selectedOSSelect }}</p>
    </section>
  </div>
  <div>
    <section>
      <input type="text" v-model.trim="trimedText">
      <p>入力文字列: {{ trimedText }}</p>
    </section>
  </div>
</template>
