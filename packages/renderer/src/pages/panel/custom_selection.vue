<script lang="tsx">
  import { defineComponent, onMounted, ref, renderList, reactive } from "vue"
  import { useCharacterStore } from "@/store"
  import { ICharacterInfo } from "@/api/character/type"
  import { useRoute } from "vue-router"
  import characterStatus from "@/components/calc/status/status.vue"
  export default {
    components: {
      characterStatus
    }
  }
</script>

<template>
  <div> custom-selection </div>
  <character-status></character-status>
</template>
