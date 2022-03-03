<template>
  <div class="home bg-cover w-full h-full p-5 overflow-auto">
    <template v-for="(sub, index) in adventureinfo">
      <div class="flex flex-row">
        <div
          class="job-icon-box w-30 h-20 flex flex-wrap justify-center items-center relative bg-no-repeat bg-center"
        >
          <div
            class="w-12 h-12 bg-center bg-no-repeat"
            :style="sub_icon(index)"
          ></div>
          <div
            class="absolute w-30 text-sm text-center font-bold bottom-0 text-color"
          >
            {{ index }}
          </div>
        </div>
      </div>
    </template>
  </div>
</template>
<script lang="ts" setup>
import { useBasicInfoStore } from '../../store'
const basicInfoState = useBasicInfoStore()
await basicInfoState.get_basic_info()
const adventureinfo = basicInfoState.adventureinfo

function sub_icon(num: number) {
  return {
    backgroundImage: `url(./images/adventure/sub/${num}.png)`
  }
}
</script>

<style lang="scss">
.home {
  background-image: url(./images/adventure/bg.png);

  .job-icon-box {
    background-image: url(./images/adventure/flash.png);
  }

  .job-box {
    .job-border {
      background-image: url(@/assets/img/job_border.png);
    }

    &:hover {
      .job-mask {
        visibility: visible;
      }
    }
  }
}
</style>
