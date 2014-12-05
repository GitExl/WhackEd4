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


class StateFilter:
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
        
        self.state_indices = []
        self.states = []
        
        filter_data = self.filters[index]
        filter_type = filter_data['type']
        filter_index = filter_data['index']
        
        # Create an unfiltered list of all states if there is no filter.
        if filter_type == FILTER_TYPE_NONE:
            state_index = 0
            for state in self.patch.states:
                self.state_indices.append(state_index)
                self.states.append(state)
                state_index += 1
        
        # Create a filtered list.
        else:
            if filter_type == FILTER_TYPE_UNUSED:
                states_list = self.get_unused_states()
            elif filter_type == FILTER_TYPE_THING:
                states_list = self.get_thing_states(filter_index)
            elif filter_type == FILTER_TYPE_WEAPON:
                states_list = self.get_weapon_states(filter_index)
        
            # Keep marking all currently listed states' next state as used until none can be found anymore.
            while True:
                added = False
                
                for index in range(len(states_list)):
                    if states_list[index] == True:
                        next_state = self.patch.states[index]['nextState']
                        if next_state >= 0 and states_list[next_state] == False:
                            states_list[next_state] = True
                            added = True
                        
                        # Action-specific state jumps.
                        # Randomly jump to state in param1
                        state = self.patch.states[index]
                        if state['action'] == 'RandomJump':
                            states_list[state['parameter1']] = True
                    
                if added == False:
                    break
                
            # If a unused filter type is active, invert the list to reveal unused states.
            if filter_type == FILTER_TYPE_UNUSED:
                for index in range(len(states_list)):
                    states_list[index] = not states_list[index]
            
            # Create the final filtered lists.
            for index in range(len(states_list)):
                if states_list[index] == True:
                    self.state_indices.append(index)
                    self.states.append(self.patch.states[index])
    
    
    def get_weapon_states(self, weapon_index):
        """
        Returns a new states list with the states for a particular weapon index.
        """
        
        states_list = [False] * len(self.patch.states)
        
        weapon = self.patch.weapons[weapon_index]
        self.add_weapon_states(states_list, weapon)
        
        # Add plasma rifle muzzle flash jitter states.
        if self.patch.engine.hacks['plasmaFlashStateJitter'] == True:
            self.add_hack_states(states_list, weapon)
            
        return states_list
    
    
    def get_thing_states(self, thing_index):
        """
        Returns a new states list with the states for a particular thing index.
        """
        
        states_list = [False] * len(self.patch.states)
        
        thing = self.patch.things[thing_index]
        self.add_thing_states(states_list, thing)
        
        return states_list

    
    def get_unused_states(self):
        """
        Returns a new states list with all used states marked.
        """
        
        states_list = [False] * len(self.patch.states)
        
        # Add thing states.
        for thing in self.patch.things:
            self.add_thing_states(states_list, thing)
            
        # Add weapon states.
        for weapon in self.patch.weapons:
            self.add_weapon_states(states_list, weapon)
            
            # Add plasma rifle muzzle flash jitter states.
            if self.patch.engine.hacks['plasmaFlashStateJitter'] == True:
                self.add_hack_states(states_list, weapon)
            
        # Add used states from the engine table.
        for state_index in self.patch.engine.used_states:
            states_list[state_index] = True
            
        return states_list
    
        
    def add_hack_states(self, states_list, weapon):
        """
        Adds states that belong to a hack setting.
        """

        # If a weapon uses the plasma or chaingun firing action, mark it's 2nd muzzle state as used.
        plasma_action = self.patch.engine.get_action_from_name('FirePlasma')
        cg_action = self.patch.engine.get_action_from_name('FireCGun')

        fire_state = weapon['stateFire']
        action = self.patch.states[fire_state]['action']
        if action == plasma_action or action == cg_action:
            muzzle_state = weapon['stateMuzzle']
            states_list[muzzle_state + 1] = True

    
    def add_thing_states(self, states_list, thing):
        """
        Adds states that belong to a thing.
        """
        
        states_list[thing['stateAttack']] = True
        states_list[thing['stateDeath']] = True
        states_list[thing['stateExplode']] = True
        states_list[thing['stateMelee']] = True
        states_list[thing['stateWalk']] = True
        states_list[thing['statePain']] = True
        states_list[thing['stateRaise']] = True
        states_list[thing['stateSpawn']] = True
        
        
    def add_weapon_states(self, states_list, weapon):
        """
        Adds states that belong to a weapon.
        """
        
        states_list[weapon['stateBob']] = True
        states_list[weapon['stateDeselect']] = True
        states_list[weapon['stateFire']] = True
        states_list[weapon['stateMuzzle']] = True
        states_list[weapon['stateSelect']] = True
    
    
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