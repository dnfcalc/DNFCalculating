import { ComponentPropsOptions, computed, ComputedRef, inject, onDeactivated, ref, Ref, SetupContext, toRaw, watch } from "vue"
import { AciveClassSymbol, AciveSymbol, InitSymbol, ModelValueSymbol, Option } from "./constants"

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

    const activeClass = inject<ComputedRef<string>>(AciveClassSymbol) ?? ref("active")

    return {
        active,
        isActive,
        current,
        activeClass
    }
}

export interface ItemProps {}
