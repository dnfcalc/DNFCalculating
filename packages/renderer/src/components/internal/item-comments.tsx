import { getCommentByItem } from "@/core/equips/comment"
import { Item } from "@/core/item"
import { computed, defineComponent } from "vue"

export default defineComponent({
    name: "item-comments",
    props: ["item"],

    setup(props) {
        const item = computed(() => props.item as Item)
        const commtents = computed(() => getCommentByItem(item.value))
        return () => {
            const content: JSX.Element[] = []
            if (item.value.fame) {
                content.push(<div v-trans:comments={`{adventurer_fame} ${item.value.fame}`}></div>)
            }

            for (let comment of commtents.value) {
                content.push(<div class="item-comment" v-trans:comments={comment}></div>)
            }

            return <div class="item-comments">{content}</div>
        }
    }
})
