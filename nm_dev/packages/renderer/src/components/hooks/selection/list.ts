import type { BaseType, ClassType } from "./types"
import {
  computed,
  provide,
  ref,
  SetupContext,
  ComponentPropsOptions,
  Ref,
  PropType
} from "vue"
import {
  AciveClassSymbol,
  AciveSymbol,
  InitSymbol,
  ItemClassSymbol,
  ModelValueSymbol,
  Option,
  UnactiveSymbol
} from "./constants"

const valuePropType = [
  String,
  Number,
  Object,
  Boolean,
  null
] as PropType<BaseType>

const classPropType = [String, Array] as PropType<string | string[]>

export const listProps: ComponentPropsOptions = {
  modelValue: {
    type: valuePropType,
    default() {
      return null
    }
  },
  defaultValue: {
    type: valuePropType,
    default() {
      return null
    }
  },
  activeClass: {
    type: classPropType
  },
  itemClass: {
    type: classPropType
  },
  unactiveClass: {
    type: classPropType
  }
}

export function useSelectionList(props: Readonly<any>, context: SetupContext) {
  const current = ref<Option>()

  const modelValue = computed(() => props.modelValue)

  const active = computed<Option | undefined>({
    set(val: Option | undefined) {
      context.emit("update:modelValue", val?.value)
      current.value = val
    },
    get() {
      return (
        options.find(e => e.value.value == props.modelValue)?.value ??
        current.value
      )
    }
  })

  provide(ModelValueSymbol, modelValue)

  provide(AciveSymbol, active)

  provide(
    AciveClassSymbol,
    computed(() => props.activeClass)
  )

  provide(
    UnactiveSymbol,
    computed(() => props.unactiveClass)
  )

  provide(
    ItemClassSymbol,
    computed(() => props.itemClass)
  )

  const options: Ref<Option>[] = []

  provide(InitSymbol, (option: Ref<Option>) => {
    options.push(option)
    if (option.value.value == props.modelValue || active.value == undefined) {
      current.value = option.value
    }
    return () => {
      options.splice(options.indexOf(option), 1)
    }
  })

  return {
    active,
    modelValue
  }
}
