export interface ICharacterInfo {
  name?: string
  character?: string
  characterType?: string
  classChange?: string
  weaponType?: string[]
  carryType?: string[]
  armor?: string
  armor_mastery?: string[]
  buff_ratio?: number
  skillInfo: ISkillInfo[]
  fuwen?: string[]
  hushi?: string[]
  individuation: IIndividuation[]
}

export interface ISkillInfo {
  name: string
  type: number
  need_level: number
  level_master: number
  level_max: number
  CD: number
  current_LV: number
  data: number
}

export interface IIndividuation {
  type: string
  value: string
  items: string[]
  row?: number
  column?: number
  key?: number
}
