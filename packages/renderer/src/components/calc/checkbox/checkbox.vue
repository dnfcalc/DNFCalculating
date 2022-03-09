<script lang="tsx">
  import { defineComponent, ref, renderSlot } from "vue"

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
          <span
            class={{ "i-checkbox-icon": true, checked: checked.value }}
          ></span>
          <span class="i-checkbox-label" v-text={props.label}></span>
        </div>
      )
    }
  })
</script>
<style lang="scss">
  .i-checkbox {
    display: flex;
    align-items: center;
    font-size: 12px;
    height: 24px;
    .i-checkbox-icon {
      width: 12px;
      height: 12px;
      margin-right: 4px;
      background-image: url("./img/checkbox_uncheck.png");

      &.checked {
        background-image: url("./img/checkbox_checked.png");
      }
    }

    &:hover {
      .i-checkbox-icon:not(.checked) {
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
