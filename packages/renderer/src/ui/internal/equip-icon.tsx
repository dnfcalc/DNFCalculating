import { Equip, getEquipImage } from "@/core/equips"
import "./equip-icon.scss"
import { Item, ItemColumn } from "@/core/item"
import { defineComponent, computed, ref, onMounted, onUnmounted } from "vue"
import SuitEffect from "./suit-effect"
import equipComments from "./equip-comments"
import itemIcon from "./item-icon"
export default defineComponent({
    name: "equip-icon",
    components: {
        equipComments,
        itemIcon
    },
    props: {
        column: {
            type: Object
        },
        showIcon: {
            type: Boolean,
            default: () => true
        }
    },
    setup(props) {
        const column = computed<ItemColumn>(() => {
            return props.column as ItemColumn
        })

        const equip_title = computed(() => {
            const { data, slots = [] } = column.value

            if (column.value.item) {
                const { name }: Item = column.value.item
                const upgrade_level = (data?.get("upgrade_level") as number) ?? 0
                const refine_level = (data?.get("refine_level") as number) ?? 0

                let title = ""
                if (slots.some(e => e.name == "amplify") && upgrade_level > 0) {
                    title = `+${upgrade_level}`
                }
                if (refine_level > 0) {
                    title = title.concat(`(${refine_level})`)
                }
                if (title.length > 0) {
                    title = title.concat(" ")
                }
                title = title.concat(`{${name}}`)
                return title
            }
        })

        const showSuitEffect = ref(false)

        onMounted(() => {
            document.addEventListener("keyup", keypress)
        })

        onUnmounted(() => {
            document.removeEventListener("keyup", keypress)
        })

        function keypress(event: KeyboardEvent) {
            if (event.code == "F8") {
                showSuitEffect.value = !showSuitEffect.value
            }
        }

        function onShow() {
            showSuitEffect.value = false
        }

        return () => {
            if (!column.value.item) {
                return <span></span>
            }
            const equip = column.value.item as Equip
            const { suit_name, rarity } = equip
            const icon = () => {
                return (
                    <div class="icon">
                        <img src={getEquipImage(equip)} />
                    </div>
                )
            }

            const defaultVslots = {
                icon,
                header() {
                    return (
                        <div class="equip-tooltip-header">
                            {props.showIcon ? <div class="equip-tooltip-icon">{icon()}</div> : <div></div>}
                            <div class="equip-tooltip-title">
                                <div class={`${rarity}-color equip-name`}>
                                    <span v-trans:items={equip_title.value}></span>
                                </div>

                                {suit_name ? (
                                    <div class="equip-suit-name suit-color">
                                        <span v-trans:items={suit_name}></span>
                                        <span class="suffix" v-trans="suits"></span>
                                    </div>
                                ) : (
                                    <div></div>
                                )}
                            </div>
                        </div>
                    )
                },
                default() {
                    return (
                        <div onKeyup={keypress}>
                            <equip-comments column={column.value} />
                        </div>
                    )
                }
            }

            const suitEffectSlots = {
                header: () => {
                    return <div key="show-suit" class="suit-color" v-trans:items={suit_name}></div>
                },
                default() {
                    return <SuitEffect suitname={suit_name} />
                }
            }

            const vslots = showSuitEffect.value ? suitEffectSlots : defaultVslots

            return <item-icon onChange={onShow} column={column.value} v-slots={vslots}></item-icon>
        }
    }
})
