import { defineComponent, ref, renderSlot } from "vue"
import "./style.scss"
import plusSvg from "./img/plus.svg"
import exp from "constants"

export default defineComponent({
    name: "calc-menu",
    props: ["label"],
    setup(props, { slots }) {
        const expand = ref(false)

        function open() {
            expand.value = !expand.value
            console.log("open")
        }

        return () => {
            return (
                <div class="i-menu">
                    <div class="i-menu-content">
                        <div onClick={open} class="i-menu-expand-icon">
                            <svg viewBox="0 0 1024 1024" width="100%" height="100%">
                                <path
                                    d="M85.312 85.312v853.376h853.376V85.312H85.312zM0 0h1024v1024H0V0z m554.624 213.312v256h256v85.376h-256v256H469.312v-256h-256V469.376h256v-256h85.312z"
                                    fill="currentColor"
                                ></path>
                            </svg>
                        </div>
                        <div class="i-menu-label" v-trans={props.label}></div>
                    </div>
                    <div class={{ "i-menu-items": true, expand: expand.value }}>{renderSlot(slots, "default")}</div>
                </div>
            )
        }
    }
})
