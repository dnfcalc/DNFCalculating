<script lang="tsx">
  // This starter template is using Vue 3 <script setup> SFCs
  // Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
  import { defineComponent, Suspense } from "vue"
  import { useAppStore } from "./store/app"

  export default defineComponent({
    setup() {
      const appStore = useAppStore()

      return () => (
        <>
          <div
            class="bg-hex bg-gradient-to-t flex from-hex-273e69 to-hex-335793 h-6 px-2 top-0 right-0 left-0  leading-6 z-9999 app-title layout-title items-center justify-between fixed"
            style="-webkit-app-region: drag"
          >
            <img src="/favicon.ico" class="h-4 leading-4 w-4" />
            <div class="text-white text-xs">{appStore.title}</div>
            <div class="flex items-center">
              <div
                onClick={appStore.minimize}
                class="cursor-pointer min-icon h-4  text-center mr-4 text-hex-f0d070 text-opacity-72 w-4 hover:text-opacity-100"
              ></div>
              <div
                onClick={appStore.close}
                class="cursor-pointer h-4 text-center  text-hex-f0d070 text-opacity-72  w-4 close-icon hover:text-opacity-100"
              ></div>
            </div>
          </div>
          <div class="h-full w-full pt-6 overflow-y-auto">
            <Suspense>
              <router-view></router-view>
            </Suspense>
          </div>
        </>
      )
    }
  })
</script>

<style>
  html {
    cursor: url("@/assets/img/cursor.png"), auto;
    cursor: url("@/assets/img/cursor.png"), default;
  }
</style>

<style scoped>
  .app {
    height: 100%;
  }

  .app-title {
    -webkit-app-region: drag;
  }

  .min-icon {
    -webkit-app-region: no-drag;
    background: url("@/assets/img/min.png") no-repeat;

    background-size: 10px 9px;
    background-position: center;
  }

  .close-icon {
    -webkit-app-region: no-drag;
    background: url("@/assets/img/exit.png") no-repeat;
    background-size: 10px 9px;
    background-position: center;
  }
</style>
