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


def filter_states(patch, filter_type, entity_index):
    """
    Updates the list of filtered states from a filter index.
    """

    # Create an unfiltered list of all states if there is no filter.
    if filter_type == FILTER_TYPE_NONE:
        state_index = 0
        state_indices = []
        states = []

        for state in patch.states:
            state_indices.append(state_index)
            states.append(state)
            state_index += 1

        return state_indices, states

    # Create an initial list of states belonging to the filtered entity.
    if filter_type == FILTER_TYPE_UNUSED:
        states_list = _get_used_states(patch)
    elif filter_type == FILTER_TYPE_THING:
        states_list = _get_thing_states(patch.things[entity_index])
    elif filter_type == FILTER_TYPE_WEAPON:
        states_list = _get_weapon_states(patch.weapons[entity_index])
    else:
        states_list = []

    # Look for next state and possible next states until all known states have been visited.
    visited = set(states_list)
    for state_index in states_list:

        next_state_index = patch.states[state_index]['nextState']
        if next_state_index >= 0 and next_state_index not in visited:
            states_list.append(next_state_index)
            visited.add(next_state_index)

        # Action-specific state jumps.
        # Randomly jump to state in param1
        state = patch.states[state_index]
        if state['action'] == 'RandomJump':
            jump_index = state['unused1']
            if jump_index >= 0 and jump_index not in visited:
                states_list.append(jump_index)
                visited.add(jump_index)

    # If a unused filter type is active, invert the list to reveal unused states.
    if filter_type == FILTER_TYPE_UNUSED:
        states_list = []
        for index in range(len(patch.states)):
            if index not in visited:
                states_list.append(index)
    else:
        states_list = sorted(states_list)

    states = []
    state_indices = states_list
    for index in states_list:
        states.append(patch.states[index])

    return state_indices, states


def _get_used_states(patch):
    """
    Returns a new states list with all used states marked.
    """

    states_list = []

    # Add thing states.
    for thing in patch.things:
        states_list.extend(_get_thing_states(thing))

    # Add weapon states.
    for weapon in patch.weapons:
        states_list.extend(_get_weapon_states(weapon))

        # Add plasma rifle muzzle flash jitter states.
        if patch.engine.hacks['plasmaFlashStateJitter']:
            states_list.extend(_get_hack_states(patch, weapon))

    # Add used states from the engine table.
    for state_index in patch.engine.used_states:
        states_list.append(state_index)

    return states_list


def _get_hack_states(patch, weapon):
    """
    Adds states that belong to a hack setting.
    """

    states = []

    action_plasma = patch.engine.get_action_key_from_name('FirePlasma')
    action_cgun = patch.engine.get_action_key_from_name('FireCGun')

    # If a weapon uses the plasma or chaingun firing action, mark it's 2nd muzzle state as used.
    plasma_action = patch.engine.get_action_from_key(action_plasma)['name']
    cg_action = patch.engine.get_action_from_key(action_cgun)['name']

    fire_state = weapon['stateFire']
    action = patch.states[fire_state]['action']
    if action == plasma_action or action == cg_action:
        muzzle_state = weapon['stateMuzzle']
        states.append(muzzle_state + 1)

    return states


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
