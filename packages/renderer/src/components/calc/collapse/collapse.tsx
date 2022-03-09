import { computed, defineComponent, ref, renderSlot, watch } from "vue"

export default defineComponent({
    name: "i-collapse",
    props: {
        title: {
            type: String
        },
        modelValue: {
            type: Boolean
        }
    },
    setup(props, { slots, emit }) {
        const is_collapse = ref(props.modelValue)

        watch(
            () => props.modelValue,
            val => (is_collapse.value = val)
        )

        const modelValue = computed<boolean>({
            set(val) {
                emit("update:modelValue", val)
                is_collapse.value = val
            },
            get() {
                return !!is_collapse.value
            }
        })

        function collapse() {
            modelValue.value = !modelValue.value
        }

        return () => {
            return (
                <div class="my-1 overflow-hidden h-auto rounded bg-hex-#00000078 border-1 border-hex-#ffffff28">
                    <div onClick={collapse} v-text={props.title} class="bg-gradient-to-b to-hex-#122438 from-hex-#244281 w-full h-6 text-xs text-center items-center justify-center flex"></div>
                    <div class={["transition-all", "ease-in-out", "h-auto"].concat(modelValue.value ? ["max-h-200"] : ["max-h-0"])}>
                        <div class="p-2">{renderSlot(slots, "default")}</div>
                    </div>
                </div>
            )
        }
    }
})
