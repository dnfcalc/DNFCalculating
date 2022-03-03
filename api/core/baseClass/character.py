from core.baseClass.skill import 技能
class Character:
  # 实际名称
  name = ''
  # 角色
  character:str = ''
  # 输出/奶
  characterType = ''
  # 转职
  classChange = ''
  # 武器类型
  weaponType = []
  # 输出类型选择，默认类型为第一个
  carryType = []
  # 防具类型
  armor =''
  # 防具类型精通，智力、力量
  armor_mastery = []
  # buff倍率
  buff_ratio = 1.0
  # 技能列表
  skillInfo = []
  # 个性化设置，技能选项等
  individuation=[]
  # 护石及符文信息
  hushi = []
  fuwen = []
  # 药剂等相关信息设置

  def set_skill_info(self,SkillClassList:技能,fuwen_except=[]):
    self.skillInfo = []
    self.fuwen = []
    self.hushi = []
    for skill in SkillClassList:
      skill.等级 = skill.基础等级
      self.skillInfo.append({
        "name":skill.名称,
        "type":skill.是否有伤害,
        "need_level":skill.所在等级,
        "level_master":skill.等级精通,
        "CD":0 if not skill.是否有伤害 else skill.CD,
        "current_LV":skill.基础等级,
        "data": 0 if not skill.是否有伤害 else skill.等效百分比('')
      })
      if skill.是否有伤害 == 1 and skill.是否有护石 == 1:
        self.hushi.append(skill.名称)
      if skill.所在等级 >= 20 and skill.所在等级 <= 80 and skill.所在等级 != 50 and skill.是否有伤害 == 1 and skill.名称 not in fuwen_except:
        self.fuwen.append(skill.名称)

  def set_individuation(self):
    pass
