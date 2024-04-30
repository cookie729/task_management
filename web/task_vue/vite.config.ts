import { fileURLToPath, URL } from "node:url";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import UnoCSS from "unocss/vite";
import presetUno from "@unocss/preset-uno";
import extractorPug from '@unocss/extractor-pug'

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    host: true,
  },

  plugins: [
    vue(),
    UnoCSS({
      presets: [presetUno()],
      include: [
        "./index.html",
        "./src/**/*.{vue,js,ts,jsx,tsx}",
        "./node_modules/primevue/**/*.{vue,js,ts,jsx,tsx}",
      ],
      extractors: [
        extractorPug(),
      ],
    }),
  ],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
});
