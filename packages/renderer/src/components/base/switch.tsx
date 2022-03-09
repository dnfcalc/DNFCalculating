import { computed, defineComponent, ref, renderSlot, watch } from "vue"

/**
 *  可以切换状态的开关
 */

export default defineComponent({
  name: "i-switch",
  props: {
    modelValue: {
      type: Boolean
    },
    class: {
      type: String,
      default: () => ""
    },
    checkedClass: {
      type: String,
      default: () => "checked"
    },
    uncheckedClass: {
      type: String,
      default: () => "unchecked"
    },
    onClickChecked: {
      type: Boolean,
      default: () => true
    }
  },

  setup(props, { emit, slots }) {
    const checked = ref(!!props.modelValue)

    watch(
      () => props.modelValue,
      val => {
        checked.value = val
      }
    )

    const modelValue = computed<boolean>({
      get() {
        return props.modelValue ? props.modelValue : checked.value
      },
      set(val) {
        checked.value = val
        emit("change", val)
        emit("update:modelValue", val)
      }
    })

    function click() {
      if (props.onClickChecked) {
        modelValue.value = !modelValue.value
      }
    }

    return () => (
      <div onClick={click} onTouchstart={click} class={[props.class, modelValue.value ? props.checkedClass : props.uncheckedClass]}>
        {renderSlot(slots, "default")}
      </div>
    )
  }
})
