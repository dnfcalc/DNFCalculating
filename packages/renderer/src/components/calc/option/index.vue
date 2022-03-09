<script lang="tsx">
  import { defineComponent, h } from "vue"
  import { itemProps } from "@/components/hooks/selection/item"
  import item from "@/components/base/item"
  export default defineComponent({
    props: {
      ...itemProps
    },
    components: { item },
    setup(props) {
      return () =>
        h(item, {
          ...props
        })
    }
  })
</script>
