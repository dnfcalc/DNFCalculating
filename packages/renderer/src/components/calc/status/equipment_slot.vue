<script lang="tsx">
  /**
   * @Author: Umi
   * @Date:   2022/3/13 16:33:00
   * @Last Modified by:   Umi
   * @Last Modified time: 2022/3/13 16:33:00
   * 装备槽
   */
  import { defineComponent } from "vue"

  export default defineComponent({
    name: "equipment-slot",
    props: ["type", "id"],
    setup(props, { slots }) {
      return () => {}
    }
  })
</script>

<template>
  equipment12312_slot
  <div class="equipment-slot" :class="type"></div>
</template>

<style lang="scss">
  .equipment-slot {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 32px;
    height: 32px;
    background-color: black;
    color: white;
  }

  .equipment-slot:hover {
    background-image: url("./img/slot-hover.png");
  }

  .belt {
    background-image: url("./img/belt.png");
  }

  .bottom {
    background-image: url("./img/bottom.png");
  }

  .bracelet {
    background-image: url("./img/bracelet.png");
  }

  .earrings {
    background-image: url("./img/earrings.png");
  }

  .magicstones {
    background-image: url("./img/magicstones.png");
  }

  .necklace {
    background-image: url("./img/necklace.png");
  }

  .ring {
    background-image: url("./img/ring.png");
  }

  .shoes {
    background-image: url("./img/shoes.png");
  }

  .top {
    background-image: url("./img/top.png");
  }

  .weapon {
    background-image: url("./img/weapon.png");
  }

  .shoulder {
    background-image: url("./img/shoulder.png");
  }

  .subequipment {
    background-image: url("./img/subequipment.png");
  }

  .title {
    background-image: url("./img/title.png");
  }
</style>
