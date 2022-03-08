/**
 * @Author: Kritsu
 * @Date:   2021/11/16 18:33:00
 * @Last Modified by:   Kritsu
 * @Last Modified time: 2021/11/17 18:49:21
 */
import { computed, defineComponent, h, inject, Ref, useSlots } from "vue"
import { RouterLink } from "vue-router"
import { AciveClassSymbol, AciveSymbol } from "./constants"

export default defineComponent({
    name: "calc-tab",
    props: ["value", "width", "to"],
    setup(props, ctx) {
        const active = inject<Ref<any>>(AciveSymbol)

        const isActive = computed<boolean>(() => {
            return props.value == active?.value
        })
        const slots = useSlots()

        const activeClass = inject<Ref<string>>(AciveClassSymbol)
        return () => {
            const width = props.width ?? 120

            const params = {
                style: {
                    width: `${width}px`
                },
                class: {
                    "i-tab": true,
                    [activeClass?.value ?? "active"]: isActive.value
                }
            }

            if (!!props.to) {
                return h(
                    RouterLink,
                    {
                        ...params,
                        to: props.to
                    },
                    slots.default?.()
                )
            }
            return h(
                "li",
                {
                    ...params,
                    onClick() {
                        if (!!active) {
                            active.value = props.value
                        }
                    }
                },

                slots.default?.()
            )
        }
    }
})
