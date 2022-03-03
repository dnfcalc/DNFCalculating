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
  # 药剂等相关信息设置

  def get_skill_info(self,SkillClassList):
    self.skillInfo = []
    for skill in SkillClassList:
      self.skillInfo.append({
        "name":skill.名称,
        "type":skill.是否有伤害
      })
