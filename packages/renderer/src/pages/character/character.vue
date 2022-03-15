<script lang="tsx">
  import { defineComponent, onMounted, ref, renderList, reactive } from "vue"
  import { useCharacterStore } from "@/store"
  import { ICharacterInfo, ISkillInfo } from "@/api/character/type"
  import { useRoute } from "vue-router"

  function skill_icon(character: string, skillName: string) {
    return `./images/characters/${character}/skill/${skillName}.png`
  }

  function skill_tooltip(skill: ISkillInfo) {
    if (skill.type == 1)
      return (
        <div class="tooltip-skill">
          <div class="name">
            {skill.name} Lv {skill.current_LV}
          </div>
          <div class="info text-right">冷却时间:{skill.CD}秒</div>
          <div class="info">学习等级:{+skill.need_level}</div>
          <div class="info">精通等级:{+skill.level_master}</div>
          <div class="info">上限等级:{+skill.level_max}</div>
          <div class="info">技能倍率:{+skill.data}%</div>
        </div>
      )
    else
      return (
        <div class="tooltip-skill">
          <div class="name-p">
            {skill.name} Lv {skill.current_LV}
          </div>
          <div class="info">学习等级:{+skill.need_level}</div>
          <div class="info">精通等级:{+skill.level_master}</div>
          <div class="info">上限等级:{+skill.level_max}</div>
        </div>
      )
  }

  export default defineComponent(() => {
    let basicInfo = ref<ICharacterInfo>({ skillInfo: [], individuation: [] })
    let characterName = ref<string>("")
    const route = useRoute()
    if (typeof route.params.name === "string")
      characterName.value = route.params.name
    onMounted(async () => {
      const characterInfoState = useCharacterStore()
      await characterInfoState.get_character_info(characterName.value)
      basicInfo.value = characterInfoState[characterName.value]
        ?.basicInfo as ICharacterInfo
    })

    const visible = ref(false)
    const showDialog = () => (visible.value = true)

    return () => (
      <div class="pt-8 pb-12 pl-4 character">
        {renderList(basicInfo.value.skillInfo, (skill, index) => (
          <div class="flex">
            <calc-tooltip position="right" offset={5}>
              {{
                default() {
                  return (
                    <img src={skill_icon(characterName.value, skill.name)} />
                  )
                },
                popper() {
                  return skill_tooltip(skill)
                }
              }}
            </calc-tooltip>
          </div>
        ))}
      </div>
    )
  })
</script>

<style lang="scss">
  .character {
    background-color: gray;
  }
</style>
