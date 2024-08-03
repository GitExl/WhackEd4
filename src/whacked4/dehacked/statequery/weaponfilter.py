"""
Weapon state filter.
"""

from typing import Set

from whacked4.dehacked.entry import Entry
from whacked4.dehacked.patch import Patch
from whacked4.dehacked.statequery.filterbase import StateFilterBase


class WeaponStateFilter(StateFilterBase):
    """
    Filter states by weapons that use them.
    """

    STATE_FIELDS = [
        'stateBob',
        'stateDeselect',
        'stateFire',
        'stateMuzzle',
        'stateSelect'
    ]

    def __init__(self, patch: Patch, weapon: Entry):
        super().__init__(patch)

        self.weapon: Entry = weapon

    def apply(self, state_indices: Set[int]) -> Set[int]:
        used_states = WeaponStateFilter.get_states(self.weapon)
        self.expand_used_states(used_states)
        self.process_states(self.patch, self.weapon, used_states)

        return state_indices.intersection(used_states)

    @staticmethod
    def get_states(weapon: Entry) -> Set[int]:
        """
        Returns all state entries used by a weapon entry.

        :param weapon:
        """

        used_states = set()
        for name in WeaponStateFilter.STATE_FIELDS:
            if name in weapon:
                used_states.add(weapon[name])

        return used_states

    @staticmethod
    def process_states(patch: Patch, weapon: Entry, state_indices: Set[int]):
        """
        Expand states based on actions if needed.

        :param patch:
        :param weapon:
        :param state_indices:

        """

        extra_state_indices = set()

        for state_index in state_indices:
            action_key = patch.states[state_index]['action']
            action = patch.engine.actions[action_key]

            if action.uses_extra_flash_state:
                muzzle_state = weapon['stateMuzzle']
                extra_state_indices.add(muzzle_state + 1)

        state_indices.update(extra_state_indices)
