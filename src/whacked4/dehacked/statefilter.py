from typing import List, Set

from whacked4.dehacked.entry import Entry
from whacked4.dehacked.patch import Patch
from whacked4.dehacked.table import Table


class StateFilterBase:

    def __init__(self, patch: Patch):
        self.patch: Patch = patch

    def apply(self, state_indices: Set[int]) -> Set[int]:
        pass

    def expand_used_states(self, used_states):
        for state_index in used_states:
            state = self.patch.states[state_index]

            next_state_index = state['nextState']
            if next_state_index >= 0:
                used_states.add(next_state_index)

            # Randomly jumps to state from param1.
            if state['action'] == 'RandomJump':
                jump_index = state['unused1']
                if jump_index >= 0:
                    used_states.add(jump_index)


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
            if name in thing and thing[name] > 0:
                used_states.add(thing[name])

        return used_states


class WeaponStateFilter(StateFilterBase):

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
        used_states = set()
        for name in WeaponStateFilter.STATE_FIELDS:
            if name in weapon and weapon[name] > 0:
                used_states.add(weapon[name])

        return used_states

    @staticmethod
    def process_states(patch: Patch, weapon: Entry, state_indices: Set[int]):

        for state_index in state_indices:
            action_key = patch.states[state_index]['action']
            action = patch.engine.actions[action_key]

            if action.usesExtraFlashState:
                muzzle_state = weapon['stateMuzzle']
                state_indices.add(muzzle_state + 1)


class UnusedStateFilter(StateFilterBase):

    def apply(self, state_indices: Set[int]) -> Set[int]:
        used_states = set()

        # Add all states used by things.
        thing_states = set()
        for thing in self.patch.things:
            thing_states.update(ThingStateFilter.get_states(thing))
        self.expand_used_states(thing_states)
        used_states.update(thing_states)

        # Add all states used by weapons. Weapon states are further processed per weapon to take care of the
        # usesExtraFlashState property of some actions.
        for weapon in self.patch.weapons:
            weapon_states = WeaponStateFilter.get_states(weapon)
            self.expand_used_states(weapon_states)
            WeaponStateFilter.process_states(self.patch, weapon, weapon_states)
            used_states.update(weapon_states)

        # Add states that are hardcoded by the engine.
        engine_used_states = set(self.patch.engine.used_states)
        self.expand_used_states(engine_used_states)
        used_states.update(engine_used_states)

        return state_indices.difference(used_states)


class StateSortBase:

    def __init__(self, patch: Patch):
        self.patch: Patch = patch

    def apply(self, state_indices: List[int]) -> List[int]:
        pass


class StateIndexSorter(StateSortBase):

    def apply(self, state_indices: List[int]) -> List[int]:
        return sorted(state_indices)


class StateFilterResult:

    def __init__(self, state_table: Table, state_indices: List[int]):
        self.state_table: Table = state_table
        self.state_indices: List[int] = state_indices

    def get_state_for_item_index(self, index: int) -> Entry:
        return self.state_table[self.state_indices[index]]


class StateFilterQuery:

    def __init__(self, patch):
        self.patch: Patch = patch

        self.state_filters: List[StateFilterBase] = []
        self.state_sorters: List[StateSortBase] = []

    def filter(self, state_filter: StateFilterBase):
        self.state_filters.append(state_filter)
        return self

    def sort(self, state_sorter: StateSortBase):
        self.state_sorters.append(state_sorter)
        return self

    def execute(self) -> StateFilterResult:
        state_indices = set(range(len(self.patch.states)))

        for state_filter in self.state_filters:
            state_indices = state_filter.apply(state_indices)

        for state_sorter in self.state_sorters:
            state_indices = state_sorter.apply(state_indices)

        return StateFilterResult(self.patch.states, list(state_indices))
