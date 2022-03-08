import { defineComponent, ref, renderSlot } from "vue"
import "./style.scss"

export default defineComponent({
    name: "i-checkbox",
    props: {
        checked: {
            type: Boolean
        },
        label: {
            type: String
        }
    },
    setup(props, { emit, slots }) {
        const checked = ref(!!props.checked)

        function check() {
            checked.value = !checked.value
            emit("update:checked", checked.value)
        }

        return () => (
            <div class="i-checkbox" onClick={check}>
                <span class={{ "i-checkbox-icon": true, checked: checked.value }}></span>
                <span class="i-checkbox-label" v-text={props.label}></span>
            </div>
        )
    }
})
