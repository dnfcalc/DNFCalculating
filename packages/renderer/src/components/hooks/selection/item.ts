import { ClassType } from "./types"
import { ComponentPropsOptions, computed, ComputedRef, inject, onDeactivated, ref, Ref, SetupContext, toRaw, watch } from "vue"
import { AciveClassSymbol, AciveSymbol, InitSymbol, ItemClassSymbol, ModelValueSymbol, Option, UnactiveSymbol } from "./constants"

export const itemProps: ComponentPropsOptions = {
  value: {
    type: [Object, String, Number, Boolean]
  },
  label: {
    type: [Function, String]
  }
}

export function useSelectionItem(props: any) {
  const active = inject(AciveSymbol) as Ref<Option>
  const init = inject<(obj: any) => () => void>(InitSymbol)
  const modelValue = inject(ModelValueSymbol) as Ref

  const isActive = computed<boolean>(() => {
    return props.value == active?.value?.value
  })

  const current = computed(() => {
    let key: string | Function = props.label
    if (typeof key == "function") {
      key = (key(props.value) as string) ?? props.value
    }
    return {
      key,
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
    return [inject<ComputedRef<ClassType>>(ItemClassSymbol)?.value ?? "", isActive.value ? activeClass.value : unactiveClass.value]
  })

  const activeClass = computed(() => {
    return inject<ComputedRef<ClassType>>(AciveClassSymbol)?.value ?? "active"
  })

  const unactiveClass = computed(() => {
    return inject<ComputedRef<ClassType>>(UnactiveSymbol)?.value ?? "unactive"
  })

  return {
    active,
    isActive,
    current,
    activeClass,
    unactiveClass,
    itemClass
  }
}

export interface ItemProps {}
