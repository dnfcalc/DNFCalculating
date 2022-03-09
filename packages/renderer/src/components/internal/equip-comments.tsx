import { armor_parts, Equip, EquipColumn, getOptionValue, getSocketColor, MythicEquip } from "@/core/equips"
import { getCommentByContext, getCommentByEquipColumn } from "@/core/equips/comment"
import { createCharacterStatus, createStatusByEquip, Status } from "@/core/status"
import { CalcData } from "@/core/calc"
import { defineComponent, computed } from "vue"
export default defineComponent({
    name: "equip-comments",
    props: {
        column: {
            type: Object
        }
    },
    setup(props) {
        const column = computed<EquipColumn>(() => {
            return props.column as EquipColumn
        })

        const comments = computed(() => {
            return getCommentByEquipColumn(column.value)
        })

        const socketComments = computed(() => {
            const s = [getComment("socket"), getComment("socket_1")].filter(e => !!e && e.length > 0)
            return s
        })

        const equipSlots = computed(() => {
            if (!comments.value || !column.value) {
                return []
            }
            return column.value.slots
        })

        const current_type = computed(() => {
            if (column.value.item) {
                let { type, part } = column.value.item as Equip
                if (armor_parts.includes(part)) {
                    type = column.value.data.get("armor_type") ?? type
                }
                return type
            }
            return "light"
        })

        const armor_types = ["cloth", "leather", "light", "heavy", "plate"]
        const current_type_title = computed(() => {
            let type = current_type.value as string
            if (armor_types.includes(type)) {
                return type.concat("_armor")
            }
            return undefined
        })

        const socket_color = computed(() => {
            if (column.value.item) {
                let { part } = column.value.item
                return getSocketColor(part)
            }
            return undefined
        })

        const emptyStatus = createCharacterStatus()

        const status = computed(() => {
            if (column.value.item) {
                let equip = column.value.item as Equip
                return createStatusByEquip({ ...equip, type: current_type.value })
            }
            return emptyStatus
        })

        const add_slots_list = ["reinforce", "amplify", "refine"]

        const add_statuess = computed(() => {
            const addes: { [key: string]: Status } = {}
            if (!!column.value) {
                const arr = (equipSlots.value ?? []).filter(e => add_slots_list.includes(e.name))
                for (let slot of arr) {
                    let data = new CalcData()
                    slot.effect(column.value, data)
                    const history = Array.from(data.history())
                    for (let i = 0; i < history.length; i++) {
                        const key = i == 0 ? slot.name : `${slot.name}_${i}`
                        addes[key] = history[i].status
                    }
                }
            }
            return addes
        })

        const bufferRefineComments = computed(() => {
            const buffer_refine = add_statuess.value["refine_1"]
            if (buffer_refine && buffer_refine.intelligence > 0) {
                return `{strength}、{intelligence}、{vitality}、{spirit} +${buffer_refine.intelligence}`
            }
        })

        function getComment(type: string): string[] | JSX.Element[] {
            if (!comments.value) {
                return [<div></div>]
            }
            return comments.value[type] ?? []
        }

        const statusKeys = computed(() => Object.keys(emptyStatus).filter(notEmptyLine))

        function notEmptyLine(key: string) {
            for (let i in add_statuess.value) {
                if (i.includes("_")) {
                    continue
                }
                const val = add_statuess.value[i]
                if (!!val[key]) {
                    return true
                }
            }
            return !!status.value[key]
        }

        const equipModifier = computed(() => {
            const modifier = column.value.item?.modifier
            if (modifier) {
                return modifier
            }
        })

        const mythicProperties = computed(() => {
            const item = column.value.item
            if (item?.rarity == "mythic") {
                const mythic = item as MythicEquip
                return mythic.mythic_properties
            }
        })

        return () => {
            if (!column.value.item) {
                return <span></span>
            }

            const { name: equip_name, icon: equip_icon, suit_name, rarity, part, type } = column.value.item as Equip
            const addes = add_statuess.value

            const content: JSX.Element[] = []
            if (socket_color.value) {
                content.push(
                    <div class="comment">
                        {socketComments.value.map((comments, i) => (
                            <div key={i}>
                                <div class={`${socket_color.value}-socket`} v-trans:comments={`[{${socket_color.value}_socket_column}]`}></div>

                                {comments.map(e => (
                                    <div class="socket-value" v-trans={e}></div>
                                ))}
                            </div>
                        ))}
                    </div>
                )
            }
            if (statusKeys.value.length > 0) {
                const list = statusKeys.value.map(i => (
                    <div key={i}>
                        <span v-trans={i}></span>
                        <span class="num" v-text={status.value[i] || ""}></span>
                        {Object.keys(addes)
                            .filter(e => !e.includes("_"))
                            .map(name => (
                                <span key={name}>{addes[name][i] ? <span class={`num ${name}-color`} v-text={`+${addes[name][i].round()}`}></span> : <span></span>}</span>
                            ))}
                    </div>
                ))
                content.push(<div class="comment status">{list}</div>)
            }
            const enchantings = getComment("enchanting")
            if (enchantings.length > 0) {
                content.push(
                    <div class="comment effect">
                        {enchantings.map((comment, index) => (
                            <div class="enchanting-color" key={index} v-trans={comment}></div>
                        ))}
                    </div>
                )
            }

            if (bufferRefineComments.value) {
                content.push(
                    <div class="comment">
                        <div class="refine-color" v-trans={bufferRefineComments.value}></div>
                    </div>
                )
            }

            const effects = getComment("effect")
            if (effects.length) {
                content.push(
                    <div class="comment effect">
                        {effects.map((comment, index) => (
                            <div key={index} v-trans:comments={comment}></div>
                        ))}
                    </div>
                )
            }

            const mythicProps = mythicProperties.value
            if (mythicProps) {
                const mythics: JSX.Element[] = []
                let i = 1
                for (let myth of mythicProps) {
                    const { deal_data, buff_data, effect } = myth
                    const deal_value = getOptionValue(deal_data)

                    const buff_value = getOptionValue(buff_data)
                    const data = new CalcData()
                    effect(data, [deal_value, buff_value])
                    const mythicComments = getCommentByContext(data)
                    mythics.push(
                        <div>
                            <span v-trans:comments={`{property}${i++}`}></span>
                            {mythicComments.map((comment, index) => (
                                <div key={index} v-trans:comments={comment}></div>
                            ))}
                        </div>
                    )
                }
                if (mythics.length > 0) {
                    content.push(
                        <div class="comment">
                            <div v-trans="<{mythic_property}>" class="property-title"></div>
                            {mythics}
                        </div>
                    )
                }
            }

            if (equipModifier.value) {
                const modifiers = getComment("modifier")
                if (modifiers.length > 0) {
                    content.push(
                        <div class="comment modifier">
                            <div v-trans="<{modifier_property}>" class="property-title"></div>
                            {modifiers.map((comment, index) => (
                                <div key={index} v-trans:comments={comment}></div>
                            ))}
                        </div>
                    )
                }
            }

            return (
                <div>
                    <div class="divider"></div>

                    <div class="info-row">
                        <span class={`${rarity}-color`} v-trans={rarity}></span>
                    </div>
                    <div class="info-row">
                        <span class={current_type.value != type ? "deep-green" : ""} v-trans={current_type_title.value}></span>
                        <span class="part-text" v-trans={current_type_title.value ? `({${part}})` : part}></span>
                    </div>
                    {content}
                </div>
            )
        }
    }
})
