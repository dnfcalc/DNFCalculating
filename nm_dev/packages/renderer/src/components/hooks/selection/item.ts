import {
  ComponentPropsOptions,
  computed,
  ComputedRef,
  inject,
  onDeactivated,
  PropType,
  Ref,
  renderSlot,
  watch
} from "vue"
import { defineHooks } from "../define"
import {
  AciveClassSymbol,
  AciveSymbol,
  InitSymbol,
  ItemClassSymbol,
  ModelValueSymbol,
  Option,
  UnactiveSymbol
} from "./constants"
import { ClassType } from "./types"

export const itemProps: ComponentPropsOptions = {
  value: {
    type: [Object, String, Number, Boolean]
  },
  label: {
    type: [Function, String] as PropType<string | ((val: string) => string)>
  }
}

export const useSelectionItem = defineHooks(itemProps, (props, { slots }) => {
  const active = inject(AciveSymbol) as Ref<Option>
  const init = inject<(obj: any) => () => void>(InitSymbol)
  const modelValue = inject(ModelValueSymbol) as Ref

  const isActive = computed<boolean>(() => {
    return props.value == active?.value?.value
  })

  const current = computed(() => {
    let label = props.label as string | Function
    if (typeof label == "function") {
      label = (label(props.value) as string) ?? props.value
    }
    return {
      label,
      render,
      value: props.value
    }
  })

  if (!!init) {
    const remove = init(current)
    onDeactivated(remove)
  }

  watch(current, (newVal, oldVal) => {
    if (active && oldVal.value == modelValue.value) {
      active.value = newVal
    }
  })

  const itemClass = computed(() => {
    return [
      inject<ComputedRef<ClassType>>(ItemClassSymbol)?.value ?? "",
      isActive.value ? activeClass.value : unactiveClass.value
    ]
  })

  const activeClass = computed(() => {
    return inject<ComputedRef<ClassType>>(AciveClassSymbol)?.value ?? "active"
  })

  const unactiveClass = computed(() => {
    return inject<ComputedRef<ClassType>>(UnactiveSymbol)?.value ?? "unactive"
  })

  function render() {
    return (props.label as string) ?? renderSlot(slots, "default")
  }

  return {
    active,
    isActive,
    current,
    activeClass,
    unactiveClass,
    itemClass,
    render
  }
})

export interface ItemProps {}
