from typing import List

from whacked4.dehacked.patch import Patch
from whacked4.dehacked.statequery.filterbase import StateFilterBase
from whacked4.dehacked.statequery.result import StateQueryResult
from whacked4.dehacked.statequery.sortbase import StateSortBase


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

    def execute(self) -> StateQueryResult:
        state_indices = set(range(len(self.patch.states)))

        for state_filter in self.state_filters:
            state_indices = state_filter.apply(state_indices)

        for state_sorter in self.state_sorters:
            state_indices = state_sorter.apply(state_indices)

        return StateQueryResult(self.patch.states, list(state_indices))
