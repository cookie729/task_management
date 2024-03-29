<script setup lang="ts">
import { ref, computed } from "vue";

// ⓶
const cocktailListInit: string[] = ["カクテル1", "カクテル2", "カクテル3"];
// ⓶
const cocktailList = ref(cocktailListInit);

const cocktailListInitKey: { [key: number]: string } = {
  2345: "カクテル1",
  4412: "カクテル2",
  6792: "カクテル3",
};
const cocktailListKey = ref(cocktailListInitKey);

// Map を使うには new して set する
// ⓷
const cocktailListInitMap = new Map<number, string>();
cocktailListInitMap.set(2345, "カクテル1");
cocktailListInitMap.set(4412, "カクテル2");
cocktailListInitMap.set(6792, "カクテル3");
const cocktailListMap = ref(cocktailListInitMap);

// ⓸
const whiteLadyInit: {
  id: number;
  name: string;
  price: number;
  recipe: string;
} = {
  id: 2345,
  name: "ホワイトレディ",
  price: 1200,
  recipe: "ジン 30ml+コワントロー 15ml + レモン + 15ml",
};
// ⓸
const whiteLady = ref(whiteLadyInit);

// ⓵
const cocktailDataListInitObj: Cocktail[] = [
  { id: 2345, name: "カクテル1", price: 1200 },
  { id: 4412, name: "カクテル2", price: 1500 },
  { id: 6792, name: "カクテル3", price: 1100 },
  { id: 8429, name: "カクテル4", price: 1500 },
];
const cocktailDataList = ref(cocktailDataListInitObj);
interface Cocktail {
  id: number;
  name: string;
  price: number;
}

// ⓹
const cocktailDataListInitMapObj = new Map<number, Cocktail>();
cocktailDataListInitMapObj.set(2345, {
  id: 2345,
  name: "カクテル1",
  price: 1200,
});
cocktailDataListInitMapObj.set(4412, {
  id: 4412,
  name: "カクテル2",
  price: 1500,
});
cocktailDataListInitMapObj.set(6792, {
  id: 6792,
  name: "カクテル3",
  price: 1100,
});
cocktailDataListInitMapObj.set(8429, {
  id: 8429,
  name: "カクテル4",
  price: 1500,
});
// ⓹
const cocktailDataListMapObj = ref(cocktailDataListInitMapObj);

// ⓵より
const cocktail1500 = computed((): Cocktail[] => {
  const newList = cocktailDataList.value.filter(
    (cocktailItem: Cocktail): boolean => {
      return cocktailItem.price == 1500;
    }
  );
  return newList;
});

// ⓶より
const changeCocktailList = (): void => {
  cocktailList.value = ["バラライカ", "XYZ", "マンハッタン"];
};
const addCocktailList = (): void => {
  cocktailList.value.push("ブルームーン");
};
const deleteCocktailList = (): void => {
  cocktailList.value.pop();
};

// ⓷より
const changeCocktailListMap = (): void => {
  cocktailListMap.value.clear();
  cocktailListMap.value.set(3416, "バラライカ");
  cocktailListMap.value.set(5517, "XYZ");
  cocktailListMap.value.set(7415, "マンハッタン");
};
const addCocktailListMap = (): void => {
  cocktailListMap.value.set(8894, "ブルームーン");
};
const deleteFromCocktailListMap = (): void => {
  cocktailListMap.value.delete(5517);
};

// ⓸より
const changeWhiteLadyPrice = (): void => {
  whiteLady.value.price = 1500;
};

// ⓹より
const cocktail1500MapObj = computed((): Map<number, Cocktail> => {
  const newList = new Map<number, Cocktail>();
  cocktailDataListMapObj.value.forEach((value: Cocktail, key: number): void => {
    if (value.price == 1500) {
      newList.set(key, value);
    }
  });
  return newList;
});
const changeWhiteLadyPriceInList = (): void => {
  const whiteLady = cocktailDataListMapObj.value.get(2345) as Cocktail;
  whiteLady.price = 1500;
};
</script>

