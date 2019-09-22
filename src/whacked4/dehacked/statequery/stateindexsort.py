from typing import List

from whacked4.dehacked.statequery.sortbase import StateSortBase


class StateIndexSort(StateSortBase):

    def apply(self, state_indices: List[int]) -> List[int]:
        return sorted(state_indices)
