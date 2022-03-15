<script lang="tsx">
  /**
   * @Author: Umi
   * @Date:   2022/3/13 16:33:00
   * @Last Modified by:   Umi
   * @Last Modified time: 2022/3/13 16:33:00
   * 人物面板
   */
  import { defineComponent, h, renderSlot } from "vue"
  import EquipmentSlot from "@/components/calc/status/equipment_slot.vue"
  export default defineComponent({
    name: "character-status",
    props: {},
    components: { EquipmentSlot },
    setup(props, { slots }) {
      return () => {}
    }
  })
</script>

<template>
  <div>cha12313a</div>
  <equipment-slot type="shoulder" id="0"></equipment-slot>
</template>
