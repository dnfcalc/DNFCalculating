<script lang="tsx">
  import { useToggle } from "@vueuse/core"
  import { defineComponent, ref, renderSlot } from "vue"

  export default defineComponent({
    name: "calc-menu",
    props: ["label"],
    setup(props, { slots }) {
      const expand = ref(false)

      const toggle = useToggle(expand)

      return () => {
        return (
          <div class="i-menu">
            <div class="i-menu-content">
              <div onClick={() => toggle()} class="i-menu-expand-icon">
                <svg viewBox="0 0 1024 1024" width="100%" height="100%">
                  <path
                    d="M85.312 85.312v853.376h853.376V85.312H85.312zM0 0h1024v1024H0V0z m554.624 213.312v256h256v85.376h-256v256H469.312v-256h-256V469.376h256v-256h85.312z"
                    fill="currentColor"
                  ></path>
                </svg>
              </div>
              <div class="i-menu-label" v-trans={props.label}></div>
            </div>
            <div class={{ "i-menu-items": true, expand: expand.value }}>
              {renderSlot(slots, "default")}
            </div>
          </div>
        )
      }
    }
  })
</script>
<style lang="scss">
  .i-menu {
    min-width: 120px;
    width: 200px;
    transition: all 0.3s ease;

    .i-menu-content {
      width: 100%;
      height: 16px;
      line-height: 16px;
      display: flex;
      background-color: rgba(37, 37, 37, 0.4);
      padding: 4px;

      .i-menu-expand-icon {
        width: 12px;
        height: 12px;
        color: rgb(255, 247, 148);
        margin-right: 8px;
      }

      .i-menu-label {
        width: auto;
        font-size: 12px;
      }
    }

    .i-menu-items {
      height: 0;
      overflow: hidden;

      &.expand {
        height: 32px;
      }
    }
  }
</style>
