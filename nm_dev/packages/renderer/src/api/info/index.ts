import hyRequest from '../index'
import { IAdventureInfo } from './type'
import { IDataType } from '../types'

enum InfoAPI {
  AdventureInfo = '/info/adventureinfo',
  BlackList = '/info/blacklist'
}

export function GetAdventureInfo() {
  return hyRequest.get<IDataType<IAdventureInfo[][]>>({
    url: InfoAPI.AdventureInfo
  })
}
