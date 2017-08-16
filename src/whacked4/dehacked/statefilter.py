#!/usr/bin/env python
#coding=utf8

"""
This module contains functionality to filter a list of states by certain criteria.
"""

# Filter types.
FILTER_TYPE_NONE = 0x0
FILTER_TYPE_UNUSED = 0x1
FILTER_TYPE_THING = 0x2
FILTER_TYPE_WEAPON = 0x4


class StateFilter(object):
    """
    A state filter. Can filter by thing states, weapon states and unused states.
    """

    def __init__(self, patch):
        self.patch = patch

        # All available filters.
        self.filters = None
        self.build_filters()

        # A list of filtered state indices and states.
        # These lists should always be synchronized.
        self.state_indices = []
        self.states = []

        # Currently active filters.
        self.filter_type = None
        self.filter_index = -1

    def build_filters(self):
        """
        Builds a list of available filters.
        """

        self.filters = []

        # Add common filters first.
        self.filters.append({
            'name': '',
            'type': FILTER_TYPE_NONE,
            'index': -1
        })
        self.filters.append({
            'name': 'Unused',
            'type': FILTER_TYPE_UNUSED,
            'index': -1
        })

        # Add thing state filters.
        for index in range(len(self.patch.things.names)):
            self.filters.append({
                'name': self.patch.things.names[index],
                'type': FILTER_TYPE_THING,
                'index': index
            })

        # Add weapon state filters.
        for index in range(len(self.patch.weapons.names)):
            self.filters.append({
                'name': self.patch.weapons.names[index],
                'type': FILTER_TYPE_WEAPON,
                'index': index
            })

    def update(self, index):
        """
        Updates the list of filtered states from a filter index.
        """

        filter_data = self.filters[index]
        self.filter_type = filter_data['type']
        self.filter_index = filter_data['index']

        # Create an unfiltered list of all states if there is no filter.
        if self.filter_type == FILTER_TYPE_NONE:
            state_index = 0
            for state in self.patch.states:
                self.state_indices.append(state_index)
                self.states.append(state)
                state_index += 1

            return

        # Create an initial list of states belonging to the filtered entity.
        if self.filter_type == FILTER_TYPE_UNUSED:
            states_list = self.get_used_states()
        elif self.filter_type == FILTER_TYPE_THING:
            states_list = self.get_thing_states(self.filter_index)
        elif self.filter_type == FILTER_TYPE_WEAPON:
            states_list = self.get_weapon_states(self.filter_index)
        else:
            states_list = []

        # Look for next state and possible next states until all known states have been visited.
        visited = set(states_list)
        for state_index in states_list:

            next_state_index = self.patch.states[state_index]['nextState']
            if next_state_index >= 0 and next_state_index not in visited:
                states_list.append(next_state_index)
                visited.add(next_state_index)

            # Action-specific state jumps.
            # Randomly jump to state in param1
            state = self.patch.states[state_index]
            if state['action'] == 'RandomJump':
                jump_index = state['unused1']
                if jump_index >= 0 and jump_index not in visited:
                    states_list.append(jump_index)
                    visited.add(jump_index)

        # If a unused filter type is active, invert the list to reveal unused states.
        if self.filter_type == FILTER_TYPE_UNUSED:
            states_list = []
            for index in range(len(self.patch.states)):
                if index not in visited:
                    states_list.append(index)
        else:
            states_list = sorted(states_list)

        self.states = []
        self.state_indices = states_list
        for index in states_list:
                self.states.append(self.patch.states[index])

    def get_weapon_states(self, weapon_index):
        """
        Returns a new states list with the states for a particular weapon index.
        """

        weapon = self.patch.weapons[weapon_index]
        states_list = _get_weapon_states(weapon)

        # Add plasma rifle muzzle flash jitter states.
        if self.patch.engine.hacks['plasmaFlashStateJitter']:
            states_list.extend(self.get_hack_states(weapon))

        return states_list

    def get_thing_states(self, thing_index):
        """
        Returns a new states list with the states for a particular thing index.
        """

        thing = self.patch.things[thing_index]
        states_list = _get_thing_states(thing)

        return states_list

    def get_used_states(self):
        """
        Returns a new states list with all used states marked.
        """

        states_list = []

        # Add thing states.
        for thing in self.patch.things:
            states_list.extend(_get_thing_states(thing))

        # Add weapon states.
        for weapon in self.patch.weapons:
            states_list.extend(_get_weapon_states(weapon))

            # Add plasma rifle muzzle flash jitter states.
            if self.patch.engine.hacks['plasmaFlashStateJitter']:
                states_list.extend(self.get_hack_states(weapon))

        # Add used states from the engine table.
        for state_index in self.patch.engine.used_states:
            states_list.append(state_index)

        return states_list

    def get_hack_states(self, weapon):
        """
        Adds states that belong to a hack setting.
        """

        states = []

        action_plasma = self.patch.engine.get_action_key_from_name('FirePlasma')
        action_cgun = self.patch.engine.get_action_key_from_name('FireCGun')

        # If a weapon uses the plasma or chaingun firing action, mark it's 2nd muzzle state as used.
        plasma_action = self.patch.engine.get_action_from_key(action_plasma)['name']
        cg_action = self.patch.engine.get_action_from_key(action_cgun)['name']

        fire_state = weapon['stateFire']
        action = self.patch.states[fire_state]['action']
        if action == plasma_action or action == cg_action:
            muzzle_state = weapon['stateMuzzle']
            states.append(muzzle_state + 1)

        return states

    def find_index(self, filter_type, item_index):
        """
        Returns the index of a filter by specifying a type and item index. Returns -1 if no index could be found.
        """

        index = 0
        for filter_data in self.filters:
            if filter_data['type'] == filter_type and filter_data['index'] == item_index:
                return index

            index += 1

        return -1


def _get_thing_states(thing):
    """
    Adds states that belong to a thing.
    """

    names = [
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

    states = []
    for name in names:
        if thing[name] > 0:
            states.append(thing[name])

    return states


def _get_weapon_states(weapon):
    """
    Adds states that belong to a weapon.
    """

    names = [
        'stateBob',
        'stateDeselect',
        'stateFire',
        'stateMuzzle',
        'stateSelect'
    ]

    states = []
    for name in names:
        if weapon[name] > 0:
            states.append(weapon[name])

    return states
