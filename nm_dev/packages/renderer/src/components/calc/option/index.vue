<script lang="tsx">
  import { defineComponent, h, renderSlot } from "vue"
  import { itemProps } from "@/components/hooks/selection/item"
  import NItem from "@/components/base/item"
  export default defineComponent({
    props: {
      ...itemProps
    },
    components: { NItem },
    setup(props, { slots }) {
      return () => <n-item {...props}>{renderSlot(slots, "default")}</n-item>
    }
  })
</script>
