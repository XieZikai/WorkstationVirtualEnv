from workstation import WorkstationAbility
from sample import Sample
import random

# 能力1：把溶剂烘干
def oven_dry_constraints(sample: Sample):
    try:
        # 离心管架进样
        if sample.data['container']['container_name'] != "rack":
            return False
        # 架子上有50ml离心管
        if sample.data['container']['subcontainer']['subcontainer_name'] != "50ml_centrifuge_tube":
            return False
        # 离心管有1-10个
        if not (1 <= sample.data['container']['subcontainer']['subcontainer_number'] <= 10):
            return False
        # 温度低于200度
        if sample.data['temperature'] >= 200:
            return False
        # 没装满（按50ml管最大50ml判断）
        if sample.data['container']['subcontainer']['subcontainer_volume'] >= 50:
            return False
        # 没有盖子
        if sample.data['container']['subcontainer']['covered'] is not False:
            return False
        # 离心管中是液体或者固液混合物
        valid_phases = ['liquid', 'slurry']
        if sample.data['container']['subcontainer']['subcontainer_phase'] not in valid_phases:
            return False
    except Exception as e:
        print(e)
        return False
    return True

def oven_dry_ability(sample: Sample):
    # 出来全都是固体
    sample.data['phase'] = 'solid'
    sample.data['container']['subcontainer']['subcontainer_phase'] = 'solid'
    # 温度达到50～100度
    sample.data['temperature'] = random.randint(50, 100)
    # 容量减少（减少30%-50%）
    original_volume = sample.data['container']['subcontainer']['subcontainer_volume']
    sample.data['container']['subcontainer']['subcontainer_volume'] = int(original_volume * random.uniform(0.5, 0.7))
    return sample

# 能力2：升温反应加热
def oven_heat_constraints(sample: Sample):
    try:
        # 离心管架进样
        if sample.data['container']['container_name'] != "rack":
            return False
        # 架子上有50ml离心管
        if sample.data['container']['subcontainer']['subcontainer_name'] != "50ml_centrifuge_tube":
            return False
        # 离心管有1-10个
        if not (1 <= sample.data['container']['subcontainer']['subcontainer_number'] <= 10):
            return False
        # 温度低于200度
        if sample.data['temperature'] >= 200:
            return False
        # 没装满（按50ml管最大50ml判断）
        if sample.data['container']['subcontainer']['subcontainer_volume'] >= 50:
            return False
        # 有盖子
        if sample.data['container']['subcontainer']['covered'] is not True:
            return False
        # 离心管中是液体或者固液混合物
        valid_phases = ['liquid', 'slurry']
        if sample.data['container']['subcontainer']['subcontainer_phase'] not in valid_phases:
            return False
    except Exception as e:
        print(e)
        return False
    return True

def oven_heat_ability(sample: Sample):
    # 把容器加热到100～200度
    sample.data['temperature'] = random.randint(100, 200)
    return sample

# 注册两个能力
oven_dry = WorkstationAbility(
    name="oven_dry",
    constraints=oven_dry_constraints,
    ability=oven_dry_ability
)

oven_heat = WorkstationAbility(
    name="oven_heat",
    constraints=oven_heat_constraints,
    ability=oven_heat_ability
)