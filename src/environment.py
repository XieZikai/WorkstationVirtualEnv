from workstation import Workstation, WorkstationAbility
from sample import Sample
from copy import deepcopy


class Environment:
    def __init__(self,
                 workstation_workflow: list[WorkstationAbility]):
        self.workstation_workflow = workstation_workflow

    def __call__(self, sample: Sample):
        sample_copy = deepcopy(sample)
        for ability in self.workstation_workflow:
            try:
                sample_copy = ability(sample_copy)
                print(f"Sample passing workstation ability '{ability.name}'")
            except Exception as e:
                print(f"Error in {ability.__class__.__name__}: {e}")
                return None
        return sample_copy
