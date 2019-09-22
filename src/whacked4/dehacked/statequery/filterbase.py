from typing import Set

from whacked4.dehacked.patch import Patch


class StateFilterBase:

    def __init__(self, patch: Patch):
        self.patch: Patch = patch

    def apply(self, state_indices: Set[int]) -> Set[int]:
        pass

    def expand_used_states(self, used_states):
        previous_len = -1

        new_states = used_states.copy()
        while len(used_states) != previous_len:
            new_states = self.__get_states_used_by(new_states)
            previous_len = len(used_states)
            used_states.update(new_states)

    def __get_states_used_by(self, states):
        used_states = set()
        for state_index in states:
            state = self.patch.states[state_index]

            next_state_index = state['nextState']
            if next_state_index >= 0:
                used_states.add(next_state_index)

            # Randomly jumps to state from param1.
            if state['action'] == 'RandomJump':
                jump_index = state['unused1']
                if jump_index >= 0:
                    used_states.add(jump_index)

        return used_states
