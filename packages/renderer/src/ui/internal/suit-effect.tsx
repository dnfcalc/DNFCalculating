import { CalcData } from "@/core/calc"
import { equips } from "@/core/equips"
import { getCommentByContext } from "@/core/equips/comment"
import { suits } from "@/core/equips/suits"
import { hasEquip } from "@/store"
import { computed, defineComponent } from "vue"
import "./suit-effect.scss"

export default defineComponent({
    props: {
        suitname: {
            type: String
        }
    },

    setup(props) {
        const suit_equips = computed(() => {
            return equips
                .filter(e => e.suit_name == props.suitname)
                .map(e => {
                    return {
                        name: e.name,
                        active: hasEquip(e.name)
                    }
                })
        })

        const activeCount = computed(() => {
            return suit_equips.value.filter(e => e.active).length
        })

        const suit_effects = computed(() => {
            return suits
                .filter(s => s.name == props.suitname)
                .map(e => {
                    const context = new CalcData()
                    e.effect?.(context)
                    const comments = getCommentByContext(context)
                    return {
                        comments,
                        active: activeCount.value >= e.needCount,
                        count: e.needCount
                    }
                })
        })

        return () => {
            return (
                <div class="suit-tooltip">
                    <div class="suit-equip-list">
                        {suit_equips.value.map(e => (
                            <div v-trans:items={e.name} class={{ "suit-color": e.active, "suit-equip": true }}></div>
                        ))}
                    </div>
                    <div class="suit-effects">
                        {suit_effects.value.map(e => (
                            <div class="suit-effect-block">
                                <div class={{ "suit-effect-title": true, "suit-color": e.active }} v-trans={`{suit_effect}[${e.count}]`}></div>
                                {e.comments.map(comment => (
                                    <div class={{ "suit-effect-comment": true, active: e.active }} v-trans:comments={comment}></div>
                                ))}
                            </div>
                        ))}
                    </div>
                </div>
            )
        }
    }
})
