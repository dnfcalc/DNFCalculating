import hyRequest from "../index"
import { ICharacterInfo } from "./type"
import { IDataType } from "../types"

enum CharacterAPI {
  // /info/characterInfo/重霄·弹药专家·女
  CharacterInfo = "/info/characterInfo/"
}

export function GetCharacterInfo(character: string) {
  return hyRequest.get<IDataType<ICharacterInfo>>({
    url: CharacterAPI.CharacterInfo + character
  })
}
