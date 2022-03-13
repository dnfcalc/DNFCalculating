import { builtinModules } from "module"
import { defineConfig, Plugin } from "vite"
import path from "path"
import vue from "@vitejs/plugin-vue"
import jsx from "@vitejs/plugin-vue-jsx"
import electron from "vite-plugin-electron-renderer"
import uncomponents from "unplugin-vue-components/vite"
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
      rules: [
        [
          /^col-(\d?\d)$/,
          ([, o]) => {
            let span = Number(o)
            const val = `${(span * 100) / 24}%`
            return {
              flex: `0 0 ${val}`
            }
          }
        ]
      ],

      presets: [presetUno(), presetIcons()]
    }),
    uncomponents({
      dts: true,
      dirs: ["src/components/"],
      allowOverrides: true,

      directoryAsNamespace: true
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
