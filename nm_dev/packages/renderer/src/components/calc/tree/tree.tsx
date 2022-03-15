import { defineComponent, ref, renderSlot } from "vue"
import "./style.scss"
import plusSvg from "./img/plus.svg"
import exp from "constants"

export default defineComponent({
    name: "calc-tree",
    props: ["label", "data"],
    setup(props, { slots }) {
        const expand = ref(false)

        function open() {
            expand.value = !expand.value
        }

        return () => {
            return (
                <div class="i-tree">
                    <div class="i-tree-content">
                        <div class="i-tree-label" v-trans={props.label}></div>
                    </div>
                    <div class={{ "i-tree-items": true, expand: expand.value }}>{renderSlot(slots, "default")}</div>
                </div>
            )
        }
    }
})
