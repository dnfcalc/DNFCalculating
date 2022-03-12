<script lang="tsx">
  import { defineComponent, ref } from "vue"

  export default defineComponent(() => {
    const visible = ref(false)
    const showDialog = () => (visible.value = true)

    return () => (
      <div>
        <calc-tabs>
          <calc-tab value="1">套装</calc-tab>
          <calc-tab value="2">自选</calc-tab>
        </calc-tabs>
        <calc-button onClick={showDialog}>DYSB</calc-button>
        <calc-checkbox>DYSB</calc-checkbox>
        <calc-select>
          <calc-option value={2}>123</calc-option>
          <calc-option value={1}>467</calc-option>
        </calc-select>
        <calc-dialog v-model:visible={visible.value}>测试</calc-dialog>
      </div>
    )
  })
</script>
