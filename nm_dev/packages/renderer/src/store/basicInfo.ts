import { defineStore } from 'pinia'
import { GetAdventureInfo } from '../api/info'
import { IAdventureInfo } from '../api/info/type'

export interface BasicInfoState {
  // 冒险团信息
  adventureinfo?: IAdventureInfo[][]
  // 版本信息
  version?: string
  // 用户识别码
  UID?: string
  // 黑名单
  blacklist?: any
  // 通知信息
  noticeInfo?: any
}

export const useBasicInfoStore = defineStore('BasicInfo', {
  state(): BasicInfoState {
    return {}
  },
  getters: {},
  actions: {
    async get_basic_info() {
      const adventure_list = (await GetAdventureInfo())?.data
      const black_list = null
      const notice_info = null
      this.adventureinfo = adventure_list
      this.version = '0.0.0.0'
      this.UID = '西瓜°'
      this.blacklist = black_list
      this.noticeInfo = notice_info
    }
  }
})
