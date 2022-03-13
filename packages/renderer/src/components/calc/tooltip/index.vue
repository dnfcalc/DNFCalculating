<script lang="tsx">
  /**
   * @Author: Kritsu
   * @Date:   2021/11/16 23:07:51
   * @Last Modified by:   Kritsu
   * @Last Modified time: 2021/11/17 18:49:42
   */

  import { NTooltip } from "@/components/base"

  import { tooltipProps } from "@/components/base/tooltip"

  import { defineComponent } from "vue"

  export default defineComponent({
    name: "i-tooltip",
    components: { NTooltip },
    props: {
      ...tooltipProps
    },
    setup(props, { slots, emit }) {
      return () => {
        return (
          <n-tooltip
            {...props}
            pop-class="i-popper z-999 fixed top-0 left-0 bg-black bg-opacity-80 border-1 border-hex-5b472a"
          >
            {slots}
          </n-tooltip>
        )
      }
    }
  })
</script>
<style lang="scss"></style>
