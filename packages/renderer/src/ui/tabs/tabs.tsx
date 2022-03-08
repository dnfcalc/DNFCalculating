/**
 * @Author: Kritsu
 * @Date:   2021/11/16 18:11:47
 * @Last Modified by:   Kritsu
 * @Last Modified time: 2021/11/17 18:49:19
 */
import { defineComponent, computed, provide, renderSlot } from "vue"
import { AciveSymbol, AciveClassSymbol } from "./constants"
import "./style.scss"

export default defineComponent({
    name: "calc-tabs",
    props: {
        modelValue: {
            type: [Object, Number, String, Array]
        },
        vertical: {
            type: Boolean
        },
        activeClass: {
            type: String
        }
    },
    setup(props, { emit, slots }) {
        const active = computed({
            set: (val: any) => emit("update:modelValue", val),
            get: () => props.modelValue
        })

        provide(AciveSymbol, active)

        provide(
            AciveClassSymbol,
            computed(() => props.activeClass)
        )

        return () => {
            return <ul class={{ "i-tabs": true, vertical: !!props.vertical }}>{renderSlot(slots, "default")}</ul>
        }
    }
})
