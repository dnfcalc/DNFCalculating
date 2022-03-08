/**
 * @Author: Kritsu
 * @Date:   2021/11/09 15:31:30
 * @Last Modified by:   Kritsu
 * @Last Modified time: 2021/11/17 18:49:23
 */
import { defineComponent, ref, computed, watch, h, Teleport, onDeactivated, renderSlot, CSSProperties, Transition } from "vue"
import { listProps, useSelectionList } from "../selection/list"
import { onClickOutside } from "@vueuse/core"
import "./style.scss"

export default defineComponent({
    name: "i-select",
    props: {
        ...listProps,
        disabled: {
            type: Boolean,
            default: false
        },
        width: {
            type: Number,
            default: 120
        },
        emptyLabel: {
            type: String
        }
    },
    setup(props, context) {
        const { active } = useSelectionList(props, context)

        const isOpen = ref(false)
        const triggerRef = ref<HTMLElement>()

        watch(isOpen, onResize)

        function collapse() {
            isOpen.value = !isOpen.value && !isDisabled.value
        }

        // 下拉框位置
        const dropdownPosition = ref({ x: 0, y: 0, w: 0 })
        // 下拉框位置
        const dropdownStyle = computed<CSSProperties>(() => {
            return {
                left: `${dropdownPosition.value.x}px`,
                top: `${dropdownPosition.value.y}px`,
                width: `${dropdownPosition.value.w}px`
            }
        })

        function onResize() {
            if (!!triggerRef.value) {
                const { width, height, left, top } = triggerRef.value.getBoundingClientRect()
                dropdownPosition.value = {
                    w: width,
                    x: left,
                    y: top + height + 4
                }
            }
        }

        const isDisabled = computed(() => !!props.disabled)

        onClickOutside(triggerRef, () => (isOpen.value = false))

        window.addEventListener("resize", onResize)
        window.addEventListener("scroll", onResize)

        onDeactivated(() => {
            window.removeEventListener("resize", onResize)
            window.removeEventListener("scroll", onResize)
        })

        return () => {
            function renderTrigger() {
                return (
                    <div
                        class={{
                            "i-select-trigger": true,
                            disabled: props.disabled
                        }}
                        ref={triggerRef}
                    >
                        <span class="i-select-label" v-text={active.value?.key ?? props.emptyLabel}></span>
                        <span class="i-select-down-icon"></span>
                    </div>
                )
            }

            const renderDropDown = () => {
                const { slots } = context
                return (
                    <Teleport to="body">
                        <div class="i-select-dropdown" style={dropdownStyle.value} v-show={isOpen.value}>
                            {renderSlot(slots, "default")}
                        </div>
                    </Teleport>
                )
            }

            return (
                <div class="i-select" onClick={collapse}>
                    {renderTrigger()}
                    {renderDropDown()}
                </div>
            )
        }
    }
})
