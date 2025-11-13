from workstation import WorkstationAbility
from sample import Sample

def storage_rack_constraints(sample: Sample):
    try:
        # 离心管架
        if sample.data['container']['container_name'] != "rack":
            return False
        # 离心管（支持50ml和15ml）
        valid_tubes = ['50ml_centrifuge_tube', '15ml_centrifuge_tube']
        if sample.data['container']['subcontainer']['subcontainer_name'] not in valid_tubes:
            return False
        # 离心管有1-10个
        if not (1 <= sample.data['container']['subcontainer']['subcontainer_number'] <= 10):
            return False
        # 固液混合物或者液体
        valid_phases = ['liquid', 'slurry']
        if sample.data['container']['subcontainer']['subcontainer_phase'] not in valid_phases:
            return False
    except Exception as e:
        print(e)
        return False
    return True

def storage_rack_ability(sample: Sample):
    # 静置（不修改状态）
    # 温度到20度
    sample.data['temperature'] = 20
    return sample

storage_rack = WorkstationAbility(
    name="storage_rack",
    constraints=storage_rack_constraints,
    ability=storage_rack_ability
)