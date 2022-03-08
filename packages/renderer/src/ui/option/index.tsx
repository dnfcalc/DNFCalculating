/**
 * @Author: Kritsu
 * @Date:   2021/11/12 10:09:29
 * @Last Modified by:   Kritsu
 * @Last Modified time: 2021/11/17 18:03:06
 */
import { defineComponent } from "vue"
import { itemProps, useSelectionItem } from "../selection/item"

export default defineComponent({
    name: "i-option",
    props: itemProps,
    setup(props) {
        const { active, activeClass, isActive, current } = useSelectionItem(props)
        function onClick() {
            active.value = current.value
        }
        return () => {
            const classes = ["i-option"]
            if (isActive.value) {
                classes.push(activeClass.value)
            }

            return <span class={classes} onClick={onClick} v-text={current.value.key}></span>
        }
    }
})
