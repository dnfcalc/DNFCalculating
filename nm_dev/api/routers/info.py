from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
from utils.apiTools import reponse, Return
from core.response import sundryInfo,characterInfo

infoRouter = APIRouter()


class adventureinfo(BaseModel):
    职业系: str
    转职名称: str
    一次觉醒: str
    二次觉醒: str
    三次觉醒: str
    显示名称: str
    类名: str
    类名2: str
    序号: str
    作者: str
    时间: str
    备注: str


@infoRouter.get(path='/adventureinfo', response_model=Return[List[List[adventureinfo]]])
async def get_adventure_info():
    return reponse(data=sundryInfo.get_adventure_info())


class noteice(BaseModel):
    time: str
    info: str


@infoRouter.get(path='/notice', response_model=Return[noteice])
async def get_notice():
    return reponse(data=sundryInfo.get_notice())


@infoRouter.get(path='/blacklistlist', response_model=Return[dict])
async def get_blacklistlist():
    return reponse(data=sundryInfo.get_blacklistlist())

class characterSkillInfo(BaseModel):
    # 技能信息
    skillInfo:dict
    # 个性化设置，技能选项等
    individuation:dict
    # 护石及符文信息
    # 药剂等相关信息设置

@infoRouter.get(path='/characterInfo/{character_name}')
async def get_character_info(character_name : str):
  return reponse(data=characterInfo.get_character_info(character_name))