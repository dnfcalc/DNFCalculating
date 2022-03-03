<template>
  <div class="home bg-cover w-full h-full p-5 overflow-auto">
    <template v-for="(sub, index) in adventureinfo">
      <div class="flex flex-row">
        <div
          class="job-icon-box w-30 h-20 flex flex-wrap justify-center items-center relative bg-no-repeat bg-center"
        >
          <div
            class="w-15 h-15 bg-center bg-no-repeat"
            :style="sub_icon(index)"
          ></div>
          <template v-for="job in sub">
            <div
              class="job-box w-30 h-22.5 m-1 box-border relative duration-300 cursor-pointer"
            >
              <div
                class="job-border w-full h-full absolute z-2 bg-no-repeat"
              ></div>
              <div
                class="job-mask bg-hex-#ffd7002e w-full h-full invisible z-999 absolute"
              ></div>
              <div
                class="absolute bottom-1 w-full text-sm text-center text-hex-#bea347"
              >
                {{ job.显示名称 }}
              </div>
              <div
                class="w-full h-full bg-no-repeat bg-auto bg-clip-content overflow-hidden z-1"
                :style="job_icon(job.序号)"
              ></div>
            </div>
          </template>
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

function sub_icon(sub: number) {
  return {
    backgroundImage: `url(./images/adventure/sub/${sub}.png)`
  }
}

function job_icon(job: string) {
  return {
    backgroundImage: `url(./images/adventure/jobs/${job}.png)`
  }
}

function choose_job(job: string) {
  alert(job)
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
