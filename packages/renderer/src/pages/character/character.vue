<script lang="tsx">
  import { defineComponent, onMounted, ref, renderList, reactive } from "vue"
  import { useCharacterStore } from "@/store"
  import { ICharacterInfo } from "@/api/character/type"
  import { useRoute } from "vue-router"

  function skill_icon(character: string, skillName: string) {
    return `./images/characters/${character}/skill/${skillName}.png`
  }

  export default defineComponent(() => {
    let basicInfo = ref<ICharacterInfo>({ skillInfo: [], individuation: [] })
    let characterName = ref<string>("")
    const route = useRoute()
    onMounted(async () => {
      const characterInfoState = useCharacterStore()
      if (typeof route.params.name === "string") {
        characterName.value = route.params.name
        await characterInfoState.get_character_info(characterName.value)
        basicInfo.value = characterInfoState[characterName.value]
          ?.basicInfo as ICharacterInfo
      }
    })

    const visible = ref(false)
    const showDialog = () => (visible.value = true)

    return () => (
      <div bg-cover bg-no-repeat pt-8 pb-12 pl-4>
        {renderList(basicInfo.value.skillInfo, (skill, index) => (
          <div>
            <img src={skill_icon(characterName.value, skill.name)} />
            {skill.name}
          </div>
        ))}
      </div>
    )
  })
</script>
