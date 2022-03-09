<script lang="tsx">
  /**
   * @Author: Kritsu
   * @Date:   2021/11/16 23:07:51
   * @Last Modified by:   Kritsu
   * @Last Modified time: 2021/11/17 18:49:42
   */
  import {
    watch,
    defineComponent,
    renderSlot,
    h,
    useSlots,
    Slot,
    Teleport,
    ref,
    computed,
    CSSProperties
  } from "vue"
  import "./style.scss"

  export default defineComponent({
    name: "calc-tooltip",
    emits: ["change"],
    props: ["popperClass"],
    setup(props, { slots, emit }) {
      const isOpen = ref(false)

      const triggerRef = ref<Element>()
      const dropdownPosition = ref({ x: 0, y: 0 })
      const dropdownStyle = computed<CSSProperties>(() => {
        return {
          left: `${dropdownPosition.value.x}px`,
          top: `${dropdownPosition.value.y}px`,
          visibility: isOpen.value ? "visible" : "hidden"
        }
      })
      function onMouseover(event: Event) {
        isOpen.value = true

        if (!!triggerRef.value) {
          const { width, height, left, top } =
            triggerRef.value.getBoundingClientRect()
          dropdownPosition.value = {
            x: left,
            y: top + height + 4
          }
        }
      }

      function onMouseout() {
        isOpen.value = false
      }

      watch(isOpen, () => emit("change", isOpen.value))

      return () => {
        return (
          <div class="i-tooltip">
            <div
              onMouseover={onMouseover}
              onMouseout={onMouseout}
              ref={triggerRef}
              class="i-tooltip-content"
            >
              {renderSlot(slots, "default")}
            </div>
            <Teleport to="body">
              <div
                class={["i-popper", props.popperClass]}
                style={dropdownStyle.value}
              >
                {renderSlot(slots, "popper")}
              </div>
            </Teleport>
          </div>
        )
      }
    }
  })
</script>
<style lang="scss">
  .i-popper {
    z-index: 999;
    position: fixed;
    top: 0;
    left: 0;
    width: auto;
    height: auto;
    min-width: 100px;
    min-height: 80px;
    border: 1px solid #5b472a;
    background-color: rgba(0, 0, 0, 0.8);
  }
</style>
