from workstation import WorkstationAbility
from sample import Sample

def stirring_constraints(sample: Sample):
    try:
        # 离心管架
        if sample.data['container']['container_name'] != "rack":
            return False
        # 50ml离心管
        if sample.data['container']['subcontainer']['subcontainer_name'] != "50ml_centrifuge_tube":
            return False
        # 离心管有1-10个
        if not (1 <= sample.data['container']['subcontainer']['subcontainer_number'] <= 10):
            return False
        # 液体或者固液混合
        valid_phases = ['liquid', 'slurry']
        if sample.data['container']['subcontainer']['subcontainer_phase'] not in valid_phases:
            return False
        # 盖子没盖住
        if sample.data['container']['subcontainer']['covered'] is not False:
            return False
        # 必须要有样品（3ml以上）
        if sample.data['container']['subcontainer']['subcontainer_volume'] <= 3:
            return False
    except Exception as e:
        print(e)
        return False
    return True

def stirring_ability(sample: Sample):
    # 搅拌（不做任何处理，仅保留能力结构）
    return sample

stirring = WorkstationAbility(
    name="stirring",
    constraints=stirring_constraints,
    ability=stirring_ability
)