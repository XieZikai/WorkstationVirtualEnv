from workstation import WorkstationAbility
from sample import Sample

def material_station_constraints(sample: Sample):
    try:
        # 物料站无额外限制（按常规兼容所有离心管架配置）
        if sample.data['container']['container_name'] != "rack":
            return False
        # 离心管有1-10个
        if not (1 <= sample.data['container']['subcontainer']['subcontainer_number'] <= 10):
            return False
        # 支持常见离心管类型
        valid_tubes = ['50ml_centrifuge_tube', '15ml_centrifuge_tube']
        if sample.data['container']['subcontainer']['subcontainer_name'] not in valid_tubes:
            return False
    except Exception as e:
        print(e)
        return False
    return True

def material_station_ability(sample: Sample):
    # 物料站能力：提供物料（不修改样品状态，仅完成流程衔接）
    return sample

material_station = WorkstationAbility(
    name="material_station",
    constraints=material_station_constraints,
    ability=material_station_ability
)