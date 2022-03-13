<script lang="tsx">
  import { defineComponent, onMounted, ref, renderList, reactive } from "vue"
  import { useCharacterStore } from "@/store"
  import { ICharacterInfo } from "@/api/character/type"
  import { useRoute } from "vue-router"

  export default defineComponent(() => {
    const route = useRoute()
    return () => (
      <div>
        hello,
        {route.params.characterName}
      </div>
    )
  })
</script>
