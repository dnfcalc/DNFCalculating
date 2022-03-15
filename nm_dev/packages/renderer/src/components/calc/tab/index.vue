<script lang="tsx">
  /**
   * @Author: Kritsu
   * @Date:   2021/11/16 18:33:00
   * @Last Modified by:   Kritsu
   * @Last Modified time: 2021/11/17 18:49:21
   */
  import { defineComponent, h, renderSlot } from "vue"
  import NItem from "@/components/base/item"
  import { itemProps } from "@/components/hooks/selection/item"

  export default defineComponent({
    name: "calc-tab",
    props: {
      ...itemProps,
      width: { type: [Number, String], default: () => 120 },
      to: { type: String }
    },
    components: { NItem },
    setup(props, { slots }) {
      return () => {
        const style = {
          width: `${props.width ?? 120}px`
        }

        const defaults = (
          <n-item {...props} style={style}>
            {renderSlot(slots, "default")}
          </n-item>
        )

        if (!!props.to) {
          return <router-link to={props.to}>{defaults}</router-link>
        }
        return defaults
      }
    }
  })
</script>
