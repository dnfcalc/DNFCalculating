import { Equip, getEquipImage } from "@/core/equips"
import Tooltip from "@/components/tooltip/tooltip"
import "./item-icon.scss"
import { ItemColumn } from "@/core/item"
import { defineComponent, computed, renderSlot } from "vue"

export default defineComponent({
    name: "item-icon",
    components: {
        Tooltip
    },
    emits: ["change"],
    props: ["column", "titleColor"],
    setup(props, { slots, emit }) {
        const column = computed<ItemColumn>(() => {
            return props.column as ItemColumn
        })

        const item = computed(() => {
            return column.value?.item
        })

        const item_title = computed(() => {
            if (!item.value) {
                return ""
            }
            let { name, title } = item.value
            if (title) {
                if (typeof title == "function") {
                    return title()
                }
                return title
            }
            return name
        })

        const title_color = computed(() => {
            if (props.titleColor) {
                return props.titleColor
            }
            if (item.value) {
                const { rarity } = item.value

                if (rarity) {
                    return `${rarity}-color`
                }
            }
            return ""
        })

        function onChange(...args: any[]) {
            emit("change", ...args)
        }

        return () => {
            if (!item.value) {
                return <div></div>
            }

            const { name: item_name, icon, suit_name, rarity, part } = item.value
            const children = {
                default: () => slots.icon?.() ?? <img src={icon} />,
                popper: () => (
                    <>
                        {slots.header ? (
                            slots.header?.()
                        ) : (
                            <div class="item-tooltip-title">
                                <div class={`${title_color.value} item-name`}>
                                    <span v-trans:items={item_title.value}></span>
                                </div>

                                {suit_name ? (
                                    <div class="item-suit-name suit-color">
                                        <span v-trans:items={suit_name}></span>
                                        <span class="suffix" v-trans="suits"></span>
                                    </div>
                                ) : (
                                    <div></div>
                                )}
                            </div>
                        )}
                        <div class="item-tooltip-comments">{renderSlot(slots, "default")}</div>
                    </>
                )
            }

            return <Tooltip onChange={onChange} popper-class="item-tooltip" v-slots={children}></Tooltip>
        }
    }
})