<template>
  <section>
    <ul>
      <li v-for="cocktailName in cocktailList" v-bind:key="cocktailName">
        {{ cocktailName }}
      </li>
    </ul>
    <ul>
      <li
        v-for="(cocktailName, index) in cocktailList"
        v-bind:key="cocktailName"
      >
        {{ cocktailName }}(インデックス{{ index }})
      </li>
    </ul>
  </section>
  <section>
    <ul>
      <li
        v-for="(cocktailName, id) in cocktailListKey"
        v-bind:key="'cocktailListKey' + id"
      >
        ID が {{ id }} のカクテルは {{ cocktailName }}
      </li>
    </ul>
    <ul>
      <li
        v-for="(cocktailName, id, index) in cocktailListKey"
        v-bind:key="'cocktailListKeyWithIdx' + id"
      >
        {{ index + 1 }}: ID が {{ id }} のカクテルは {{ cocktailName }}
      </li>
    </ul>
  </section>
  <!-- Map -->
  <section>
    <ul>
      <li v-for="[id, cocktailName] in cocktailListMap" v-bind:key="id">
        ID が {{ id }} のカクテルは {{ cocktailName }}
      </li>
    </ul>
  </section>
  <!-- WhiteLady -->
  <section>
    <dl>
      <!-- 複数のタグを繰り返すには template タグ -->
      <template v-for="(value, key) in whiteLady" v-bind="key">
        <dt>{{ key }}</dt>
        <dd>{{ value }}</dd>
      </template>
    </dl>
  </section>
  <section>
    <ul>
      <li v-for="cocktailItem in cocktailDataList" v-bind:key="cocktailItem.id">
        {{ cocktailItem.name }} の値段は {{ cocktailItem.price }}円
      </li>
    </ul>
  </section>
  <!-- MapObj -->
  <section>
    <ul>
      <li v-for="[id, cocktailItem] in cocktailDataListMapObj" v-bind:key="id">
        {{ cocktailItem.name }} の値段は {{ cocktailItem.price }} 円
      </li>
    </ul>
  </section>
  <section>
    <ul>
      <li v-for="r in 5" v-bind:key="r">
        半径 {{ r }} の円の円周: {{ 2 * r * 3.14 }}
      </li>
    </ul>
  </section>
  <section>
    全てのカクテルリスト
    <ul>
      <li v-for="cocktailItem in cocktailDataList" v-bind:key="cocktailItem.id">
        {{ cocktailItem.name }} の値段は {{ cocktailItem.price }}円
      </li>
    </ul>
  </section>
  <section>
    1500 円のカクテルリスト
    <ul>
      <li
        v-for="cocktailItem in cocktail1500"
        v-bind:key="'cocktail1500' + cocktailItem.id"
      >
        {{ cocktailItem.name }} の値段は {{ cocktailItem.price }}円
      </li>
    </ul>
  </section>
  <section>
    <ul>
      <li
        v-for="(cocktailName, index) in cocktailList"
        v-bind:key="cocktailName"
      >
        {{ cocktailName }}(インデックス{{ index }})
      </li>
    </ul>
    <p>
      CocktailListを
      <button v-on:click="changeCocktailList">変更</button>
    </p>
    <p>
      CocktailList から末尾の要素に「ブルームーン」を
      <button v-on:click="addCocktailList">追加</button>
    </p>
    <p>
      CocktailList から末尾の要素を
      <button v-on:click="deleteCocktailList">削除</button>
    </p>
  </section>
  <section>
    <ul>
      <li v-for="[id, cocktailName] in cocktailListMap" v-bind:key="id">
        ID が {{ id }} のカクテルは {{ cocktailName }}
      </li>
    </ul>
    <p>
      CocktailListを
      <button v-on:click="changeCocktailListMap">変更</button>
    </p>
    <p>
      CocktailList から末尾の要素に「ブルームーン」を
      <button v-on:click="addCocktailListMap">追加</button>
    </p>
    <p>
      CocktailList から末尾の要素を
      <button v-on:click="deleteFromCocktailListMap">削除</button>
    </p>
  </section>
  <section>
    <dl>
      <template v-for="(value, key) in whiteLady" v-bind="key">
        <dt>{{ key }}</dt>
        <dd>{{ value }}</dd>
      </template>
    </dl>
    <p>
      価格を 1500 円に
      <button v-on:click="changeWhiteLadyPrice">変更</button>
    </p>
  </section>
  <section>
    すべてのカクテルリスト
    <ul>
      <li v-for="[id, cocktailItem] in cocktailDataListMapObj" v-bind:key="id">
        {{ cocktailItem.name }} の値段は {{ cocktailItem.price }} 円
      </li>
    </ul>
  </section>
  <section>
    値段が 1500 円のカクテルリスト
    <ul>
      <li
        v-for="[id, cocktailItem] in cocktail1500MapObj"
        v-bind:key="'cocktail1500MapObj' + id"
      >
        {{ cocktailItem.name }} の値段は {{ cocktailItem.price }}
      </li>
    </ul>
    <p>
      CocktailDataList 内のホワイトレディの価格を 1500 円に
      <button v-on:click="changeWhiteLadyPriceInList">変更</button>
    </p>
  </section>
</template>
