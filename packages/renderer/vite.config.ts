import { builtinModules } from "module"
import { defineConfig, Plugin } from "vite"
import path from "path"
import vue from "@vitejs/plugin-vue"
import jsx from "@vitejs/plugin-vue-jsx"
import electron from "vite-plugin-electron-renderer"
import pkg from "../../package.json"
import unocss from "unocss/vite"

import { presetUno, presetIcons } from "unocss"

// https://vitejs.dev/config/
export default defineConfig({
  mode: process.env.NODE_ENV,
  root: __dirname,
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src")
    }
  },
  plugins: [
    unocss({
      presets: [presetUno(), presetIcons()]
    }),
    jsx(),
    vue(),
    electron()
  ],

  optimizeDeps: {
    exclude: ["electron"]
  },
  base: "./",
  build: {
    assetsDir: ".",
    emptyOutDir: true
  },
  server: {
    port: pkg.env.PORT
  }
})
