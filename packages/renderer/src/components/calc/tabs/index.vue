<script lang="tsx">
  /**
   * @Author: Kritsu
   * @Date:   2021/11/16 18:11:47
   * @Last Modified by:   Kritsu
   * @Last Modified time: 2021/11/17 18:49:19
   */
  import { defineComponent, computed, provide, renderSlot } from "vue"
  import NSelection from "@/components/base/selection"
  import { listProps } from "@/components/hooks/selection/list"

  export default defineComponent({
    name: "calc-tabs",
    components: {
      NSelection
    },
    props: {
      ...listProps,
      vertical: {
        type: Boolean
      }
    },
    setup(props, { emit, slots }) {
      return () => {
        return (
          <n-selection
            {...props}
            class={{ "i-tabs": true, vertical: !!props.vertical }}
            item-class="i-tab cursor-pointer"
          >
            {renderSlot(slots, "default")}
          </n-selection>
        )
      }
    }
  })
</script>
<style lang="scss">
  /**
 * @Author: Kritsu
 * @Date:   2021/11/16 18:31:51
 * @Last Modified by:   Kritsu
 * @Last Modified time: 2021/11/17 18:03:13
 */
  .i-tabs {
    display: flex;
    list-style: none;

    font-size: 14px;

    color: #c6b083;
    margin: 0;
    padding: 0;

    a {
      text-decoration: none;
      color: #c6b083;
      &:visited {
        color: currentColor;
      }
    }

    &.vertical {
      flex-direction: column;

      .i-tab {
        border-radius: 0;
      }
    }

    .i-tab {
      font-size: 12px;

      width: 120px;
      height: 24px;
      line-height: 24px;
      text-align: center;
      text-decoration: none;

      &:visited {
        color: currentColor;
      }

      border: black 1px solid;
      border-radius: 5px 5px 0 0;
      background: linear-gradient(#2e2f31, #121315);
      transition: all 0.4s ease-in-out;

      &:hover {
        background: linear-gradient(#4a4b4e, #1d1e22);
      }

      &.active {
        background: linear-gradient(#574d38, #25221d);
        border-image: url("./img/active_top.png") 1 fill stretch;
        color: #ffb400;
      }
    }
  }
</style>
