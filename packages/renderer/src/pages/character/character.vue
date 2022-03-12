<script lang="tsx">
  import { defineComponent, onMounted, ref, renderList, reactive } from "vue"
  import { useCharacterStore } from "@/store"
  import { ICharacterInfo } from "@/api/character/type"
  import { useRoute } from "vue-router"
  export default defineComponent(() => {
    let basicInfo = ref<ICharacterInfo>({ skillInfo: [], individuation: [] })
    const route = useRoute()
    onMounted(async () => {
      const characterInfoState = useCharacterStore()
      if (typeof route.params.name === "string") {
        await characterInfoState.get_character_info(route.params.name)
        basicInfo.value = characterInfoState[route.params.name]
          ?.basicInfo as ICharacterInfo
      }
    })

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
        <calc-dialog modal v-model:visible={visible.value}>
          测试
        </calc-dialog>
        {renderList(basicInfo.value.skillInfo, (skill, index) => (
          <div>{skill.name}</div>
        ))}
      </div>
    )
  })
</script>
