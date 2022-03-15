import { computed, defineComponent, ref, renderSlot, watch } from "vue"
import { switchProps, useSwitch } from "../hooks/swtich/swtich"

/**
 *  可以切换状态的开关
 */

export default defineComponent({
  name: "i-switch",
  props: {
    ...switchProps,
    onClickChecked: {
      type: Boolean,
      default: () => true
    }
  },

  setup(props, context) {
    const { slots } = context
    const { switchClass, toggle } = useSwitch(props, context)

    function click() {
      if (props.onClickChecked) {
        toggle()
      }
    }

    return () => (
      <div onClick={click} class={switchClass.value}>
        {renderSlot(slots, "default")}
      </div>
    )
  }
})
