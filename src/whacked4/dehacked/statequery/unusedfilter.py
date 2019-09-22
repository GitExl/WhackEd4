from typing import Set

from whacked4.dehacked.statequery.filterbase import StateFilterBase
from whacked4.dehacked.statequery.thingfilter import ThingStateFilter
from whacked4.dehacked.statequery.weaponfilter import WeaponStateFilter


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
