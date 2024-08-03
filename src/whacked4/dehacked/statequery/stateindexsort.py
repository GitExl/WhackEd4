"""
State sort by index.
"""

from typing import List

from whacked4.dehacked.statequery.sortbase import StateSortBase


class StateIndexSort(StateSortBase):
    """
    Sort states by their index.
    """

    def apply(self, state_indices: List[int]) -> List[int]:
        return sorted(state_indices)
