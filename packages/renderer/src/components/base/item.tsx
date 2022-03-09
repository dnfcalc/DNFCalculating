import { defineComponent, h, renderSlot } from "vue"
import { itemProps, useSelectionItem } from "@/components/hooks/selection/item"

export default defineComponent({
  name: "i-item",
  props: itemProps,
  setup(props, { slots }) {
    const { itemClass, active, current } = useSelectionItem(props)

    function onClick() {
      if (!!active) {
        active.value = current.value
      }
    }
    return () => (
      <div onClick={onClick} class={itemClass.value}>
        {current.value.key ?? renderSlot(slots, "default")}
      </div>
    )
  }
})
