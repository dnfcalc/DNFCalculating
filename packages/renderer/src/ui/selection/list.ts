import { computed, provide, ref, SetupContext, ComponentPropsOptions, Ref } from "vue"
import { AciveClassSymbol, AciveSymbol, InitSymbol, ModelValueSymbol, Option } from "./constants"

export const listProps: ComponentPropsOptions = {
    modelValue: {
        type: [String, Number, Object, Boolean],
        default() {
            return null
        }
    },
    defaultValue: {
        type: [String, Number, Object, Boolean],
        default() {
            return null
        }
    },
    activeClass: {
        type: String
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
            return options.find(e => e.value.value == props.modelValue)?.value ?? current.value
        }
    })

    provide(ModelValueSymbol, modelValue)

    provide(AciveSymbol, active)

    provide(
        AciveClassSymbol,
        computed(() => props.activeClass)
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
