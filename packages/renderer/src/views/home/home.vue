<script lang="tsx">
  import { IAdventureInfo } from "@/api/info/type"
  import { useBasicInfoStore } from "@/store"
  import { defineComponent, onMounted, ref, renderList } from "vue"

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
  export default defineComponent(() => {
    const adventureinfo = ref<IAdventureInfo[][]>([])
    onMounted(async () => {
      const basicInfoState = useBasicInfoStore()
      await basicInfoState.get_basic_info()
      adventureinfo.value = basicInfoState.adventureinfo as IAdventureInfo[][]
    })

    return () => (
      <div class="bg-cover h-full w-full p-5 home overflow-auto">
        {renderList(adventureinfo.value, (sub, index) => (
          <div class="flex flex-row">
            <div class="bg-no-repeat bg-center flex flex-wrap h-25 w-30 job-icon-box justify-center items-center relative">
              <div
                class="bg-center bg-no-repeat h-22.5 w-30"
                style={sub_icon(index)}
              ></div>
            </div>
            {renderList(sub, job => (
              <div class="cursor-pointer h-22.5 m-1 w-30 duration-300 job-box box-border relative">
                <div class="bg-no-repeat h-full w-full z-2 job-border absolute"></div>
                <div class="h-full bg-hex-ffd7002e w-full z-999 job-mask invisible absolute"></div>
                <div class="text-sm text-center w-full bottom-1 text-hex-bea347 absolute">
                  {job.显示名称}
                </div>
                <div
                  class="bg-no-repeat bg-auto bg-clip-content h-full w-full z-1 overflow-hidden"
                  style={job_icon(job.序号)}
                ></div>
              </div>
            ))}
          </div>
        ))}
      </div>
    )
  })
</script>

<style lang="scss">
  .home {
    background-image: url(./images/adventure/bg.png);
    background-repeat: no-repeat;
    background-size: 865px 100%;

    .job-icon-box {
      background-image: url(./images/adventure/flash.png);
    }

    .job-box {
      .job-border {
        background-image: url(./images/adventure/border.png);
      }

      &:hover {
        .job-mask {
          visibility: visible;
        }
      }
    }
  }
</style>
