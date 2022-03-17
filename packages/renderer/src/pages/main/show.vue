<script lang="tsx">
  import { defineComponent, ref } from "vue"
  import SkillPanel from "@/components/internal/skill/skill-panel.vue"

  export default defineComponent({
    components: { SkillPanel },
    setup() {
      const visible = ref(false)
      const showDialog = () => (visible.value = true)

      return () => (
        <div>
          <calc-tabs>
            <calc-tab value="1">套装</calc-tab>
            <calc-tab value="2">自选</calc-tab>
          </calc-tabs>
          <calc-button onClick={showDialog}>点击展开窗口</calc-button>
          <calc-button disabled>禁用</calc-button>

          <calc-checkbox>DYSB</calc-checkbox>
          <calc-select>
            <calc-option value={0}>123</calc-option>

            <calc-option value={1}>467</calc-option>
          </calc-select>
          <calc-dialog modal v-model:visible={visible.value}>
            测试
          </calc-dialog>
          <skill-panel></skill-panel>

          <div class="flex mx-12 py-12">
            <div class="flex col-6 justify-center">
              <calc-tooltip position="left">
                {{
                  default() {
                    return (
                      <img src="https://gitee.com/FeelingsCoder/picture-resource-station/raw/master/equipment/arms/swordman/sswd/192.png" />
                    )
                  },
                  popper() {
                    return (
                      <div class="h-20 text-white w-20">左侧Tooltip(默认)</div>
                    )
                  }
                }}
              </calc-tooltip>
            </div>

            <div class="flex col-6 justify-center">
              <calc-tooltip>
                {{
                  default() {
                    return (
                      <img src="https://gitee.com/FeelingsCoder/picture-resource-station/raw/master/equipment/arms/swordman/sswd/192.png" />
                    )
                  },
                  popper() {
                    return (
                      <div class="h-20 text-white w-20">下方ToolTip(默认)</div>
                    )
                  }
                }}
              </calc-tooltip>
            </div>

            <div class="flex col-6 justify-center">
              <calc-tooltip position="top">
                {{
                  default() {
                    return (
                      <img src="https://gitee.com/FeelingsCoder/picture-resource-station/raw/master/equipment/arms/swordman/sswd/192.png" />
                    )
                  },
                  popper() {
                    return <div class="h-20 text-white w-20">上方ToolTip</div>
                  }
                }}
              </calc-tooltip>
            </div>

            <div class="flex col-6 justify-center">
              <calc-tooltip position="right">
                {{
                  default() {
                    return (
                      <img src="https://gitee.com/FeelingsCoder/picture-resource-station/raw/master/equipment/arms/swordman/sswd/192.png" />
                    )
                  },
                  popper() {
                    return (
                      <div class="h-20 text-white w-20">右侧Tooltip(默认)</div>
                    )
                  }
                }}
              </calc-tooltip>
            </div>
          </div>
        </div>
      )
    }
  })
</script>
