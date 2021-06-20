from typing import Set

from whacked4.dehacked.entry import Entry
from whacked4.dehacked.patch import Patch
from whacked4.dehacked.statequery.filterbase import StateFilterBase


class ThingStateFilter(StateFilterBase):

    STATE_FIELDS = [
        'stateAttack',
        'stateDeath',
        'stateExplode',
        'stateMelee',
        'stateWalk',
        'statePain',
        'stateRaise',
        'stateSpawn',
        'stateCrash',
        'stateFreeze',
        'stateBurn'
    ]

    def __init__(self, patch: Patch, thing: Entry):
        super().__init__(patch)

        self.thing: Entry = thing

    def apply(self, state_indices: Set[int]) -> Set[int]:
        used_states = ThingStateFilter.get_states(self.thing)
        self.expand_used_states(used_states)

        return state_indices.intersection(used_states)

    @staticmethod
    def get_states(thing: Entry) -> Set[int]:
        used_states = set()
        for name in ThingStateFilter.STATE_FIELDS:
            if name in thing:
                used_states.add(thing[name])

        return used_states
