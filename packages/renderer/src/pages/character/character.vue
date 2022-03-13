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
        {renderList(basicInfo.value.skillInfo, (skill, index) => (
          <div>{skill.name}</div>
        ))}
      </div>
    )
  })
</script>
