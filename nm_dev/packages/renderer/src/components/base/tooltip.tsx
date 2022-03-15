/**
 * @Author: Kritsu
 * @Date:   2021/11/16 23:07:51
 * @Last Modified by:   Kritsu
 * @Last Modified time: 2021/11/17 18:49:42
 */
import {
  watch,
  defineComponent,
  renderSlot,
  Teleport,
  ref,
  computed,
  CSSProperties,
  Transition,
  PropType,
  reactive
} from "vue"

export const tooltipProps = {
  popClass: {
    type: String
  },
  position: {
    type: String as PropType<"bottom" | "top" | "left" | "right">,
    default: () => "bottom"
  },
  offset: {
    type: Number,
    default: () => 4
  }
}

export default defineComponent({
  name: "i-tooltip",
  emits: ["change"],
  props: tooltipProps,
  setup(props, { slots, emit }) {
    const isOpen = ref(false)

    const triggerRef = ref<Element>()
    const popupRef = ref<Element>()

    const dropdownPosition = reactive({ x: 0, y: 0 })
    const dropdownStyle = computed<CSSProperties>(() => {
      return {
        left: `${dropdownPosition.x}px`,
        top: `${dropdownPosition.y}px`,
        visibility: isOpen.value ? "visible" : "hidden"
      }
    })

    function onMouseover() {
      isOpen.value = true

      const trigger = triggerRef.value
      const popup = popupRef.value

      if (!!trigger && !!popup) {
        const { width, height, left, top } = trigger.getBoundingClientRect()

        const { clientWidth: pWidth, clientHeight: pHeight } = popup

        console.log(pWidth, pHeight)

        let x = 0
        let y = 0

        const offset = props.offset
        switch (props.position) {
          case "bottom":
            x = left
            y = top + height + offset
            break
          case "top":
            x = left
            y = top - pHeight - offset
            break
          case "left":
            x = left - pWidth - offset
            y = top
            break
          case "right":
            x = left + width + offset
            y = top
            break
        }
        dropdownPosition.x = x
        dropdownPosition.y = y
      }
    }

    function onMouseout() {
      isOpen.value = false
    }

    watch(isOpen, () => emit("change", isOpen.value))
    return () => {
      return (
        <div {...{ onMouseout, onMouseover }} ref={triggerRef}>
          {renderSlot(slots, "default")}
          <Teleport to="body">
            <Transition name="dropdown" mode="out-in">
              <div
                class={["i-popper z-999", props.popClass]}
                style={dropdownStyle.value}
                ref={popupRef}
              >
                {renderSlot(slots, "popper")}
              </div>
            </Transition>
          </Teleport>
        </div>
      )
    }
  }
})
