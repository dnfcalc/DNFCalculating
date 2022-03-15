import { useToggle } from "@vueuse/core"
import { computed, PropType, ref, watch } from "vue"
import { defineHooks } from "../define"

export const switchProps = {
  modelValue: {
    type: [Boolean, null, undefined] as PropType<boolean | undefined>,
    default: () => null
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
}

export const useSwitch = defineHooks(switchProps, (props, { emit }) => {
  const checked = ref(!!props.modelValue)

  watch(
    () => props.modelValue,
    val => {
      checked.value = !!val
    }
  )

  const modelValue = computed<boolean>({
    get() {
      return !!(props.modelValue ?? checked.value)
    },
    set(val) {
      checked.value = val
      emit("change", val)
      emit("update:modelValue", val)
    }
  })

  const toggle = useToggle(modelValue)

  const switchClass = computed(() => {
    return [
      props.class,
      modelValue.value ? props.checkedClass : props.uncheckedClass
    ]
  })

  return {
    toggle,
    modelValue,
    switchClass
  }
})
