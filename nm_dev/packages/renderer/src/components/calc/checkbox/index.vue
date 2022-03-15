<script lang="tsx">
  import { defineComponent, renderSlot } from "vue"
  import { switchProps, useSwitch } from "@/components/hooks/swtich/swtich"

  export default defineComponent({
    name: "i-checkbox",
    components: {},
    props: {
      ...switchProps,
      label: {
        type: String
      }
    },

    setup(props, context) {
      const { toggle, switchClass } = useSwitch(
        {
          ...props,
          class: "i-checkbox flex items-center text-xs h-6 cursor-pointer",
          checkedClass: "checked"
        },
        context
      )

      const { slots } = context

      return () => (
        <div onClick={() => toggle()} class={switchClass.value}>
          <span class="i-checkbox-icon"></span>
          <span class="i-checkbox-label">
            {props.label ?? renderSlot(slots, "default")}
          </span>
        </div>
      )
    }
  })
</script>
<style lang="scss">
  .i-checkbox {
    &.checked {
      .i-checkbox-icon {
        background-image: url("./img/checkbox_checked.png");
      }
    }

    .i-checkbox-icon {
      width: 12px;
      height: 12px;
      margin-right: 4px;
      background-image: url("./img/checkbox_uncheck.png");
    }

    &:hover:not(.checked) {
      .i-checkbox-icon {
        background-image: url("./img/checkbox_hover.png");
      }
    }

    .i-checkbox-label {
      height: 24px;
      line-height: 24px;
      color: #af8f4c;
    }
  }
</style>
