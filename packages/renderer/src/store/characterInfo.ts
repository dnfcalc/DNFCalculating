import { defineStore } from "pinia"
import { GetCharacterInfo } from "../api/character"
import { ICharacterInfo } from "../api/character/type"

export interface CharacterInfo {
  // 类名
  name?: string
  // 基础信息
  basicInfo?: ICharacterInfo
  // 存档信息
  storeInfo?: any
}

export type CharacterState = Record<string, CharacterInfo>

export const useCharacterStore = defineStore("CharacterInfo", {
  state(): CharacterState {
    return {}
  },
  getters: {},
  actions: {
    async get_character_info(char: string) {
      if (!this[char] && this[char] != undefined) return
      this[char] = {}
      const character_info = (await GetCharacterInfo(char))?.data
      this[char].basicInfo = character_info
      this[char].name = char
    }
  }
})
