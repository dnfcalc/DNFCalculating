<script lang="tsx">
  // This starter template is using Vue 3 <script setup> SFCs
  // Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
  import { defineComponent, onMounted, Suspense } from "vue"
  import { useRoute, useRouter } from "vue-router"

  export default defineComponent(() => {
    const char = useRoute().params.name as string

    return () => (
      <div class="main">
        <div class="header">
          <calc-tabs>
            <calc-tab value="1" to={"/equipment/" + char}>
              装备
            </calc-tab>
            <calc-tab value="2" to={"/character/" + char}>
              技能
            </calc-tab>
          </calc-tabs>
        </div>
        <div class="center">
          <Suspense>
            <router-view></router-view>
          </Suspense>
        </div>
        <div class="footer">
          <div class="flex col-3 justify-center">
            <calc-button>全局重置</calc-button>
          </div>
          <div class="flex col-3 justify-center">
            <calc-button>开始计算</calc-button>
          </div>
        </div>
      </div>
    )
  })
</script>
<style lang="scss">
  .main {
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 100%;

    .header,
    .footer {
      flex: 1;
      height: 5%;
      max-height: 25px;
    }

    .footer {
      display: flex;
      align-items: center;
      justify-content: end;
    }

    .center {
      flex: 1;
      overflow-y: auto;
      overflow-x: hidden;
    }
  }
</style>
