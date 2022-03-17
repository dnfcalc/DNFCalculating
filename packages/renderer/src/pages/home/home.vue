<script lang="tsx">
  import { IAdventureInfo } from "@/api/info/type"
  import { useBasicInfoStore } from "@/store"
  import { defineComponent, onMounted, ref, renderList } from "vue"
  import { useRouter } from "vue-router"
  import openURL from "@/utils/openURL"

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

  export default defineComponent(() => {
    const adventureinfo = ref<IAdventureInfo[][]>([])
    const router = useRouter()
    onMounted(async () => {
      const basicInfoState = useBasicInfoStore()
      await basicInfoState.get_basic_info()
      adventureinfo.value = basicInfoState.adventureinfo as IAdventureInfo[][]
    })

    // 获取角色相关信息，判定是否开放
    function choose_job(alter: string) {
      return () => {
        if (alter == "空") return
        if (alter === "重霄·弹药专家·女") {
          openURL(router, "/equipment/" + alter, { width: 1000, height: 500 })
        } else {
          openURL(router, "/show", { width: 800, height: 800 })
        }
      }
      // router.push("/character/" + alter)
    }

    return () => (
      <div class="bg-cover bg-no-repeat pt-8 pb-12 pl-4 home">
        {renderList(adventureinfo.value, (sub, index) => (
          <div class="flex flex-row">
            <div class="bg-no-repeat bg-center flex flex-wrap h-25 w-30 job-icon-box justify-center items-center relative">
              <div
                class="bg-center bg-no-repeat h-22.5 w-30"
                style={sub_icon(index)}
              ></div>
            </div>
            {renderList(sub, job => (
              <div
                onClick={choose_job(job.类名)}
                class="cursor-pointer h-22.5 m-1 w-30 duration-300 job-box box-border relative"
              >
                {!!job.显示名称 && (
                  <>
                    <div class="bg-no-repeat h-full w-full z-2 duration-200 job-border absolute hover:bg-hex-ffd7002e"></div>
                    <div class="text-xs text-center w-full bottom-1 text-hex-bea347 absolute">
                      {job.显示名称}
                    </div>
                  </>
                )}
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
    background-image: url(./images/adventure/bg.jpg);
    background-size: 100% 100%;

    .job-icon-box {
      background-image: url(./images/adventure/flash.png);
    }

    .job-box {
      .job-border {
        background-image: url(./images/adventure/border.png);
      }
    }
  }
</style>
