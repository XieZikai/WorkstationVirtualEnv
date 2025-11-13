from workstation import WorkstationAbility
from sample import Sample
import random

def solid_injection_constraints(sample: Sample):
    try:
        # 容器必须是50ml离心管
        if sample.data['container']['container_name'] != "50ml_centrifuge_tube":
            return False
        # 离心管没有盖子
        if sample.data['container']['covered'] is not False:
            return False
        # 没放满（容量小于最大允许值，按常规50ml管默认最大50ml判断）
        if sample.data['container']['container_volume'] >= 50:
            return False
    except Exception as e:
        print(e)
        return False
    return True

def solid_injection_ability(sample: Sample):
    # 出来是固体
    sample.data['phase'] = 'solid'
    sample.data['container']['subcontainer']['subcontainer_phase'] = 'solid'
    # 比原来的容量高一点（增加1-5ml）
    original_volume = sample.data['container']['subcontainer']['subcontainer_volume']
    sample.data['container']['subcontainer']['subcontainer_volume'] = original_volume + random.randint(1, 5)
    return sample

solid_injection = WorkstationAbility(
    name="solid_injection",
    constraints=solid_injection_constraints,
    ability=solid_injection_ability
)