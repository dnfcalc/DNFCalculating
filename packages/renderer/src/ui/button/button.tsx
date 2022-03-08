/**
 * @Author: Kritsu
 * @Date:   2021/11/16 23:07:51
 * @Last Modified by:   Kritsu
 * @Last Modified time: 2021/11/17 18:49:42
 */
import { defineComponent, useSlots, h, renderSlot } from "vue"
import { RouterLink } from "vue-router"
import "./style.scss"

export default defineComponent({
    name: "calc-button",
    props: {
        disabled: {
            type: Boolean,
            default: false
        },
        small: {
            type: Boolean,
            default: false
        },
        to: {
            type: String,
            default: null
        }
    },
    setup(props, { slots }) {
        return () => {
            return h(
                //@ts-ignore
                !!props.to ? RouterLink : "button",
                {
                    to: props.to,
                    class: {
                        "i-button": true,
                        disabled: props.disabled,
                        small: props.small
                    }
                },
                renderSlot(slots, "default")
            )
        }
    }
})
