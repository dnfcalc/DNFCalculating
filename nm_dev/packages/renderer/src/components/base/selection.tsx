/**
 *  项 结合selection使用
 */

import { defineComponent, PropType, renderSlot } from "vue"

import { listProps, useSelectionList } from "@/components/hooks/selection/list"

export default defineComponent({
  name: "i-selection",
  props: {
    ...listProps
  },
  setup(props, context) {
    useSelectionList(props, context)
    const { slots } = context
    return () => {
      return <div>{renderSlot(slots, "default")}</div>
    }
  }
})
