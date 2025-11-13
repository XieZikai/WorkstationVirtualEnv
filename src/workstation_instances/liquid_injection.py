from workstation import WorkstationAbility
from sample import Sample
import random

def liquid_injection_constraints(sample: Sample):
    try:
        # 容器必须是离心管架
        if sample.data['container']['container_name'] != "rack":
            return False
        # 离心管架上是50ml离心管
        if sample.data['container']['subcontainer']['subcontainer_name'] != "50ml_centrifuge_tube":
            return False
        # 离心管有1-10个
        if not (1 <= sample.data['container']['subcontainer']['subcontainer_number'] <= 10):
            return False
        # 少于30ml
        if sample.data['container']['subcontainer']['subcontainer_volume'] >= 30:
            return False
    except Exception as e:
        print(e)
        return False
    return True

def liquid_injection_ability(sample: Sample):
    # 可以加盖子
    sample.data['container']['subcontainer']['covered'] = True
    # 出来是液体（随机纯液体或悬浊液）
    if sample.data['container']['subcontainer']['subcontainer_volume'] == 0:
        sample.data['container']['subcontainer']['subcontainer_phase'] = 'liquid'
    if sample.data['container']['subcontainer']['subcontainer_phase'] == 'solid':
        sample.data['container']['subcontainer']['subcontainer_phase'] = 'suspension'
    # sample.data['container']['subcontainer']['subcontainer_phase'] = sample.data['phase']
    # 比原来多一点（增加1-3ml）
    original_volume = sample.data['container']['subcontainer']['subcontainer_volume']
    new_volume = original_volume + random.randint(1, 3)
    # 确保出来后少于30ml
    sample.data['container']['subcontainer']['subcontainer_volume'] = min(new_volume, 29)
    return sample

liquid_injection = WorkstationAbility(
    name="liquid_injection",
    constraints=liquid_injection_constraints,
    ability=liquid_injection_ability
)